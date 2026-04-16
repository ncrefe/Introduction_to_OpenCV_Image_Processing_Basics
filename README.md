# 📷 Sheet 00 — Introduction to OpenCV

This project demonstrates fundamental image processing operations using **OpenCV** and **NumPy** in Python. It covers essential concepts such as color space transformations, pixel manipulation, masking, and drawing operations.

The goal is to build a solid foundation for more advanced computer vision tasks by working directly with image data and understanding how different operations affect it.

---

## 🚀 Features

* 📥 Load and display images
* 🎨 Convert images to HSV color space and analyze channels
* 🔆 Adjust image brightness (loop-based and vectorized approaches)
* ⚡ Compare performance between implementations
* 🧩 Extract and manipulate image patches
* 🎭 Apply masking using thresholding
* 🖌️ Draw shapes and overlay text on images
* 🖼️ Add borders to images

---

## 🛠️ Tech Stack

* Python 3.12
* OpenCV 4.11
* NumPy 2.3.3

> ⚠️ The project is designed to run in a Linux environment.

---

## 📂 Project Structure

```
.
├── bonn.jpeg
├── main.py
├── README.md
```

---

## ⚙️ Installation

```
pip install opencv-python numpy
```

---

## ▶️ Usage

```
python main.py
```

The program will:

* Display intermediate image processing results
* Print image properties (dimensions, data type)
* Show comparisons between different implementations

---

## 🧪 Implemented Tasks

### 1. Image Loading & Inspection

* Load an image using OpenCV
* Display it
* Print image dimensions and data type

### 2. Color Space Conversion

* Convert image from BGR to HSV
* Display individual channels (H, S, V)

### 3. Brightness Adjustment (Loop-Based)

* Increase brightness by adding 50 to each pixel
* Clip values to [0, 255]
* Implemented using nested loops

### 4. Brightness Adjustment (Vectorized)

* Same operation using NumPy (single line)
* Compare execution time with loop-based approach

### 5. Patch Extraction & Placement

* Extract a 32×32 patch from the top-left corner
* Paste it into three random positions in the image

### 6. Masking with Threshold

* Convert image to grayscale
* Apply binary threshold at 128
* Use mask to display only bright regions

### 7. Drawing & Annotation

* Add a 20-pixel border to the image
* Draw 5 random circles and 5 random text labels

---

## 📌 Notes

* Only specified libraries are used
* The implementation focuses on clarity and understanding
* This project serves as a foundation for computer vision tasks
