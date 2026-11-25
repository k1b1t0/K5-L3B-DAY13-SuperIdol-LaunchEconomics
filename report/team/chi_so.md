# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu chuyển nhân viên | Số yêu cầu có `ket_qua == 'chuyen_nhan_vien'` chia tổng số yêu cầu | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn phí sai mức tiền (ngầm) | Số ca có sai lệch `so_tien_vnd` phát hiện khi kiểm tra chéo chia số ca `thanh_cong` | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | Hệ thống tiếp nhận | `request_id`, `loai`, `depot`, `trace_id` | Khi nhận yêu cầu hoàn phí mới |
| `agent_run_finished` | Agent hoàn phí | `request_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls`, `trace_id` | Khi mỗi lần chạy của agent kết thúc |
| `human_review_completed` | Nhân viên xử lý | `request_id`, `duoc_xem_lai`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên xem lại gợi ý của agent |
| `request_escalated` | Agent / Hệ thống | `request_id`, `ket_qua` (`chuyen_nhan_vien`), `so_lan_chay`, `trace_id` | Khi vượt quá giới hạn lần chạy hoặc từ chối tự động |
| `request_closed_24h` | Hệ thống ticket | `request_id`, `dong_trong_24h`, `ket_qua`, `trace_id` | Tại mốc 24 giờ sau khi tiếp nhận yêu cầu |
| `request_reopened_7d` | Hệ thống ticket | `request_id`, `mo_lai_trong_7_ngay`, `nguyen_nhan`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **% yêu cầu đóng trong 24h và không mở lại trong 7 ngày:** tính từ `request_received`, `request_closed_24h` và `request_reopened_7d` (nối qua `request_id`, `trace_id`).
- **Tỉ lệ bỏ qua gợi ý:** tính từ `human_review_completed` (`quyet_dinh_xem_lai` là `sua` hoặc `bo` chia tổng số ca `duoc_xem_lai == 1`).
- **Tỉ lệ lỗi lọt đến khách:** tính từ `request_reopened_7d` (`mo_lai_trong_7_ngay == 1`) chia tổng số `request_received`.
- **Tỉ lệ yêu cầu chuyển nhân viên:** tính từ `request_escalated` chia tổng số `request_received`.
- **Tỉ lệ hoàn phí sai mức tiền (ngầm):** **chưa đo được** từ 6 event trên vì chưa có event kiểm toán/đối soát số tiền sau khi đóng (`audit_amount_checked`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca phải làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,77%** (từ 4.472 đ lên **6.787 đ**) | Tỉ lệ `mo_lai_trong_7_ngay` vượt ngưỡng 4,25% hoặc `lam_lai` tăng liên tục theo tuần | Kích hoạt luật dừng an toàn, rà soát nguyên nhân gốc trong bảng lỗi và tạm thu hẹp phạm vi pilot | Trưởng vận hành pilot |
| Tỉ lệ nhân viên phải xem lại tăng lên 100% | Chi phí mỗi việc thành công ở phạm vi `noi_dia` + `hang_nang` lên **11.743 đ** (**0,98×** với 9 phút làm lại) hoặc **12.415 đ** (**1,03×** mức 12.000 đ nếu làm lại 15,3 phút/ca như dữ liệu, `simulated`) | Tỉ lệ `duoc_xem_lai` vượt 50% hoặc thời gian xem lại trung bình > 4,8 phút/ca | Tạm dừng mở rộng rollout, tinh chỉnh ngưỡng tự tin của agent để giảm ca phải xem lại | Kỹ sư phụ trách agent |
