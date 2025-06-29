# cross_camera_reid/main.py

import cv2
from ultralytics import YOLO
import os

def run_yolo_on_video(video_path, output_path, model_path):
    # Load YOLO
    model = YOLO(model_path)
    
    cap = cv2.VideoCapture(video_path)

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        boxes = results[0].boxes.xyxy.cpu().numpy()

        for box in boxes:
            x1,y1,x2,y2 = map(int, box[:4])
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

        out.write(frame)
    
    cap.release()
    out.release()
    print(f"Saved {output_path}")


if __name__ == "__main__":
    run_yolo_on_video(
        video_path="videos/broadcast.mp4",
        output_path="outputs/broadcast_detected.mp4",
        model_path="models/best.pt"
    )
    
    run_yolo_on_video(
        video_path="videos/tacticam.mp4",
        output_path="outputs/tacticam_detected.mp4",
        model_path="models/best.pt"
    )
