# 🦺 Automated PPE Detection System

An AI-powered desktop application for detecting Personal Protective Equipment (PPE), including safety helmets and safety vests, using the YOLO11 object detection model.

## 📖 Overview

The Automated PPE Detection System is designed to improve workplace safety by automatically detecting Personal Protective Equipment (PPE) in images, folders, videos, and live webcam streams. The application provides a simple desktop interface for performing detections, managing detection history, and configuring application settings.

## ✨ Features

- Image Detection
- Folder Detection
- Video Detection
- Live Webcam Detection
- Gallery Module
- Image Viewer
- Detection History
- Search and Delete Detection Records
- Settings Management
- SQLite Database Integration

## 🛠️ Technologies Used

- Python
- YOLO11 (Ultralytics)
- OpenCV
- Tkinter
- Pillow
- SQLite

## 📁 Project Structure

```
Automated-PPE-Detection-System/
│
├── app.py
├── config.py
├── requirements.txt
├── controllers/
├── database/
├── views/
├── utils/
├── config/
├── model/
└── output/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Kartikdogra5911/Automated-PPE-Detection-System.git
```

Move into the project directory:

```bash
cd Automated-PPE-Detection-System
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## 📋 Modules

- Home Dashboard
- Image Detection
- Folder Detection
- Gallery Module
- Image Viewer
- Video Detection
- Live Webcam Detection
- Detection History
- Settings Module

## 💾 Database

The application uses SQLite to store:

- Detection Type
- File Name
- Helmet Count
- Vest Count
- Processing Time
- Detection Date

## 🚀 Future Improvements

- Detection of additional PPE (Gloves, Goggles, Safety Shoes)
- CCTV Camera Integration
- Cloud Database Support
- Mobile Application
- Web Dashboard
- Real-Time Notifications
- Face Recognition Integration

## 👨‍💻 Author

**Kartik Dogra**

B.Tech – Artificial Intelligence and Data Science

Chandigarh Engineering College, Jhanjeri

GitHub: https://github.com/Kartikdogra5911

## 📄 License

This project is developed for educational and academic purposes.