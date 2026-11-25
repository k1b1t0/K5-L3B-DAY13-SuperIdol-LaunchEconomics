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
- **Nhiệm vụ E & Duyệt chéo:** Đặc tả chỉ số, 6 event có `trace_id` và rủi ro kinh tế trong [chi_so.md](chi_so.md); tổng hợp 1 trang vào [ho_so_launch_v0.md](ho_so_launch_v0.md); phiếu chấm hội đồng tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí & Độ nhạy (`bang_chi_phi.md`):**
  - Ba phép thử A1 đạt (`1,20 · 1,25 · 1,25`). Chi phí mỗi việc thành công đạt **4.472 đ** (`simulated`), gấp **16,28×** hoá đơn token+tool/yêu cầu (274,7 đ); khoản lớn nhất là **Làm lại** (**51,77%**, `simulated`).
  - Phạm vi đề xuất `noi_dia` (**2.696 đ**, 0,22×) và `hang_nang` (**8.221 đ**, 0,69×); loại `quoc_te` (**22.515 đ**, 1,88×, thành công 27,3%) và `doi_tac` (**10.215 đ**, 0,85×) (`simulated`). Cộng cố định 40 triệu đ/tháng cho phạm vi pilot đạt **4.599 đ** (0,38×) ở 45.000 yc/tháng và **5.784 đ** (0,48×) ở nửa khối lượng (`simulated`).
  - Ba yếu tố nhạy nhất (`simulated`): (1) Số ca làm lại (+51,77%), (2) Tỉ lệ xem lại (+40,70%), (3) Lương nhân viên (+23,12%). Giới hạn chạy tối đa **2 lần** cho tổng chi phí cả hệ thống thấp nhất (**6.901.220 đ**, `simulated`). Xem lại 100% tốn **11.743 đ** (`0,98×` với 9 phút làm lại) hoặc **12.415 đ** (`1,03×` với 15,3 phút làm lại) (`simulated`).
- **Chỉ số & Pilot (`chi_so.md`, `pilot_plan.yaml`):**
  - Trong đợt chạy thử: đóng 24h không mở lại 7 ngày **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot **3,97%**).
  - Kế hoạch pilot chia theo `staff` **20 nhân viên/nhóm** (`control_share: 0.5`, `n_per_arm: 859`, `design_effect: 6.96`, `mde: 0.06`, `m >= 299`, ngày quyết định `2026-12-16`) kèm 3 luật dừng an toàn/chi phí/sử dụng.
- **Lỗi & Đề xuất Gate 2a (`bang_loi.md`, `ho_so_launch_v0.md`):**
  - [bang_loi.md](bang_loi.md) hoàn tất ghép 20 nhãn độc lập giữa Người gắn nhãn 1 và Người gắn nhãn 2 đạt đồng thuận **20/20 (100%)** kèm bảng khắc phục 5 ca (`9, 7, 18, 4, 17`).
  - Nhóm chốt **Go có điều kiện** (4 điều kiện: vá khoá chống trùng & đối soát sổ cái Ca 7/Ca 20; ký xác nhận đánh đổi MDE 6 điểm / power `0,64` ở mức 5 điểm; bật đủ event `trace_id` + đo phút thật + kiểm toán lỗi ngầm; giữ tỉ lệ xem lại < 50% và ≤ 4,8 phút/ca).
- **Kết quả duyệt chéo từ hội đồng:** Chưa ghi nhận vì chưa có dữ liệu phản hồi/hồ sơ duyệt chéo từ nhóm hội đồng (không tự bịa kết quả theo `RULES.md`; [phieu_cham.md](phieu_cham.md) giữ nguyên mẫu chờ bổ sung khi có hồ sơ nhóm bạn).

## 5. Khó khăn và cách xử lý

- Thời gian nhân viên lấy từ hai cột `_simulated` nên nhóm gắn nhãn `simulated` nhất quán và bổ sung đo phút thực tế qua event `human_review_completed`, `staff_rework_completed` khi pilot.
- Khi rà soát chéo CP1–CP4, nhóm phát hiện và đã khắc phục hai lỗi trước khi chốt `main`: (1) bổ sung gán `phut_xem_lai_simulated = 0` và `phut_lam_lai_simulated = 0` khi cắt `max_lan_chay`, cùng chuẩn hoá mẫu số A4 (`1.200` yc) và tập ca `ok` ở B4 (`948` yc) trong `src/lab13.py`; (2) điều chỉnh `pilot_plan.yaml` từ `42` nhân viên/nhóm về `20` nhân viên/nhóm phù hợp quy mô 40 nhân viên (chấp nhận MDE 6 điểm, `n_per_arm: 859`, nêu rõ power `0,64` ở mức 5 điểm).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu hiện là giả lập và đợt chạy thử chưa có nhóm đối chứng nên chỉ báo cáo mức chỉ số quan sát được, chưa quy kết tác động nhân quả.
- Chỉ số phát hiện lỗi ngầm về sai mức tiền hoàn chưa đo được trực tiếp từ 6 event cơ bản, cần bổ sung event đối soát kiểm toán hằng tuần trước khi bắt đầu pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`).
