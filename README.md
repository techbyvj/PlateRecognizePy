# PlateRecognizePy

PlateRecognizePy is a Python library for license plate detection and recognition. It provides a simple interface to process images containing license plates and extract the plate text.

## Features

- License plate detection in images
- Text recognition from license plates
- Support for both Tesseract OCR and EasyOCR
- Automatic saving of original and processed images
- Logging of detection and recognition results

## Installation

You can install PlateRecognizePy using pip:

```
pip install PlateRecognizePy
```

## Requirements

PlateRecognizePy requires Python 3.7 or later. The main dependencies are:

- [pytesseract](https://pypi.org/project/pytesseract/)
- [easyocr](https://pypi.org/project/easyocr/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)

For a complete list of dependencies, please refer to the `setup.py` file.

## Usage

Here's a simple example of how to use PlateRecognizePy:

```python
from plate_recognize_py import process_license_plate
import cv2

# Load an image
image = cv2.imread('path/to/your/image.jpg')

# Process the image
license_plate, text = process_license_plate(image)

print(f"Detected license plate: {text}")
```

## Contributing

Contributions to PlateRecognizePy are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for image processing capabilities
- Tesseract and EasyOCR for text recognition

PlateRecognizePy is developed by VJ. For any questions or support, please open an issue on the GitHub repository.