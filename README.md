# Vision Sandbox

This repository contains a collection of **Computer Vision projects** developed as part of coursework and experimentation. The projects combine **traditional computer vision techniques** with **modern deep learning approaches** to solve tasks such as **image retrieval, object recognition, and feature-based analysis**.

Each project is organized as a **submodule** and can be built and executed independently.

---

# Projects Included

## 1. Content-Based Image Retrieval (CBIR)

A system that retrieves **visually similar images** using a combination of:

- Deep learning embeddings (ResNet)
- Color histograms
- Texture descriptors
- Gradient-based features

The system allows users to **adjust feature weights interactively through a GUI** to control the importance of **color, texture, and semantic similarity**.

**Key techniques**

- ResNet feature embeddings
- RGB / rg color histograms
- Gradient-based texture features
- Laws texture filters
- Cosine similarity and histogram intersection metrics

---

## 2. Object Recognition System

An interactive object recognition pipeline that supports both:

- **Handcrafted geometric features**
- **Deep learning embeddings using ResNet**

The system supports **training and inference modes**, allowing users to build a database of labeled objects and recognize them in images or video streams.

**Key techniques**

- Image thresholding and segmentation
- Connected component analysis
- Moment-based feature extraction
- Hu moments
- ResNet-18 embeddings
- Nearest neighbor classification

---

## 3. Image Feature Analysis / Hybrid Feature Systems

This project explores **combining handcrafted features with deep learning features** to improve robustness across different visual recognition tasks.

The focus is on understanding how:

- Classical computer vision
- Feature engineering
- Deep neural embeddings

can complement each other for better image understanding.

---

Each submodule contains its own:

- documentation
- build instructions
- usage examples

---

# Technologies Used

- **C++17**
- **Python**
- **OpenCV**
- **NumPy**
- **Pillow**
- **ResNet (ONNX / PyTorch models)**
- **CMake**

---

# Key Concepts Covered

These projects explore several important **computer vision concepts**:

- Image feature extraction
- Deep neural embeddings
- Texture analysis
- Color histogram indexing
- Object segmentation
- Moment-based descriptors
- Nearest neighbor search
- Similarity metrics


