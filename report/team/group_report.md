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
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu D1 trong `src/lab13.py`, kiểm tra 5 câu tách tác động D2 và hoàn thiện các trường + 3 luật dừng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E & Duyệt chéo:** Đặc tả chỉ số, 6 event có `trace_id` và rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp 1 trang vào [ho_so_launch_v0.md](ho_so_launch_v0.md); chấm chéo nhóm bạn tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí & Độ nhạy (`bang_chi_phi.md`):**
  - Ba phép thử A1 đạt (`1,20 · 1,25 · 1,25`). Chi phí mỗi việc thành công đạt **4.472 đ** (`simulated`), gấp **16,28×** hoá đơn token+tool/yêu cầu (275 đ); khoản lớn nhất là **Làm lại** (**51,77%**, `simulated`).
  - Phạm vi đề xuất `noi_dia` (**2.696 đ**, 0,22×) và `hang_nang` (**8.221 đ**, 0,69×); loại `quoc_te` (**22.515 đ**, 1,88×, thành công 27,3%) (`simulated`). Cộng cố định 40 triệu đ/tháng cho phạm vi này đạt **4.384 đ** (0,37×) ở 45.000 yc/tháng và **5.354 đ** (0,45×) ở nửa khối lượng (`simulated`).
  - Ba yếu tố nhạy nhất: (1) Số ca làm lại (+51,77%), (2) Tỉ lệ xem lại (+40,70%), (3) Lương nhân viên (+23,12%). Xem lại 100% tốn **12.962 đ** (`simulated`, 1,08× mức 12.000 đ).
- **Chỉ số & Pilot (`chi_so.md`, `pilot_plan.yaml`):**
  - Trong đợt chạy thử: đóng 24h không mở lại 7 ngày **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại 7 ngày **4,25%** (51/1.200).
  - Kế hoạch pilot chọn chia theo `staff` (`control_share: 0.5`, `n_per_arm: 3100`, `design_effect: 2.48`, `clusters_per_arm: 42`, `mde: 0.05`, ngày quyết định `2026-12-16`) kèm 3 luật dừng an toàn/chi phí/sử dụng.
- **Lỗi, Đề xuất Gate 2a & Duyệt chéo:** *(Cập nhật sau khi ghép bộ nhãn TV4 vào `bang_loi.md`, chốt đề xuất từ `ho_so_launch_v0.md` và nhận kết quả chấm từ hội đồng lúc 17:00)*.

## 5. Khó khăn và cách xử lý

- Thời gian nhân viên lấy từ hai cột `_simulated` nên nhóm gắn nhãn `simulated` nhất quán và bổ sung đo phút thực tế qua event `human_review_completed`, `staff_rework_completed` khi pilot.
- Khi rà soát chéo CP1–CP4, phát hiện hai điểm cần hiệu chỉnh trước khi chốt hồ sơ: (1) trong `src/lab13.py`, nhánh `max_lan_chay` chưa đặt `phut_xem_lai_simulated` và `phut_lam_lai_simulated` về `0` khiến số B1/B3 lệch so với mô tả; (2) `pilot_plan.yaml` đang ghi `clusters_per_arm: 42` mỗi nhóm (tổng 84 người) trong khi LogiX-VN chỉ có 40 nhân viên, cần cân nhắc chốt phương án 20 nhân viên/nhóm (MDE 6 điểm, `n_per_arm: 859`).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu hiện là giả lập và đợt chạy thử chưa có nhóm đối chứng nên chỉ báo cáo mức chỉ số quan sát được, chưa quy kết tác động nhân quả.
- Chỉ số phát hiện lỗi ngầm về sai mức tiền hoàn chưa đo được trực tiếp từ 6 event cơ bản, cần bổ sung event đối soát kiểm toán hằng tuần trước khi bắt đầu pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
