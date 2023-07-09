import cv2
import numpy as np

def apply_image_stretching(image):
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Lakukan image stretching
    min_val = np.min(gray)
    max_val = np.max(gray)
    stretched = (gray - min_val) * (255 / (max_val - min_val))
    
    # Konversi kembali ke format BGR
    return cv2.cvtColor(stretched.astype(np.uint8), cv2.COLOR_GRAY2BGR)

def calculate_mse(image1, image2):
    mse = np.mean((image1 - image2) ** 2)
    return mse

def calculate_psnr(mse, max_value=255):
    if mse == 0:
        return float('inf')
    psnr = 20 * np.log10(max_value / np.sqrt(mse))
    return psnr

# Baca gambar
image = cv2.imread('gambar1.jpg')

# Terapkan Image Stretching pada gambar
stretched_image = apply_image_stretching(image)

# Hitung MSE antara gambar asli dan hasil perbaikan
mse = calculate_mse(image, stretched_image)

# Hitung PSNR berdasarkan MSE
psnr = calculate_psnr(mse)

# Tampilkan nilai MSE dan PSNR
print("MSE:", mse)
print("PSNR:", psnr)

# Tampilkan gambar asli dan hasil perbaikan
cv2.imshow('Original Image', image)
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()