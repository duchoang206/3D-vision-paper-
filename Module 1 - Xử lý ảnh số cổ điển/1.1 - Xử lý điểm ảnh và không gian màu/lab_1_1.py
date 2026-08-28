import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, title):
    """Hàm phụ trợ vẽ histogram của ảnh xám"""
    plt.figure(figsize=(6, 4))
    plt.hist(image.ravel(), 256, [0, 256])
    plt.title(title)
    plt.xlabel('Cường độ sáng (Pixel value)')
    plt.ylabel('Số lượng pixel')
    plt.show()

def enhance_contrast():
    print("--- 1. Histogram Equalization (HE) & CLAHE ---")
    # Đọc ảnh xám (bạn cần thay thế 'sample_dark.jpg' bằng đường dẫn ảnh thực tế)
    # Ở đây tạo ảnh mẫu dạng gradient bị tối
    img = np.zeros((400, 400), dtype=np.uint8)
    for i in range(400):
        img[:, i] = int(min(255, i * 0.3)) # Ảnh rất tối
        
    # Thêm vật thể sáng hơn
    cv2.circle(img, (200, 200), 50, 100, -1)
    
    # 1. Histogram Equalization (HE)
    img_he = cv2.equalizeHist(img)
    
    # 2. CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img_clahe = clahe.apply(img)
    
    # Hiển thị
    cv2.imshow("Original Dark Image", img)
    cv2.imshow("HE Image", img_he)
    cv2.imshow("CLAHE Image", img_clahe)
    print("Bấm phím bất kỳ trên cửa sổ ảnh để tiếp tục...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def color_segmentation():
    print("--- 2. Tách vật thể bằng không gian màu HSV ---")
    # Tạo ảnh RGB mẫu với một quả bóng đỏ ở giữa
    img_color = np.ones((300, 300, 3), dtype=np.uint8) * 200  # Nền xám nhạt
    cv2.circle(img_color, (150, 150), 60, (0, 0, 255), -1)    # Quả bóng đỏ (OpenCV dùng BGR)
    
    # Chuyển đổi BGR sang HSV
    hsv_img = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
    
    # Xác định dải màu đỏ trong HSV
    # Màu đỏ có Hue nằm ở hai đầu của trục (0-10 và 170-180)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # Tạo mask (Mặt nạ)
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask = mask1 | mask2
    
    # Áp dụng mask lên ảnh gốc
    result = cv2.bitwise_and(img_color, img_color, mask=mask)
    
    # Hiển thị
    cv2.imshow("Original Image", img_color)
    cv2.imshow("Mask", mask)
    cv2.imshow("Extracted Red Object", result)
    print("Bấm phím bất kỳ trên cửa sổ ảnh để kết thúc...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Lab 1.1: Xử lý điểm ảnh và không gian màu")
    # Chạy các bài thực hành
    enhance_contrast()
    color_segmentation()
