# detect_traffic.py
import cv2
from ultralytics import YOLO

def process_video_for_traffic(video_path, output_path, confidence_threshold=0.5):
    """
    Performs object detection on a video stream using a pre-trained YOLOv8 model.
    Only focuses on 'car', 'truck', and 'bus' (common traffic objects).
    """
    print(f"Loading model and processing video: {video_path}")
    
    # 1. Load the pre-trained YOLOv8 model
    # 'n' stands for nano—the smallest and fastest version for quick testing.
    model = YOLO('yolov8n.pt') 

    # 2. Define the classes we are interested in (COCO dataset indexes)
    # 2: car, 5: bus, 7: truck
    target_classes = [2, 5, 7]
    
    # 3. Setup video input and output
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    # Using 'mp4v' for broader compatibility
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 4. Perform detection
        # The 'stream=True' setting returns an iterator for more memory efficiency
        results = model.track(
            frame, 
            persist=True, 
            classes=target_classes, 
            conf=confidence_threshold, 
            iou=0.5, 
            verbose=False # Keep console clean
        )
        
        # 5. Draw the results on the frame
        # The plot method handles drawing bounding boxes and labels for us
        annotated_frame = results[0].plot()

        # 6. Write the annotated frame to the output video
        out.write(annotated_frame)
        
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames...")

    # 7. Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"\nProcessing complete. Output saved to {output_path}")


if __name__ == "__main__":
    # ⚠️ Replace 'input_traffic_video.mp4' with the path to your video file!
    # A short video (10-15 seconds) is best for a quick demo.
    INPUT_VIDEO = 'input_traffic_video.mp4' 
    OUTPUT_VIDEO = 'detected_traffic_output.mp4'
    
    # Download a sample traffic video and name it 'input_traffic_video.mp4'
    # E.g., search YouTube/Pexels for "free traffic video"
    
    process_video_for_traffic(INPUT_VIDEO, OUTPUT_VIDEO)

    # Optional: Display the first detected frame for a quick check (requires GUI)
    # if cv2.cuda.getCudaEnabledDeviceCount() == 0:
    #     cv2.imshow('Example Detection', cv2.imread(results[0].path))
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
