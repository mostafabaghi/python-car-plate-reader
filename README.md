# 🚗 License Plate Text Extractor

This Python project uses OpenCV and Tesseract OCR to detect and extract license plate text from car images — optimized for **French license plates**.

## 📸 Example Use Case

You place images of vehicles inside a `cars/` folder, and the script will process each image to locate the license plate and extract its text.

## 🔧 Features

- Automatic detection of license plates using image processing
- Optical Character Recognition (OCR) with `pytesseract`
- Optimized for French plate formats (e.g. `AB-123-CD`)
- Preprocessing pipeline for better OCR accuracy
- CLI output of image paths and detected plate text

---

## 🧰 Requirements

- Python 3.6+
- OpenCV
- pytesseract
- Tesseract OCR engine installed on your system

### Install dependencies

```bash
pip install opencv-python pytesseract numpy
```

### Install Tesseract (OCR Engine)

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install tesseract-ocr
```

#### macOS (using Homebrew):
```bash
brew install tesseract
```

#### Windows:
- Download the installer from: https://github.com/tesseract-ocr/tesseract
- Make sure to add the Tesseract installation path to your system’s PATH.
- Example: `C:\Program Files\Tesseract-OCR\tesseract.exe`

If needed, you can specify the Tesseract executable path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📁 Folder Structure

```
project/
│
├── cars/                 # Input images of vehicles
├── main.py               # Main script for processing
├── README.md             # This file
```

---

## ▶️ How to Run

```bash
python main.py
```

The script will print the detected license plate text for each image in the `cars/` directory.

---

## 🔍 How It Works

1. Converts the image to grayscale and enhances contrast.
2. Uses edge detection and contour finding to locate license plate candidates.
3. Filters candidates based on aspect ratio (French plates ~4:1).
4. Extracts the plate region and applies thresholding.
5. Uses `pytesseract` to perform OCR on the region.
6. Prints the extracted text if it resembles a valid French plate.

---

## ✨ Sample Output

```
🔍 Reading French car plates from images in 'cars/' folder...

📷 cars/car1.jpg ➤ 🏷️ Plate: AB-123-CD
📷 cars/car2.jpg ➤ 🏷️ Plate: ZY-987-WX
```

---

## 📌 License Plate Format Supported

This script is optimized for **French license plates**, typically formatted like:

- `AB-123-CD`
- `1234 AB 75`

For other country formats, some logic may need to be adjusted.

---

## 🛠️ Future Improvements

- Support for other countries (e.g. Iran, Germany)
- GUI for drag-and-drop detection
- Model-based plate detection with YOLO or other deep learning methods
- Integration with Flask for web interface

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🤝 Contributions

Feel free to fork, improve, or submit a pull request! 🚀