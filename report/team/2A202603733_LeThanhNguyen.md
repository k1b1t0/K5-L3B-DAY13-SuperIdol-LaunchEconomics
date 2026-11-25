# Báo cáo cá nhân — LeThanhNguyen-2A202603733

## 1. Thông tin thành viên

- Họ tên: Lê Thành Nguyên
- MSSV: 2A202603733
- Email: nguyenngungonvc@gmail.com
- GitHub: NguyenLTpk
- Vai trong nhóm: Người gắn nhãn 2 & Giữ hồ sơ

## 2. Phần việc phụ trách

- Điền thông tin nhóm, bảng 4 thành viên và cập nhật phần đóng góp vào `TEAM.md`.
- Giữ và hoàn thiện trang hồ sơ tổng hợp `report/team/ho_so_launch_v0.md` (7 mục và chốt đề xuất Gate 2a).
- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, gắn nhãn độc lập theo 5 loại Google PAIR và gửi bộ nhãn cho Người gắn nhãn 1 nhập vào `report/team/bang_loi.md`.
- Hợp nhất các nhánh về `main` và chạy kiểm tra tuân thủ cuối buổi (quét từ cấm trong `report/team/`, chạy lại `src/lab13.py`, kiểm tra YAML và dấu `?` trong `report/team/pilot_plan.yaml`, kiểm tra danh sách file nộp theo `SUBMISSION.md`).

## 3. Đóng góp cụ thể

- Cập nhật thông tin nhóm (`URL repo`, `nhánh nộp`), điền đủ 4 thành viên và tổng hợp đóng góp trong `TEAM.md`.
- Đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gửi bộ 20 nhãn độc lập (4 `Do người dùng`, 5 `Hệ thống`, 4 `Ngữ cảnh`, 4 `Giới hạn hệ thống`, 3 `Ngầm`) cho Người gắn nhãn 1 đối chiếu vào `report/team/bang_loi.md`, đạt đồng thuận `20/20 = 100%`.
- Hợp nhất các nhánh vào `main` và phối hợp chuẩn hoá lại các phần còn sai lệch kỹ thuật theo rà soát chéo: sửa `max_lan_chay`, A4, B4, D1 trong `src/lab13.py`, đồng bộ `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/group_report.md` và chỉnh `report/team/pilot_plan.yaml` về phương án khả thi `20` nhân viên/nhóm (`n = 859`, `DE = 6,96`, `m >= 299`, MDE `0,06`).
- Hoàn thiện 7 mục của `report/team/ho_so_launch_v0.md`: gắn nhãn `simulated` và trạng thái `Giả lập`/`Xong, có bằng chứng` đầy đủ, nêu rõ con số bất lợi (power còn `0,64` ở mức 5 điểm; xem lại 100% tốn `11.743–12.415 đ`; loại `quoc_te` tốn `22.515 đ`) và chốt đề xuất **Go có điều kiện** kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra.
- Chạy kiểm tra tuân thủ cuối buổi: không dùng từ cấm trong `report/team/`, không còn dấu `?` ngoài chú thích trong `report/team/pilot_plan.yaml`, `yaml.safe_load` đọc hợp lệ, `src/lab13.py` chạy hết và A1 đạt cả 3 phép thử, file gốc không bị thay đổi.

## 4. Bằng chứng

- Branch `lethanhnguyen` (`d7de5bc`) và nhánh nộp `main`: `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603733_LeThanhNguyen.md` cùng các bản đồng bộ `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/group_report.md`.
- Bộ 20 nhãn độc lập đã ghép vào `report/team/bang_loi.md` với đồng thuận `20/20 = 100%`.
- Kiểm tra cuối buổi trên `main`: `src/lab13.py` chạy thông suốt (`Ba phép thử đáp án biết trước: ĐẠT`), `yaml.safe_load` thành công trên `report/team/pilot_plan.yaml`, quét từ cấm trả về rỗng.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để rà soát yêu cầu từ `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`, phân loại độc lập 20 ca lỗi theo Google PAIR, hỗ trợ chuẩn hoá lại công thức A4/B1/B3/B4/D1 và tổng hợp hồ sơ `report/team/ho_so_launch_v0.md`.
- Tự kiểm tra lại bằng cách chạy trực tiếp `python -B lab13.py` trong `src/`, đọc kiểm tra `report/team/pilot_plan.yaml` bằng `yaml.safe_load`, đối chiếu từng con số với hướng dẫn buổi chiều và `bang_chi_phi.md`/`chi_so.md`, đồng thời quét từ cấm và kiểm tra `git diff` trước khi push lên `main`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc của Người gắn nhãn 2 & Giữ hồ sơ và hợp nhất hoàn chỉnh bài nhóm lên nhánh `main` (giữ nguyên các nhánh thành viên, không tự bịa nội dung cho `report/team/phieu_cham.md` vì chưa có hồ sơ/phản hồi của nhóm hội đồng theo đúng `RULES.md`).
