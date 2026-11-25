# Team

## Thông tin nhóm

- Tên nhóm: SuperIdol
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-SuperIdol-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: (cập nhật khi chốt bài nộp trên nhánh `main`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyen Thanh Nam | 2A202663213 | n4malias@gmail.com | (theo tai khoan n4malias@gmail.com) | Nhóm trưởng & Người viết code (trước giải lao) |
|   2 | Nguyen Minh Duc | 2A202603960 | nguyenminhduc2882005@gmail.com | k1b1t0 | Kiểm số → Code (sau giải lao) |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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
