# Dockerfile

# === Stage 1: Build/Install Dependencies ===
# Using a slim base image to reduce final size
FROM python:3.12-slim AS builder

# Install system dependencies required for opencv-python and video codecs
# These are necessary for the cv2.VideoCapture and cv2.VideoWriter functions
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# === Stage 2: Final Runtime Image ===
FROM python:3.12-slim

# Copy the system dependencies from the builder stage
# This keeps the final image smaller than installing them again
COPY --from=builder /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu
COPY --from=builder /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Install the essential system libraries in the final image
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy your script and the input video file
# NOTE: The input video needs to be in your project directory
COPY detect_traffic.py .
COPY input_traffic_video.mp4 . 

# Define the command to run the script. This is the entrypoint of the container.
# The script will execute, process 'input_traffic_video.mp4', and create 'detected_traffic_output.mp4'.
CMD ["python3", "detect_traffic.py"]
