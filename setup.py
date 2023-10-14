from setuptools import find_packages, setup

setup(
    name="DocsInARow",
    version="0.1",
    description="A script for processing images and extracting, correcting, and categorizing text from them",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Scott White",
    author_email="stolidwisdom@gmail.com",
    url="https://github.com/ScottStevenWhite/DocsInARow",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "openai",
        "Pillow",
        "pytesseract",
        "python-dotenv",
        "google-cloud-core",
        "google-cloud-vision",
        "google-cloud-documentai",
        "piexif",
        "pyinstaller",
        "scikit-learn",
        "opencv-python",
    ],
)