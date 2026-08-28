# 1.1 - Xử lý điểm ảnh và không gian màu

Trong bài học này, chúng ta sẽ tìm hiểu về cách máy tính lưu trữ và biểu diễn hình ảnh, cũng như các kỹ thuật cơ bản nhất để thao tác với điểm ảnh (pixel) và thay đổi không gian màu.

## 1. Biểu diễn ảnh dưới dạng ma trận
Mỗi bức ảnh kỹ thuật số thực chất là một ma trận (hoặc mảng đa chiều) chứa các con số.
- **Kích thước (Resolution):** Được xác định bởi chiều rộng (Width) và chiều cao (Height). Ví dụ ảnh 1920x1080 có nghĩa là ma trận có 1080 hàng và 1920 cột.
- **Số kênh (Channels):** 
  - Ảnh xám (Grayscale): Có 1 kênh màu. Mỗi giá trị đại diện cho độ sáng từ tối đến sáng.
  - Ảnh màu (RGB): Có 3 kênh màu tương ứng với Đỏ (Red), Lục (Green) và Lam (Blue).
- **Bit depth (Độ sâu bit):** 
  - **8-bit:** Giá trị mỗi điểm ảnh nằm trong khoảng từ `0` đến `255` (đây là định dạng phổ biến nhất `uint8`).
  - **16-bit:** Giá trị điểm ảnh từ `0` đến `65535`, thường dùng trong ảnh y tế hoặc ảnh chụp RAW chuyên nghiệp.
  - **Float (32-bit):** Giá trị điểm ảnh từ `0.0` đến `1.0`, thường được dùng khi đưa ảnh vào huấn luyện các mô hình học sâu (Deep Learning).
- **Lượng tử hóa (Quantization) và Clipping:** Khi thực hiện tính toán trên điểm ảnh, nếu giá trị vượt quá giới hạn (ví dụ > 255), ta thường sử dụng kỹ thuật `clipping` (cắt xén) để ép giá trị về lại khoảng cho phép (0-255).

## 2. Các không gian màu phổ biến
Mặc dù RGB là không gian màu hiển thị tiêu chuẩn trên màn hình, nhưng nó không phải lúc nào cũng tối ưu cho việc xử lý ảnh vì ba kênh R, G, B mang các thông tin tương quan với nhau và đều bị ảnh hưởng bởi độ sáng. Do đó ta thường chuyển đổi sang:
- **Grayscale:** Lấy trung bình có trọng số của R, G, B để tạo ra một kênh độ sáng duy nhất.
- **HSV (Hue, Saturation, Value):** 
  - **H (Hue):** Giá trị màu (từ đỏ, vàng, lục, lam...). Rất phù hợp để tách vật thể dựa trên màu sắc.
  - **S (Saturation):** Độ bão hòa màu (nhạt hay đậm).
  - **V (Value):** Độ sáng. 
  - *Ứng dụng:* HSV đặc biệt hiệu quả để phân đoạn tách nền vật thể có màu sắc cụ thể mà không bị ảnh hưởng nhiều bởi ánh sáng môi trường.
- **LAB (CIELAB):**
  - **L (Lightness):** Kênh độ sáng.
  - **a & b:** Các kênh màu (a: lục - đỏ, b: lam - vàng).
  - *Ứng dụng:* Dùng LAB để tách biệt hoàn toàn thông tin ánh sáng ra khỏi thông tin màu sắc, giúp xử lý độ tương phản hoặc cân bằng trắng dễ dàng hơn.

## 3. Histogram và Cân bằng độ tương phản
- **Histogram (Biểu đồ tần suất):** Là biểu đồ thể hiện sự phân bố các giá trị điểm ảnh trong một bức ảnh (từ mức 0 đến 255).
- **Histogram Equalization (HE):** Phương pháp dàn đều tần suất điểm ảnh trên toàn bộ thang độ sáng, giúp tăng độ tương phản tổng thể. Tuy nhiên, phương pháp này dễ làm nhiễu vùng tối trở nên rõ rệt hơn hoặc làm lóa vùng sáng.
- **CLAHE (Contrast Limited Adaptive Histogram Equalization):** Khắc phục nhược điểm của HE bằng cách chia nhỏ ảnh thành các khối (tiles) rồi thực hiện cân bằng cục bộ. Đồng thời giới hạn (clip limit) việc tăng độ tương phản quá mức. CLAHE cực kỳ hiệu quả đối với ảnh chụp thiếu sáng hoặc ánh sáng không đồng đều.

## 4. Phân ngưỡng (Thresholding)
Phân ngưỡng là kỹ thuật đưa ảnh về dạng nhị phân (chỉ gồm pixel đen và trắng) để làm nổi bật đối tượng khỏi nền.
- **Binary Thresholding:** Nếu điểm ảnh lớn hơn một ngưỡng cố định T, gán bằng 255 (trắng), ngược lại gán bằng 0 (đen).
- **Adaptive Thresholding:** Thay vì dùng một ngưỡng chung, thuật toán sẽ tính toán ngưỡng cục bộ cho từng vùng nhỏ trên ảnh. Giúp xử lý tốt các ảnh có độ sáng thay đổi không đều.
- **Otsu's Binarization:** Thuật toán tự động tìm ra ngưỡng tối ưu nhất bằng cách tối đa hóa phương sai giữa hai lớp (nền và vật thể) dựa trên biểu đồ Histogram, thay vì phải chọn ngưỡng thủ công.

---
## Bài tập thực hành đề xuất
Tạo file `lab_1_1.py` để:
1. Đọc một bức ảnh bị thiếu sáng hoặc ánh sáng không đều.
2. Vẽ Histogram của ảnh.
3. So sánh kết quả tăng độ tương phản bằng HE và CLAHE.
4. Chuyển ảnh sang không gian màu HSV và thử trích xuất một vật thể theo màu sắc (ví dụ: quả bóng màu đỏ).
