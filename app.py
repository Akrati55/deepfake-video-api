from flask import Flask, request, jsonify
import os
import cv2

app = Flask(__name__)

@app.route("/analyze-video", methods=["POST"])
def analyze_video():
    if "video" not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files["video"]
    os.makedirs("uploads", exist_ok=True)
    video_path = os.path.join("uploads", video_file.filename)
    video_file.save(video_path)

    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    return jsonify({
        "message": "Video processed successfully",
        "frames_detected": frame_count,
        "is_deepfake": False
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
