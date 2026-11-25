# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lê Hải Anh (2A202603986) · Người gắn nhãn 2: ... *(chờ TV4 gửi bộ nhãn độc lập)* (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...% *(cập nhật sau khi ghép bộ nhãn của TV4; yêu cầu ≥ 80% tức ≥ 16/20)*

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- *(Cập nhật sau khi so nhãn với TV4)*

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`); cảnh báo khi vượt 2% tổng yêu cầu mỗi ngày | Nhận diện mã đơn sàn TMĐT để tra ngược mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát theo giờ: tin nhắn báo "đã hoàn" nhưng không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ gửi thông báo "đã hoàn" khi API sổ cái trả `ok`; gặp lỗi 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại trong 7 ngày (`request_reopened_7d`) với lý do thắc mắc số tiền dù kiểm tra tính đúng, tổng hợp theo tuần; ngưỡng > 1% | Cập nhật mẫu tin nhắn luôn hiển thị phép tính chi tiết (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `request_escalated` với `reason = thieu_du_lieu` theo từng `loai`, theo dõi hằng ngày | Giữ cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần (`audit_sample_checked`) đối chiếu bảng giá hiện hành; ngưỡng lệch ≥ 1% số đơn | Xoá bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi `price_table_version` vào `trace_id` | Kế toán trưởng |
