import cv2
import pytesseract
import os
import numpy as np

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    return filtered

def extract_plate_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None, "Could not load image"

    filtered = preprocess_image(image)

    edged = cv2.Canny(filtered, 30, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    plate_text = "Plate not detected"
    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[:20]:
        approx = cv2.approxPolyDP(contour, 0.018 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)

            aspect_ratio = w / float(h)
            if 3 < aspect_ratio < 5:
                plate_img = filtered[y:y+h, x:x+w]

                _, thresh = cv2.threshold(plate_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

                text = pytesseract.image_to_string(thresh, config=custom_config)
                text = text.strip().replace(" ", "").replace("\n", "")

                if 6 <= len(text) <= 10:
                    plate_text = text
                    break

    return image_path, plate_text

folder_path = "cars"

print("🔍 Reading Iranian car plates from images in 'cars/' folder...\n")

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(folder_path, filename)
        file, plate = extract_plate_text(img_path)
        print(f"📷 {file} ➤ 🏷️ Plate: {plate}")