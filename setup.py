from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PlateRecognizePy",
    version="0.1.1",
    author="VJ",
    author_email="",
    description="A Python library for license plate detection and recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techbyvj/PlateRecognizePy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pytesseract",
        "easyocr",
        "opencv-python",
        "numpy",
    ],
)
