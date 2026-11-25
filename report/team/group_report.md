# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: SuperIdol
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ launch v0 (Gate 2a) cho trợ lý hoàn phí LogiX-VN từ dữ liệu giả lập 1.200 yêu cầu (1.624 lần chạy) để trả lời bốn câu hỏi: (1) có đáng chạy không qua chi phí mỗi việc thành công và độ nhạy, (2) nhân viên có dùng không qua chỉ số và event có `trace_id`, (3) khi hỏng xử lý thế nào qua phân loại 20 ca lỗi Google PAIR, và (4) pilot thiết kế thế nào để tách được tác động, đủ cỡ mẫu và có luật dừng rõ ràng.

## 3. Giải pháp

- **Nhiệm vụ A–B (Mô hình chi phí & Độ nhạy):** Cài đặt trong [src/lab13.py](../../src/lab13.py) (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `mo_hinh`, A3, A4, B1–B4) và tổng hợp vào [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi & Khắc phục):** Hai người gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc, đối chiếu đồng thuận và lập bảng khắc phục 5 ca đại diện đủ 5 loại trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu D1 trong `src/lab13.py`, kiểm tra 5 câu tách tác động D2 và hoàn thiện các trường + luật dừng 4 vế trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E & Duyệt chéo:** Đặc tả chỉ số, 6 event có `trace_id` và rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp 1 trang vào [ho_so_launch_v0.md](ho_so_launch_v0.md); chấm chéo nhóm bạn tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Kinh tế & Vận hành (đã tính trong `src/lab13.py` và `chi_so.md`):**
  - Ba phép thử A1 đạt (`1,20 · 1,25 · 1,25`). Chi phí mỗi việc thành công đạt **4.472 đ** (`simulated`).
  - Trong đợt chạy thử: tỉ lệ đóng trong 24h và không mở lại 7 ngày là **82,83%** (994/1.200); tỉ lệ bỏ qua gợi ý là **27,12%** (48/177); tỉ lệ lỗi lọt đến khách (`mo_lai_trong_7_ngay`) là **4,25%** (51/1.200).
  - Rủi ro kinh tế nổi bật: nếu số ca làm lại tăng gấp đôi, chi phí mỗi việc thành công tăng **+51,77%** lên **6.787 đ** (`simulated`); nếu phải xem lại 100% ở phạm vi `noi_dia` + `hang_nang`, chi phí vượt ngưỡng 12.000 đ nhân viên tự làm (`simulated`).
- **Lỗi & Pilot & Đề xuất Gate 2a:** *(Cập nhật sau khi hoàn thiện `bang_loi.md`, `pilot_plan.yaml` và `ho_so_launch_v0.md`)*.
- **Kết quả duyệt chéo từ hội đồng:** *(Cập nhật sau phiên duyệt chéo 17:00)*.

## 5. Khó khăn và cách xử lý

- Thời gian nhân viên lấy từ hai cột `_simulated` nên nhóm phải gắn nhãn `simulated` nhất quán và bổ sung cơ chế đo phút thực tế qua event `staff_review_decision`, `staff_rework_completed` trong giai đoạn pilot.
- Quy mô 40 nhân viên bị giới hạn cỡ mẫu hiệu dụng theo cụm (ICC = 0,02), cần cân nhắc đánh đổi giữa mức chênh phát hiện được và độ dài thời gian pilot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu đánh giá hiện là giả lập và chưa có nhóm đối chứng trong đợt chạy thử, nên chỉ kết luận được mức chỉ số trong đợt chạy thử chứ chưa quy kết được tác động nhân quả.
- Chỉ số phát hiện lỗi ngầm về sai mức tiền hoàn hiện chưa đo được trực tiếp từ 6 event cơ bản, cần bổ sung event đối soát kiểm toán hằng tuần trước khi triển khai pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
