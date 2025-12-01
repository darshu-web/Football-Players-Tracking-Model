⚽ Football Analysis System using YOLOv8, Computer Vision & Deep Learning

This project demonstrates how to build an intelligent Football Analysis System by combining computer vision and deep learning techniques. It uses YOLOv8 for detection, KMeans for team classification, Optical Flow for understanding camera motion, and Perspective Transformation for converting pixel movement into real-world metrics.

The system detects players, footballs, referees, tracks them across video frames, classifies team colors, and computes player speed & distance covered in meters.


🚀 Features

✅ Detect players, referees, and football using YOLOv8

✅ Fine-tune YOLOv8 on a custom football dataset

✅ Team classification using KMeans color clustering

✅ Optical Flow for estimating camera movement

✅ Perspective Transformation to convert pixel data → meters

✅ Player tracking and real-world analysis:

🏃 Speed estimation

📏 Distance covered


📂 Project Structure
football-analysis/
│-- data/                     # Dataset & annotations
│-- models/                   # YOLO weights & trained models
│-- src/
│   ├── detection.py          # YOLOv8 detection script
│   ├── tracking.py           # Object tracking logic
│   ├── team_clustering.py    # KMeans clustering for t-shirt colors
│   ├── optical_flow.py       # Camera movement estimation
│   ├── perspective.py        # Perspective transformation calculations
│   ├── analysis.py           # Player speed & distance calculation
│   └── utils.py              # Helper functions
│-- notebooks/                # Jupyter notebooks for experiments
│-- requirements.txt          # Dependencies
│-- README.md                 # Project documentation


🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/football-analysis.git
cd football-analysis

2. Install dependencies
pip install -r requirements.txt

3. Install YOLOv8
pip install ultralytics


📊 Usage
1. Run Object Detection
python src/detection.py --source data/match.mp4 --weights models/yolov8_custom.pt

2. Train YOLOv8 on Custom Dataset
yolo detect train data=data/dataset.yaml model=yolov8n.pt epochs=50 imgsz=640

3. Assign Teams using KMeans
python src/team_clustering.py --input outputs/detections/

4. Optical Flow for Camera Movement
python src/optical_flow.py --input data/match.mp4

5. Perspective Transform & Speed Calculation
python src/analysis.py --input outputs/tracked/


📦 Requirements

Python 3.8+

Ultralytics YOLOv8

OpenCV

NumPy

scikit-learn

Matplotlib

Install all using:

pip install -r requirements.txt


📹 Demo

👉 Add your demo video or screenshots here

🌟 Key Concepts Covered

YOLOv8 Object Detection

Custom Dataset Training

KMeans Clustering for Color Segmentation

Optical Flow for Camera Motion Estimation

Perspective Transform (OpenCV)

Real-world Computation of Speed & Distance


📌 Applications

Football Match Analysis

Sports Data Analytics

Player Performance Insight

Real-time Broadcast Enhancements


🤝 Contributing

Contributions are welcome!
Feel free to open an issue or submit a pull request.


📜 License

This project is licensed under the MIT License.
