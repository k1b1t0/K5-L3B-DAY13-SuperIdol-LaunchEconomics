"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""

import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26  # đồng cho 1.000 token đầu vào
GIA_RA = 130  # đồng cho 1.000 token đầu ra
GIA_TOOL = 15  # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000  # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000  # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return sum((1.0 - p) ** (i - 1) for i in range(1, k + 1))


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, (
        "p=0,8, tối đa 2 lần → 1,20 lần chạy"
    )
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, (
        "p=0,8, chạy đến khi đúng → 1,25 lần chạy"
    )
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, (
        "p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy"
    )
    print("Ba phép thử đáp án biết trước: ĐẠT")


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(
    runs,
    reqs,
    gia_vao=26,
    gia_ra=130,
    gia_tool=15,
    luong_phut=2000,
    he_so_xem_lai=1.0,
    he_so_lam_lai=1.0,
    max_lan_chay=None,
):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs["request_id"].isin(reqs["request_id"])]
    if max_lan_chay is not None:
        runs = runs[runs["attempt"] <= max_lan_chay]
        vuot = reqs["so_lan_chay"] > max_lan_chay
        reqs.loc[vuot, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[vuot, ["phut_xem_lai_simulated", "phut_lam_lai_simulated"]] = 0

    token = (runs["tokens_in"].sum() / 1000.0) * gia_vao + (
        runs["tokens_out"].sum() / 1000.0
    ) * gia_ra
    tool = runs["tool_calls"].sum() * gia_tool
    xem_lai = reqs["phut_xem_lai_simulated"].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs["phut_lam_lai_simulated"].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs["ket_qua"] == "thanh_cong").sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float("inf")
    return {
        "token": token,
        "tool": tool,
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": cps,
    }


def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ p1 và p2."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (
            za * math.sqrt(2 * pb * (1 - pb))
            + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
        )
        ** 2
        / (p2 - p1) ** 2
    )


if __name__ == "__main__":
    runs = pd.read_csv("logix_runs.csv")
    reqs = pd.read_csv("logix_requests.csv", keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f"{ten:12s} {gia_tri:>14,.0f}")
    hoa_don = ket_qua["token"] + ket_qua["tool"]
    chay_lai_runs = runs[runs["attempt"] > 1]
    chay_lai = (
        (chay_lai_runs["tokens_in"].sum() / 1000.0) * GIA_VAO
        + (chay_lai_runs["tokens_out"].sum() / 1000.0) * GIA_RA
        + chay_lai_runs["tool_calls"].sum() * GIA_TOOL
    )
    hoa_don_moi_yc = hoa_don / len(reqs)
    print(f"chay_lai     {chay_lai:>14,.0f}")
    print(f"hoa_don/yc   {hoa_don_moi_yc:>14,.1f}")
    print(f"gap_hoa_don  {ket_qua['cps'] / hoa_don_moi_yc:>14,.2f}x")

    # Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print("\nA3 - theo loai:")
    for loai in ["noi_dia", "hang_nang", "quoc_te", "doi_tac"]:
        sub_reqs = reqs[reqs["loai"] == loai]
        kq = mo_hinh(runs, sub_reqs)
        ti_le_tc = kq["thanh_cong"] / len(sub_reqs)
        lan_chay_tb = len(runs[runs["request_id"].isin(sub_reqs["request_id"])]) / len(
            sub_reqs
        )
        print(
            f"{loai:10s} | n={len(sub_reqs):4d} | tc={ti_le_tc:5.1%} | chay={lan_chay_tb:4.2f} | cps={kq['cps']:8,.0f} | vs_12k={kq['cps'] / BASELINE:.2f}x"
        )

    # Nhiệm vụ A4: chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang
    print("\nA4 - chi phi co dinh:")
    pham_vi_reqs = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    pham_vi_runs = runs[runs["request_id"].isin(pham_vi_reqs["request_id"])]
    kq_pv = mo_hinh(pham_vi_runs, pham_vi_reqs)
    ti_le_tc_tren_toan_mau = kq_pv["thanh_cong"] / len(reqs)
    for khoi_luong in [45000, 22500]:
        viec_tc_thang = khoi_luong * ti_le_tc_tren_toan_mau
        co_dinh_moi_viec = 40_000_000 / viec_tc_thang
        tong_cps = kq_pv["cps"] + co_dinh_moi_viec
        print(
            f"KL={khoi_luong:5d} | tc/thang={viec_tc_thang:8,.0f} | co_dinh/viec={co_dinh_moi_viec:6,.0f} | tong_cps={tong_cps:7,.0f} | vs_12k={tong_cps / BASELINE:.2f}x"
        )

    # Nhiệm vụ B1-B4: độ nhạy, đổi cặp, giới hạn chạy lại, xem lại 100%
    print("\nB1 - do nhay:")
    cps_goc = ket_qua["cps"]
    kich_ban_b1 = [
        ("Gia token x2", dict(gia_vao=52, gia_ra=260)),
        ("Gia token /2", dict(gia_vao=13, gia_ra=65)),
        ("Xem lai x2", dict(he_so_xem_lai=2.0)),
        ("Xem lai /2", dict(he_so_xem_lai=0.5)),
        ("Lam lai x2", dict(he_so_lam_lai=2.0)),
        ("Lam lai /2", dict(he_so_lam_lai=0.5)),
        ("Luong +25%", dict(luong_phut=2500)),
        ("Max 2 lan", dict(max_lan_chay=2)),
        ("Max 1 lan", dict(max_lan_chay=1)),
    ]
    for ten_kb, kw in kich_ban_b1:
        kq_kb = mo_hinh(runs, reqs, **kw)
        pct = (kq_kb["cps"] - cps_goc) / cps_goc * 100
        print(f"{ten_kb:16s} | cps={kq_kb['cps']:7,.0f} | {pct:+6.2f}%")

    print("\nB2 - doi cap:")
    kq_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    print(
        f"Token x2 + Xem lai x2 | cps={kq_b2['cps']:7,.0f} | {(kq_b2['cps'] - cps_goc) / cps_goc * 100:+6.2f}%"
    )

    print("\nB3 - gioi han chay lai:")
    for max_k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=max_k)
        khong_tc = len(reqs) - kq_k["thanh_cong"]
        chi_phi_he_thong = kq_k["tong"] + khong_tc * BASELINE
        print(
            f"Max {max_k} lan | tong_tro_ly={kq_k['tong']:9,.0f} | khong_tc={khong_tc:3d} | he_thong={chi_phi_he_thong:9,.0f} | cps={kq_k['cps']:7,.0f}"
        )

    print("\nB4 - xem lai 100% (pham vi noi_dia + hang_nang):")
    co_ok_ids = set(pham_vi_runs.loc[pham_vi_runs["status"] == "ok", "request_id"])
    so_xem_lai_100 = len(co_ok_ids)
    so_lam_lai_pv = int((pham_vi_reqs["ket_qua"] == "lam_lai").sum())
    token_tool_pv = kq_pv["token"] + kq_pv["tool"]
    tb_phut_lam_lai_all = reqs.loc[
        reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"
    ].mean()
    for nhan_b4, phut_ll in [
        ("9 phut/ca (de)", 9.0),
        (f"{tb_phut_lam_lai_all:.1f} phut/ca (du lieu)", tb_phut_lam_lai_all),
    ]:
        tien_xl = so_xem_lai_100 * 5 * LUONG_PHUT
        tien_ll = so_lam_lai_pv * phut_ll * LUONG_PHUT
        tong_b4 = token_tool_pv + tien_xl + tien_ll
        cps_b4 = tong_b4 / kq_pv["thanh_cong"]
        # Mức phút xem lại tối đa để tổng chi phí <= BASELINE * thanh_cong
        hoa_von_phut = (
            BASELINE * kq_pv["thanh_cong"] - token_tool_pv - tien_ll
        ) / (so_xem_lai_100 * LUONG_PHUT)
        print(
            f"{nhan_b4:24s} | co_ok={so_xem_lai_100} | lam_lai={so_lam_lai_pv} | tong={tong_b4:10,.0f} | cps={cps_b4:7,.0f} ({cps_b4 / BASELINE:.2f}x) | hoa_von={hoa_von_phut:.1f} phut"
        )

    # Nhiệm vụ D: tính cỡ mẫu 5 kịch bản (D1) và tỉ lệ mở lại trong 7 ngày
    print("\nD1 - co mau:")
    n_req = co_mau(0.70, 0.75)
    icc = 0.02
    deff_75 = 1 + (75 - 1) * icc
    n_eff_75 = math.ceil(n_req * deff_75)
    cum_nv = math.ceil(n_eff_75 / 75)
    max_nv_20 = int(20 / icc)
    max_depot_6 = int(6 / icc)
    n_6pt = co_mau(0.70, 0.76)
    m_min_6pt = math.ceil(n_6pt * (1 - icc) / (20 - n_6pt * icc))
    deff_6pt = 1 + (m_min_6pt - 1) * icc
    za = NormalDist().inv_cdf(0.975)
    p1_t, p2_t, pb_t = 0.70, 0.75, 0.725
    se0 = math.sqrt(2 * pb_t * (1 - pb_t) / n_6pt)
    se1 = math.sqrt((p1_t * (1 - p1_t) + p2_t * (1 - p2_t)) / n_6pt)
    power_at_5pt = NormalDist().cdf((0.05 - za * se0) / se1)
    ti_le_mo_lai = (reqs["mo_lai_trong_7_ngay"] == 1).mean()
    ti_le_mo_lai_pv = (pham_vi_reqs["mo_lai_trong_7_ngay"] == 1).mean()
    print(f"a) theo yeu cau: {n_req} moi nhom")
    print(
        f"b) theo nhan vien (m=75): deff={deff_75:.2f}, n={n_eff_75} ({cum_nv} nv/nhom, tong {cum_nv * 2} > 40 nv -> khong du)"
    )
    print(f"c) 20 nv/nhom: co mau hieu dung toi da {max_nv_20} < {n_req} -> khong dat")
    print(f"d) 6 depot/nhom: co mau hieu dung toi da {max_depot_6} < {n_req} -> khong dat")
    print(
        f"e) chenh 6 diem ({n_6pt}/nhom), 20 nv/nhom: m>={m_min_6pt} yc/nv, DE={deff_6pt:.2f}; neu tac dong that 5 diem thi power={power_at_5pt:.2f}"
    )
    print(
        f"ti le mo_lai_trong_7_ngay: toan bo={ti_le_mo_lai:.2%} ({(reqs['mo_lai_trong_7_ngay'] == 1).sum()}/{len(reqs)}), pham vi={ti_le_mo_lai_pv:.2%} ({(pham_vi_reqs['mo_lai_trong_7_ngay'] == 1).sum()}/{len(pham_vi_reqs)})"
    )
