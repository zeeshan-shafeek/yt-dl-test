from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Set the download directory
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/download", methods=["GET"])
def download_video():
    video_url = request.args.get("url")
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Define the output filename template
        output_template = os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s")

        # Use yt-dlp to download the video
        command = [
            "yt-dlp",
            "--format", "best",
            "-o", output_template,
            video_url
        ]

        subprocess.run(command, check=True)
        return jsonify({"status": "Download started", "video_url": video_url})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
