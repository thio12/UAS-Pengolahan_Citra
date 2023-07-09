import cv2
import numpy as np

def apply_median_filter(image):
    # Terapkan Median Filter pada gambar
    return cv2.medianBlur(image, 9)

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

# Terapkan Median Filter pada gambar
filtered_image = apply_median_filter(image)

# Hitung MSE antara gambar asli dan hasil filter
mse = calculate_mse(image, filtered_image)

# Hitung PSNR berdasarkan MSE
psnr = calculate_psnr(mse)

# Tampilkan nilai MSE dan PSNR
print("MSE:", mse)
print("PSNR:", psnr)

# Tampilkan gambar asli dan hasil filter
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()