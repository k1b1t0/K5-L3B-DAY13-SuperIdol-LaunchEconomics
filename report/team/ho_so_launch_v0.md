# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: SuperIdol · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`; tổng 4.373.585 đ / 978 việc thành công; gấp **16,28×** hoá đơn token+tool 275 đ/yêu cầu). | Giả lập | Trưởng vận hành pilot |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại ×2 (**+51,77%**, lên 6.787 đ, `simulated`); 2) Tỉ lệ xem lại ×2 (**+40,70%**, lên 6.292 đ, `simulated`); 3) Lương +25% (**+23,12%**, lên 5.506 đ, `simulated`). | Giả lập | Kỹ sư phụ trách agent |
| 3 · So với nhân viên tự làm | Cả hệ thống 1.200 yc: **7.037.585 đ** = **5.865 đ/yc (0,49×** mức 12.000 đ, `simulated`). Theo loại: `noi_dia` **2.696 đ (0,22×)**, `hang_nang` **8.221 đ (0,69×)**, `doi_tac` **10.215 đ (0,85×)**, `quoc_te` **22.515 đ (1,88×, đắt hơn)** (`simulated`). Cộng cố định 40 triệu/tháng: **4.384 đ (0,37×)** ở 45.000 yc/tháng (`simulated`). Xem lại 100% phạm vi: **12.962 đ (1,08×**, `simulated`). *(Lưu ý: code `max_lan_chay`/A4/B4 đang lệch > 2% cần sửa).* | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (1.200 yc): Chính (đóng 24h, không mở lại 7 ngày) = **82,83%** (994/1.200); Dùng (bỏ qua gợi ý) = **27,12%** (48/177); An toàn (mở lại 7 ngày) = **4,25%** (51/1.200). Có 6 event có `trace_id` (lỗi ngầm sai mức tiền chưa đo được). | Xong, có bằng chứng | Kỹ sư phụ trách agent |
| 5 · Bảng lỗi và cách khắc phục | Chưa chốt đồng thuận 20 ca trên `main` (nhánh `haianh` đã có 20 nhãn Người gắn nhãn 1 + bảng 5 ca đại diện; Người gắn nhãn 2 đã gắn độc lập 20 ca, chờ ghép đối chiếu ≥ 80%). | Chưa | Người gắn nhãn 1 |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang` (loại `quoc_te`), chia ngẫu nhiên theo `staff` (50% đối chứng cùng thời gian), rollout `[0.10, 0.25, 0.50]`, 3 luật dừng 4 vế (`> 5,0%` mở lại 7 ngày; `> 12.000 đ` `simulated` hoặc xem lại `> 50%`; bỏ qua gợi ý `> 40%`), chốt `2026-12-16`. **Bất lợi:** `pilot_plan.yaml` hiện ghi **42 nv/nhóm** (3.100 yc/nhóm, MDE 0,05) vượt tổng 40 nhân viên hiện có. | Giả lập | Trưởng vận hành pilot |
| 7 · Rủi ro kinh tế | (1) Số ca làm lại ×2 → CPS **6.787 đ (+51,77%**, `simulated`); (2) Xem lại 100% phạm vi `noi_dia` + `hang_nang` → **12.962 đ (1,08×** mức 12.000 đ, `simulated`). | Giả lập | Trưởng vận hành pilot |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1 (Chỉnh cỡ mẫu pilot về khả thi với 40 nhân viên):** Sửa `report/team/pilot_plan.yaml` từ `42` nhân viên/nhóm (`3.100` yc/nhóm, MDE `0,05`) xuống `20` nhân viên/nhóm (`859` yc/nhóm, `DE = 6,96`, chấp nhận MDE `0,06` và ghi rõ power còn khoảng `0,64` nếu tác động thật `+5` điểm), đồng thời cân nhắc ngưỡng dừng an toàn so với đối chứng (mức hiện tại đã là `4,25%`, sát trần `5,0%`). **Người phụ trách:** Trưởng vận hành pilot · **Ngày kiểm tra:** `2026-11-28`.
- **Điều kiện 2 (Sửa lỗi tính toán B1/B3/A4/B4 để đạt sai số ≤ 2%):** Cập nhật `mo_hinh` trong `src/lab13.py` đặt `phut_xem_lai_simulated` và `phut_lam_lai_simulated` về `0` khi vượt `max_lan_chay`, kiểm tra lại mẫu số A4 (`1.200` yc) và tập ca `ok` ở B4 (`948` yc), rồi đồng bộ `report/team/bang_chi_phi.md` và `report/team/chi_so.md`. **Người phụ trách:** Người kiểm số · **Ngày kiểm tra:** `2026-11-26`.
- **Điều kiện 3 (Hoàn tất bảng lỗi và vá lỗi hệ thống nghiêm trọng):** Ghép 20 nhãn độc lập vào `report/team/bang_loi.md` (đạt đồng thuận ≥ 80%), bổ sung khoá chống trùng lệnh hoàn và đối soát API sổ cái trước khi báo đã hoàn (Ca 7, Ca 20). **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** `2026-11-28`.
- **Điều kiện 4 (Bật đủ event và giữ tỉ lệ xem lại < 50%):** Ghi đủ ≥ 6 event có `trace_id`, bổ sung đo phút xem lại/làm lại thực tế và event kiểm toán sai tiền hoàn; vì nếu phải xem lại 100%, chi phí đạt **12.962 đ** (`1,08×` mức 12.000 đ, `simulated`). **Người phụ trách:** Kỹ sư phụ trách agent · **Ngày kiểm tra:** `2026-12-02`.
