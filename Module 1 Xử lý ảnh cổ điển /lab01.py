import numpy as np

def convolve2d(image, kernel):
    # Lấy kích thước ảnh và kernel
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape
    
    # Tính khoảng đệm (padding) để không bị lỗi ở viền ảnh
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    # Thêm viền số 0 quanh ảnh (Zero Padding)
    padded_img = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    
    # Tạo mảng rỗng để chứa ảnh kết quả
    output = np.zeros_like(image, dtype=np.float32)
    
    # Trượt kernel qua từng pixel của ảnh
    for i in range(img_h):
        for j in range(img_w):
            # Cắt lấy vùng ảnh cục bộ kích thước 3x3 quanh pixel (i, j)
            region = padded_img[i : i + k_h, j : j + k_w]
            
            # Nhân từng phần tử rồi tính tổng (tích vô hướng ma trận)
            output[i, j] = np.sum(region * kernel)
            
    return np.clip(output, 0, 255).astype(np.uint8)

# Thử nghiệm với vùng ảnh ví dụ
image = np.array([
    [10,  10,  10],
    [10, 255,  10],
    [10,  10,  10]
], dtype=np.uint8)

# Định nghĩa Gaussian Kernel 3x3
gaussian_kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32) / 16.0

result = convolve2d(image, gaussian_kernel)
print("Pixel ở giữa sau khi lọc:", result[1, 1])  # Kết quả: 71