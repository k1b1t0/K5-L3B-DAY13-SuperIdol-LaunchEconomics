# Team

## Thông tin nhóm

- Tên nhóm: SuperIdol
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-SuperIdol-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/k1b1t0/K5-L3B-DAY13-SuperIdol-LaunchEconomics` · Nhánh nộp: `main` (commit chốt là HEAD mới nhất trên `main` sau khi hợp nhất và rà soát toàn bộ nhánh)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyen Thanh Nam | 2A202663213 | n4malias@gmail.com | (theo tai khoan n4malias@gmail.com) | Nhóm trưởng & Người viết code (trước giải lao) |
|   2 | Nguyen Minh Duc | 2A202603960 | nguyenminhduc2882005@gmail.com | k1b1t0 | Kiểm số → Code (sau giải lao) |
|   3 | Lê Hải Anh | 2A202603986 | lehaianh252005@gmail.com | haianh020505 | Người gắn nhãn 1 & Duyệt chéo |
|   4 | Lê Thành Nguyên | 2A202603733 | nguyenngungonvc@gmail.com | NguyenLTpk | Người gắn nhãn 2 & Giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenThanhNam-2A202663213

### Phần việc phụ trách

- Nhóm trưởng & Người viết code (trước giải lao): khởi tạo/cấu hình repo nhóm, code `src/lab13.py` (A1–A4, B1–B4), hoàn thiện `report/team/chi_so.md` (E1, E2) và test lại `src/lab13.py` cuối buổi.

### Đóng góp cụ thể

- Viết 3 hàm A1 đạt cả 3 phép thử (`1,20 · 1,25 · 1,25`), viết `mo_hinh` (A2) và các phần tính toán A3, A4, B1–B4 trong `src/lab13.py`.
- Tính thử 3 chỉ số trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`), đề xuất 2 chỉ số bổ sung, liệt kê 6 event có `trace_id`, kiểm tra chéo và 2 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
- Viết báo cáo cá nhân `report/team/2A202663213_NguyenThanhNam.md`.

### Bằng chứng

- `src/lab13.py` chạy thông suốt, `Ba phép thử đáp án biết trước: ĐẠT`, `cps = 4,472`.
- `report/team/chi_so.md` và `report/team/2A202663213_NguyenThanhNam.md` trên nhánh `nguyenthanhnam`.

## NguyenMinhDuc-2A202603960

### Phần việc phụ trách

- Kiểm số đối chiếu A1–A4, B1–B4 và hoàn thiện `report/team/bang_chi_phi.md`.
- Code phần D1 (cỡ mẫu) và tỉ lệ `mo_lai_trong_7_ngay` trong `src/lab13.py` (sau giải lao).
- Hoàn thiện `report/team/pilot_plan.yaml` và báo cáo cá nhân `report/team/2A202603960_NguyenMinhDuc.md`.

### Đóng góp cụ thể

- Điền đầy đủ bảng A1–A4, B1–B4, gắn nhãn `simulated` và trả lời các câu hỏi trong `report/team/bang_chi_phi.md`.
- Code phần tính cỡ mẫu D1 (5 kịch bản) và tỉ lệ `mo_lai_trong_7_ngay` trong `src/lab13.py`.
- Điền hết dấu `?`, viết 5 câu D2 và 3 luật dừng đủ 4 vế trong `report/team/pilot_plan.yaml`, kiểm tra hợp lệ bằng `yaml.safe_load`.

### Bằng chứng

- `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `src/lab13.py` (phần D1) và `report/team/2A202603960_NguyenMinhDuc.md` trên nhánh `2A202603960_NguyenMinhDuc`.

## LeHaiAnh-2A202603986

### Phần việc phụ trách

- Người gắn nhãn 1 & Duyệt chéo: rà soát điều kiện "Xong khi" (CP1–CP2), gắn nhãn độc lập 20 ca lỗi, đối chiếu đồng thuận và lập bảng khắc phục 5 ca (`report/team/bang_loi.md`), rà soát D2 & luật dừng (`report/team/pilot_plan.yaml`), chấm chéo Gate 2a (`report/team/phieu_cham.md`) và viết báo cáo nhóm (`report/team/group_report.md`).

### Đóng góp cụ thể

- Rà soát `src/lab13.py` ở CP1–CP2 và `pilot_plan.yaml` ở CP4 (phát hiện lỗi `max_lan_chay` chưa đặt phút simulated về 0, mẫu số A4/B4 và lỗi `42` nhân viên/nhóm vượt quá tổng 40 nhân viên).
- Gắn nhãn độc lập 20 ca lỗi, ghép 20 nhãn của Người gắn nhãn 2 đạt đồng thuận **20/20 (100%)** và lập bảng khắc phục 5 ca đại diện đủ 5 loại trong `report/team/bang_loi.md`.
- Viết báo cáo nhóm `report/team/group_report.md` và báo cáo cá nhân `report/team/2A202603986_LeHaiAnh.md` *(đã merge vào `main`; riêng `report/team/phieu_cham.md` giữ nguyên mẫu do chưa có hồ sơ nhóm bạn)*.

### Bằng chứng

- Các commit trên nhánh `haianh` (`c0581f0`–`7334fd4`, đã merge vào `main`): `report/team/bang_loi.md`, `report/team/group_report.md`, `report/team/2A202603986_LeHaiAnh.md`.

## LeThanhNguyen-2A202603733

### Phần việc phụ trách

- Người gắn nhãn 2 & Giữ hồ sơ: hoàn thiện thông tin thành viên và tổng hợp đóng góp trong `TEAM.md`, giữ và hoàn thiện hồ sơ 1 trang `report/team/ho_so_launch_v0.md` (7 mục + đề xuất Gate 2a), gắn nhãn độc lập 20 ca lỗi gửi Người gắn nhãn 1, hợp nhất các nhánh và kiểm tra tuân thủ cuối buổi trên `main`.

### Đóng góp cụ thể

- Cập nhật đầy đủ bảng 4 thành viên, URL repo/nhánh nộp và tổng hợp đóng góp trong `TEAM.md`.
- Đọc và gắn nhãn độc lập 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` bàn giao cho Người gắn nhãn 1 ghép vào `report/team/bang_loi.md` (đạt đồng thuận `20/20 = 100%`).
- Hợp nhất các nhánh về `main`, đồng bộ và khắc phục các sai lệch kỹ thuật đã được nhóm cảnh báo trong `src/lab13.py` (`max_lan_chay`, A4, B4, D1), `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml` (`20` nhân viên/nhóm, MDE `0,06`, `n = 859`, `DE = 6,96`) và `report/team/group_report.md`.
- Hoàn thiện 7 mục hồ sơ trong `report/team/ho_so_launch_v0.md` (gắn nhãn `simulated` đầy đủ, ghi nhận mọi con số bất lợi và chốt đề xuất **Go có điều kiện** kèm 4 điều kiện có vai trò và ngày kiểm tra).
- Chạy rà soát tuân thủ cuối buổi và viết báo cáo cá nhân `report/team/2A202603733_LeThanhNguyen.md`.

### Bằng chứng

- Nhánh `lethanhnguyen` (`d7de5bc`, đã merge vào `main`) và commit hoàn thiện trên `main`: `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603733_LeThanhNguyen.md`, cùng các bản đồng bộ đã kiểm chứng từ `src/lab13.py`.
