# Báo cáo cá nhân — LeThanhNguyen-2A202603733

## 1. Thông tin thành viên

- Họ tên: Lê Thành Nguyên
- MSSV: 2A202603733
- Email: nguyenngungonvc@gmail.com
- GitHub: NguyenLTpk
- Vai trong nhóm: Người gắn nhãn 2 & Giữ hồ sơ

## 2. Phần việc phụ trách

- Điền thông tin nhóm, bảng 4 thành viên và cập nhật phần đóng góp vào `TEAM.md`.
- Giữ và hoàn thiện trang hồ sơ tổng hợp `report/team/ho_so_launch_v0.md` (7 mục và chốt đề xuất Gate 2a trước 17:00).
- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, gắn nhãn độc lập theo 5 loại Google PAIR và gửi bộ nhãn cho Người gắn nhãn 1 nhập vào `report/team/bang_loi.md`.
- Chạy kiểm tra tuân thủ cuối buổi (quét từ cấm trong `report/team/`, chạy lại `src/lab13.py`, kiểm tra YAML và dấu `?` trong `report/team/pilot_plan.yaml`, kiểm tra danh sách file nộp theo `SUBMISSION.md`).

## 3. Đóng góp cụ thể

- Cập nhật thông tin nhóm (`URL repo`, `nhánh nộp`), điền đủ 4 thành viên (gồm cả thành viên 3 từ nhánh `haianh`) và cập nhật phần đóng góp trong `TEAM.md`.
- Đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và hoàn thành bộ 20 nhãn độc lập theo nguyên nhân gốc (4 `Do người dùng`, 5 `Hệ thống`, 4 `Ngữ cảnh`, 4 `Giới hạn hệ thống`, 3 `Ngầm`) để gửi Người gắn nhãn 1 đối chiếu đồng thuận trong `report/team/bang_loi.md` (không sửa đè lên file thuộc quyền sở hữu của Người gắn nhãn 1 trên nhánh `haianh`).
- Hoàn thiện 7 mục của `report/team/ho_so_launch_v0.md` từ số liệu của `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md` và `report/team/pilot_plan.yaml`:
  - Gắn nhãn `simulated` và trạng thái `Giả lập` đầy đủ cho mọi con số từ cột `_simulated`; ghi trạng thái `Chưa` cho mục 5 đang chờ ghép đồng thuận bảng lỗi.
  - Đưa đầy đủ con số bất lợi vào hồ sơ (xem lại 100% tốn `12.962 đ = 1,08×` mức 12.000 đ `simulated`, `quoc_te` tốn `22.515 đ`, thiết kế `42 nv/nhóm` vượt tổng 40 nhân viên, sai lệch code `max_lan_chay`/A4/B4) và chốt đề xuất **Go có điều kiện** với 4 điều kiện kèm vai trò phụ trách và ngày kiểm tra cụ thể.
- Chạy rà soát tuân thủ quy tắc nộp bài: không dùng từ cấm trong `report/team/`, không còn dấu `?` ngoài chú thích trong `report/team/pilot_plan.yaml`, `yaml.safe_load` đọc hợp lệ, `src/lab13.py` chạy hết và A1 đạt cả 3 phép thử, các file gốc không bị thay đổi và không có thư mục nháp trong git.

## 4. Bằng chứng

- Branch `lethanhnguyen`: cập nhật `TEAM.md`, hoàn thiện `report/team/ho_so_launch_v0.md` và tạo `report/team/2A202603733_LeThanhNguyen.md`.
- Bộ 20 nhãn độc lập (Ca 1–20) bàn giao cho Người gắn nhãn 1 ghép và tính đồng thuận trong `report/team/bang_loi.md`.
- Kết quả tự kiểm tra trên nhánh `lethanhnguyen`: `src/lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`, `yaml.safe_load` thành công trên `report/team/pilot_plan.yaml`, kiểm tra không chứa từ cấm hay dấu `?` ngoài chú thích.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để rà soát yêu cầu từ `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`, phân loại độc lập 20 ca lỗi theo khung nguyên nhân gốc của Google PAIR, tổng hợp 7 mục vào `report/team/ho_so_launch_v0.md` và phát hiện các sai lệch cần gắn vào điều kiện Gate 2a.
- Tự kiểm tra lại bằng cách chạy trực tiếp `python -B lab13.py` trong `src/`, đọc kiểm tra `report/team/pilot_plan.yaml` bằng `yaml.safe_load`, đối chiếu từng con số với `report/team/bang_chi_phi.md` và `report/team/chi_so.md`, đồng thời quét từ cấm và kiểm tra `git diff` trước khi commit.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc sở hữu cá nhân của Người gắn nhãn 2 & Giữ hồ sơ trên nhánh riêng `lethanhnguyen` đúng quy định phân quyền file, đảm bảo tính trung thực của số liệu và điều kiện Gate 2a.
- Sau khi ghép nhánh `haianh` (hoàn tất đồng thuận `bang_loi.md` và `phieu_cham.md` sau phiên duyệt chéo 17:00) và xử lý các sửa đổi ở `src/lab13.py`/`pilot_plan.yaml`, cần cập nhật lại mục 5–6 trong `ho_so_launch_v0.md` và commit chốt `TEAM.md` trên `main` trước khi nộp LMS.
