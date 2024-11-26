# 📥 YouTube Downloader Script

Easily download YouTube videos, playlists, or channels in **video** or **MP3 audio** format using this Python script. It leverages the powerful `yt-dlp` library to handle downloads from YouTube and other platforms seamlessly.

---

## 🌟 Features

- 🎥 Download individual YouTube videos.  
- 📃 Download entire playlists.  
- 🎬 Download all videos from a channel.  
- 🎶 Options to download as video or MP3 audio.  
- 📁 Automatically organizes files into separate directories.  

---

## 📋 Requirements

- **Python 3.x**: Make sure you have Python installed on your system.  
- **yt-dlp**: Install via pip.  

---

### 📦 Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/abdelghafouur/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Install dependencies**:  
   ```bash
   pip install yt-dlp
   ```

---

## 🚀 Usage

To start downloading content:  

1. **Run the script**:  
   ```bash
   python yt_downloader.py
   ```  

2. **Follow the prompts**:  

   - 🖇️ **Input the URL**: Enter the link to the YouTube video, playlist, or channel.  
   - 🎛️ **Choose the format**:  
     - Enter **1** for video.  
     - Enter **2** for MP3 audio.  
   - 🗂️ **Specify the content type**:  
     - Enter **1** for a single video.  
     - Enter **2** for a playlist.  
     - Enter **3** for a channel.  

---

### 🔍 Examples  

#### **Download a single video**:  
```bash
Enter the YouTube video, playlist, or channel URL: https://www.youtube.com/watch?v=xxxxxxxxxxxxxx  
Enter '1' for video or '2' for MP3 audio: 1  
Is this a (1) single video, (2) playlist, or (3) channel? Enter '1', '2', or '3': 1  
```  

#### **Download a playlist**:  
```bash
Enter the YouTube video, playlist, or channel URL: https://www.youtube.com/playlist?list=xxxxxxxxxxxxxx  
Enter '1' for video or '2' for MP3 audio: 2  
Is this a (1) single video, (2) playlist, or (3) channel? Enter '1', '2', or '3': 2  
```  

#### **Download all videos from a channel**:  
```bash
Enter the YouTube video, playlist, or channel URL: https://www.youtube.com/c/YourChannelName  
Enter '1' for video or '2' for MP3 audio: 1  
Is this a (1) single video, (2) playlist, or (3) channel? Enter '1', '2', or '3': 3  
```

---

### 📂 Directory Structure  

- **Video files**: Saved to `download_video/`.  
- **MP3 files**: Saved to `download_mp3/`.  

These directories are created automatically if they don’t exist.

---

## ⚙️ Options  

- **Video format**: Downloads the best available video quality.  
- **MP3 format**: Extracts audio and saves it as a high-quality MP3 (192kbps).  

---

## 🛠️ Error Handling  

- 🚨 If the URL is invalid or unavailable, the script notifies you and allows re-entry.  
- ✋ Graceful exit: Use `Ctrl+C` to stop the script anytime.  

---

## 📝 License  

This project is licensed under the **MIT License**. See the LICENSE file for details.  

---

## 🤝 Contributing  

Want to improve this script? Follow these steps:  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -am 'Add new feature'
   ```  
4. Push to your branch:  
   ```bash
   git push origin feature-name
   ```  
5. Open a pull request.  

---

## 🙏 Acknowledgements  

Thanks to **yt-dlp** for providing a reliable way to handle video downloads.

---

## 📬 Contact  

Feel free to reach out for questions or feedback:  
📧 **abdelghafourlahnida01@gmail.com**  