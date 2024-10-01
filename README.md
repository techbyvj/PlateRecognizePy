# License Plate Recognition (LPR)

LPR is a Python library for license plate detection and recognition. It provides a simple interface to process images containing license plates and extract the plate text.

## Features

- License plate detection in images
- Text recognition from license plates
- Support for both Tesseract OCR and EasyOCR
- Automatic saving of original and processed images
- Logging of detection and recognition results

## Installation

You can install LPR using pip:

```
pip install lpr
```

## Requirements

LPR requires Python 3.7 or later. The main dependencies are:

- [pytesseract](https://pypi.org/project/pytesseract/)
- [easyocr](https://pypi.org/project/easyocr/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)

For a complete list of dependencies, please refer to the `setup.py` file.

## Usage

Here's a simple example of how to use LPR:

```python
from lpr import process_license_plate
import cv2

# Load an image
image = cv2.imread('path/to/your/image.jpg')

# Process the image
license_plate, text = process_license_plate(image)

if license_plate is not None:
    print(f"Detected license plate text: {text}")
else:
    print("No license plate detected")
```

## Output

The `process_license_plate` function returns two values:

1. The cropped image of the detected license plate (or None if no plate was detected)
2. The recognized text from the license plate (or "unknown" if no text was recognized)

Additionally, the function saves the following files in an `output` directory:

- The original input image
- The cropped license plate image (if detected)

The output directory is organized by date, and the filenames include timestamps and recognized text (when available).

## Logging

LPR uses Python's built-in logging module to provide information about the detection and recognition process. You can configure the logging level and format as needed in your application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

LPR is developed by VJ. For any questions or support, please open an issue on the GitHub repository.
