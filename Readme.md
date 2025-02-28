# Flask YouTube Video Downloader

This is a simple **Flask-based YouTube video downloader** using `yt-dlp`. It provides an API where users can submit a YouTube video URL and download it directly from the server.

## 🚀 Features
- Accepts a YouTube video URL via API.
- Downloads the best available video format.
- Stores downloaded videos in the `downloads/` directory.
- Provides an endpoint to retrieve the downloaded video.

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zeeshan-shafeek/yt-dl-test.git
cd yt-dl-test
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage
### Start the Flask Server
```bash
python app.py
```
By default, the server runs on `http://127.0.0.1:8000`.

### API Endpoints
#### 🎯 Download a YouTube Video
**Request:**
```bash
GET /download?url=https://www.youtube.com/watch?v=VIDEO_ID
```
**Response:**
```json
{
  "status": "Download started",
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

#### 🎯 Retrieve a Downloaded Video
Once the video is downloaded, retrieve it from:
```bash
GET /downloads/VIDEO_FILENAME
```
Example:
```bash
GET http://127.0.0.1:8000/downloads/video-file.mp4
```

## 📌 Notes
- Ensure `yt-dlp` is installed properly.
- The `downloads/` folder must have **write permissions**.
- This is for **educational purposes only**. Downloading YouTube videos may violate **YouTube's Terms of Service**.

