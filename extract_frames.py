import cv2
import os

video_path = "/home/zxcv/Projects/F1-Race-Line-Analyzer/src/max_suzuka_h264.mp4"
output_dir = "frames"

cap = cv2.VideoCapture(video_path)
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f"{output_dir}/frame_{count:04d}.jpg", frame)
    count += 1

cap.release()
print(f"Extracted {count} frames.")
