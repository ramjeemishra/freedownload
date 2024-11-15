import yt_dlp
from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Create a temporary file path
    download_path = '/tmp/%(title)s.%(ext)s'

    # yt-dlp options
    ydl_opts = {
        'outtmpl': download_path,
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)

        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Export the app for Vercel
app = app
