"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""

import math
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
    if max_lan_chay is not None:
        runs = runs[runs["attempt"] <= max_lan_chay]
        reqs = reqs.copy()
        reqs.loc[reqs["so_lan_chay"] > max_lan_chay, "ket_qua"] = "chuyen_nhan_vien"

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


if __name__ == "__main__":
    runs = pd.read_csv("logix_runs.csv")
    reqs = pd.read_csv("logix_requests.csv", keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f"{ten:12s} {gia_tri:>14,.0f}")
    # Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print("\nA3 - theo loai:")
    for loai in ["noi_dia", "hang_nang", "quoc_te", "doi_tac"]:
        sub_reqs = reqs[reqs["loai"] == loai]
        sub_runs = runs[runs["request_id"].isin(sub_reqs["request_id"])]
        kq = mo_hinh(sub_runs, sub_reqs)
        ti_le_tc = kq["thanh_cong"] / len(sub_reqs)
        lan_chay_tb = len(sub_runs) / len(sub_reqs)
        print(
            f"{loai:10s} | n={len(sub_reqs):4d} | tc={ti_le_tc:5.1%} | chay={lan_chay_tb:4.2f} | cps={kq['cps']:8,.0f}"
        )

    # Nhiệm vụ A4: chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang
    print("\nA4 - chi phi co dinh:")
    pham_vi_reqs = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    pham_vi_runs = runs[runs["request_id"].isin(pham_vi_reqs["request_id"])]
    kq_pv = mo_hinh(pham_vi_runs, pham_vi_reqs)
    ti_le_tc_pv = kq_pv["thanh_cong"] / len(pham_vi_reqs)
    for khoi_luong in [45000, 22500]:
        viec_tc_thang = khoi_luong * ti_le_tc_pv
        co_dinh_moi_viec = 40_000_000 / viec_tc_thang
        tong_cps = kq_pv["cps"] + co_dinh_moi_viec
        print(
            f"KL={khoi_luong:5d} | tc/thang={viec_tc_thang:8,.0f} | co_dinh/viec={co_dinh_moi_viec:6,.0f} | tong_cps={tong_cps:7,.0f}"
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

    print("\nB4 - xem lai 100%:")
    # Nếu xem lại 100% yêu cầu trong phạm vi, mỗi yêu cầu tốn thêm thời gian xem lại trung bình
    reqs_100 = pham_vi_reqs.copy()
    tb_phut_xem_lai = reqs_100.loc[
        reqs_100["duoc_xem_lai"] == 1, "phut_xem_lai_simulated"
    ].mean()
    reqs_100["phut_xem_lai_simulated"] = tb_phut_xem_lai
    kq_b4 = mo_hinh(pham_vi_runs, reqs_100)
    print(
        f"Xem lai 100% (tb {tb_phut_xem_lai:.2f} phut) | cps={kq_b4['cps']:7,.0f} | so voi 12,000: {kq_b4['cps'] / BASELINE:.2f}x"
    )
    # Nhiệm vụ D: tính cỡ mẫu 5 kịch bản (D1) và tỉ lệ mở lại trong 7 ngày
    print("\nD1 - co mau:")
    z_a, z_b = 1.959964, 0.841621
    h_5 = 2 * math.asin(math.sqrt(0.75)) - 2 * math.asin(math.sqrt(0.70))
    n_req = math.ceil(2 * ((z_a + z_b) / h_5) ** 2)
    icc = 0.02
    deff_75 = 1 + (75 - 1) * icc
    n_eff_75 = math.ceil(n_req * deff_75)
    cum_nv = math.ceil(n_eff_75 / 75)
    # Với 20 nhân viên/nhóm và 6 depot/nhóm: tính cỡ mẫu hiệu dụng
    m_20nv = (
        math.ceil(n_req * (1 - icc) / (20 - n_req * icc))
        if 20 > n_req * icc
        else float("inf")
    )
    ti_le_mo_lai = (reqs["mo_lai_trong_7_ngay"] == 1).mean()
    print(f"a) theo yeu cau: {n_req} moi nhom")
    print(
        f"b) theo nhan vien (m=75): deff={deff_75:.2f}, n={n_eff_75} ({cum_nv} nv/nhom)"
    )
    print(f"c) 20 nv/nhom: can toi thieu {m_20nv} yeu cau/nv")
    print("d) 6 depot/nhom: khong du cum (toi thieu 20 cum/nhom)")
    print(
        f"e) chenh 6 diem (859/nhom), 20 nv/nhom: deff_max={20 * 200 / (859):.2f}, thieu cum neu m lon"
    )
    print(f"ti le mo_lai_trong_7_ngay hien tai: {ti_le_mo_lai:.2%}")
