# Computer Vision Traffic Pipeline (CV-Pipeline)

This repository contains a containerized batch processing application for real-time traffic object detection in video streams, built using **Python** and **YOLOv8**.

The project demonstrates core competencies in optimizing and automating an **AI pipeline** for scalability and integration with modern **Cloud Computing Platforms**.

---

## Project Highlights

* **Application:** Object detection on video streams, focusing on cars, buses, and trucks (classes 2, 5, 7 from COCO dataset).
* **Core Technology:** `ultralytics` (YOLOv8n) for lightweight, high-performance inference.
* **Goal:** Serve as a proof-of-concept for a scalable, automated AI microservice suitable for deployment in an enterprise cloud environment.

## Technology Stack

| Component | Technology | Role in Pipeline |
| :--- | :--- | :--- |
| **Scripting** | **Python 3.12** | Core implementation of the detection logic. |
| **Containerization** | **Docker** | Creates a standardized, reproducible execution environment. |
| **Orchestration** | **Kubernetes (K8s) Job** | Defines the batch workload for seamless, state-of-the-art cloud deployment. |
| **Automation** | **GitHub Actions** | Implements Continuous Integration (CI) for automated build and push to a container registry. |

---

## Project Structure & Execution

### 1. The Core Script: `detect_traffic.py`

This script uses OpenCV and YOLOv8 to load a video (`input_traffic_video.mp4`), perform object tracking and detection, and save the result to `detected_traffic_output.mp4`.

### 2. Building the Docker Image (Containerization)

The `Dockerfile` provides a lightweight, multi-stage build, ensuring minimal footprint and reproducibility across environments.

```bash
# Build the image (e.g., using your Docker Hub username)
docker build -t your-username/traffic-ai-pipeline:latest .

# Run the container locally (requires an input video file in the host folder)
# The output file will be created inside the container's /app directory.
docker run -v $(pwd)/:/app your-username/traffic-ai-pipeline:latest
