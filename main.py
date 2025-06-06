import cv2
import pytesseract
import os

def extract_plate_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None, "Could not load image"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(filtered, 30, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    plate_text = "Plate not detected"
    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[:10]:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            plate_img = gray[y:y+h, x:x+w]
            text = pytesseract.image_to_string(plate_img, config='--psm 8')
            if len(text.strip()) > 4:
                plate_text = text.strip()
                break

    return image_path, plate_text

# Folder path
folder_path = "cars"

print("🔍 Reading car plates from images in 'cars/' folder...\n")

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(folder_path, filename)
        file, plate = extract_plate_text(img_path)
        print(f"📷 {file} ➤ 🏷️ Plate: {plate}")