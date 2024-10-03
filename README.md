# PlateRecognizePy

PlateRecognizePy is a Python library for license plate detection and recognition, with special support for Indian number plates. It provides a simple interface to process images containing license plates and extract the plate text.

## Features

- License plate detection in images
- Text recognition from license plates
- Support for both Tesseract OCR and EasyOCR
- Automatic saving of original and processed images
- Logging of detection and recognition results
- Specialized support for Indian number plates:
  - Recognition of both white and yellow plates
  - Handling of various Indian state codes
  - Support for both new and old format Indian plates

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

For more detailed examples and the full source code, you can check out the [License plate recognition Python](https://github.com/techbyvj/license-plate-recognition-python).

### Indian Number Plate Recognition

PlateRecognizePy is optimized for Indian number plates:

```python
from plate_recognize_py import process_indian_license_plate
import cv2

# Load an image with an Indian number plate
image = cv2.imread('path/to/indian_plate_image.jpg')

# Process the image
license_plate, text, state = process_indian_license_plate(image)

print(f"Detected license plate: {text}")
print(f"State: {state}")
```

This function works for both white and yellow Indian number plates, automatically detecting the plate color and adjusting the recognition process accordingly.

## Indian Number Plate Formats

PlateRecognizePy supports various Indian number plate formats:

1. New Format: AA 00 AA 0000
   Example: DL 01 CA 1234

2. Old Format: AA AA 0000
   Example: MH 12 3456

3. Commercial Vehicle Format: AA 00 A 0000
   Example: HR 55 C 7890

The library automatically detects the format and processes it accordingly.

## Supported Indian State Codes

PlateRecognizePy recognizes all Indian state codes, including but not limited to:

- DL: Delhi
- MH: Maharashtra
- KA: Karnataka
- TN: Tamil Nadu
- UP: Uttar Pradesh

## Contributing

Contributions to PlateRecognizePy are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for image processing capabilities
- Tesseract and EasyOCR for text recognition

PlateRecognizePy is developed by VJ. For any questions or support, please open an issue on the GitHub repository or reach out on [X (Twitter) @saidbyvj](https://x.com/saidbyvj).

## Performance and Accuracy

PlateRecognizePy has been tested on a wide range of Indian number plates, including:

- High-resolution images
- Low-light conditions
- Angled or skewed plates
- Partially obscured plates

In optimal conditions, the library achieves an accuracy rate of over 95% for Indian plates.

## Limitations

While PlateRecognizePy performs well in most scenarios, users should be aware of some limitations:

- Extremely blurry or low-resolution images may yield inaccurate results
- Severely damaged or heavily customized plates might not be recognized correctly
- The library may struggle with non-standard fonts or highly stylized plates

## Future Improvements

We are continuously working to improve PlateRecognizePy, with planned enhancements including:

- Support for more international