# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: SuperIdol · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`; tổng 4.373.585 đ / 978 việc thành công; gấp **16,28×** hoá đơn token+tool 274,7 đ/yêu cầu). | Giả lập | Trưởng vận hành pilot |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại ×2 (**+51,77%**, lên 6.787 đ, `simulated`); 2) Tỉ lệ xem lại ×2 (**+40,70%**, lên 6.292 đ, `simulated`); 3) Lương +25% (**+23,12%**, lên 5.506 đ, `simulated`). | Giả lập | Kỹ sư phụ trách agent |
| 3 · So với nhân viên tự làm | Cả hệ thống (3 lần) **7.037.585 đ** = **5.865 đ/yc (0,49×** của 12.000 đ, `simulated`); giới hạn 2 lần rẻ nhất (**6.901.220 đ**, `simulated`). Theo loại: `noi_dia` **2.696 đ (0,22×)**, `hang_nang` **8.221 đ (0,69×)**, `doi_tac` **10.215 đ (0,85×)**, `quoc_te` **22.515 đ (1,88×, đắt hơn)** (`simulated`). Cộng cố định 40 triệu/tháng: **4.599 đ (0,38×)** ở 45.000 yc/tháng và **5.784 đ (0,48×)** ở nửa khối lượng (`simulated`). Xem lại 100% phạm vi: **11.743 đ (0,98×)** với 9 phút làm lại hoặc **12.415 đ (1,03×)** với 15,3 phút làm lại (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (1.200 yc): Chính (đóng 24h, không mở lại 7 ngày) = **82,83%** (994/1.200); Dùng (bỏ qua gợi ý) = **27,12%** (48/177); An toàn (mở lại 7 ngày) = **4,25%** (51/1.200; phạm vi pilot **3,97%**). Có 6 event có `trace_id` (lỗi ngầm sai mức tiền chưa đo được trực tiếp). | Xong, có bằng chứng | Kỹ sư phụ trách agent |
| 5 · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập đồng thuận **20/20 = 100%** (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm); đủ bảng khắc phục 5 ca (`9, 7, 18, 4, 17`) có cách phát hiện đo được và 1 vai trò phụ trách. | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang` (loại `quoc_te`, `doi_tac`), chia ngẫu nhiên theo `staff` **20 nhân viên/nhóm** (`n = 859`/nhóm, `DE = 6,96`, `m >= 299`, chấp nhận MDE **0,06** — **bất lợi:** power còn **0,64** nếu tác động thật chỉ 5 điểm), 50% đối chứng cùng thời gian, 3 luật dừng 4 vế, ngày chốt `2026-12-16`. | Giả lập | Trưởng vận hành pilot |
| 7 · Rủi ro kinh tế | (1) Số ca làm lại ×2 → CPS **6.787 đ (+51,77%**, `simulated`); (2) Xem lại 100% phạm vi → **11.743 đ (0,98×)** hoặc **12.415 đ (1,03×**, `simulated`); (3) Nửa khối lượng → chi phí cố định tăng gấp đôi (**2.370 đ/việc**, `simulated`). | Giả lập | Trưởng vận hành pilot |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1 (Vá lỗi hệ thống nghiêm trọng trước khi mở pilot):** Hoàn tất khoá chống trùng lệnh hoàn và đối soát bản ghi API sổ cái trước khi báo "đã hoàn tiền thành công" (Ca 7, Ca 20 trong `report/team/bang_loi.md`). **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-11-28`.
- **Điều kiện 2 (Xác nhận đánh đổi cỡ mẫu pilot):** Ký xác nhận chấp nhận mức chênh phát hiện được **MDE = 6 điểm** với 20 nhân viên/nhóm (`n = 859`, `DE = 6,96`, power còn **0,64** ở mức 5 điểm) do giới hạn tổng 40 nhân viên CSKH. **Người phụ trách:** Trưởng vận hành pilot · **Ngày kiểm tra:** `2026-11-28`.
- **Điều kiện 3 (Bật đủ event `trace_id` và đo thời gian thật):** Ghi đủ ≥ 6 event có `trace_id`, thay các cột `_simulated` bằng phút xem lại/làm lại đo thật sau tuần 1 và bổ sung event kiểm toán mẫu (`audit_sample_checked`) bắt lỗi ngầm sai mức tiền. **Người phụ trách:** Kỹ sư phụ trách agent · **Ngày kiểm tra:** `2026-12-02`.
- **Điều kiện 4 (Kế hoạch giảm xem lại theo bậc dưới 50%):** Giữ thời gian xem lại trung bình ≤ `4,8` phút/ca và giảm tỉ lệ xem lại < `50%` theo bậc, vì xem lại 100% đẩy chi phí lên **11.743–12.415 đ** (`0,98×–1,03×` mức `12.000 đ`, `simulated`). **Người phụ trách:** Trưởng nhóm CSKH · **Ngày kiểm tra:** `2026-12-02`.
