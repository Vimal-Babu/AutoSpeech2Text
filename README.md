# AutoSpeech2Text

This project converts audio or video files to text using speech-to-text transcription.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoSpeech2Text.git
   ```

2. Navigate into the project directory:
   ```bash
   cd AutoSpeech2Text
   ```

3. Create a virtual environment:
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. Install required dependencies:
   ```bash
   pip install -r requirements.txt

   ```

6. Install FFmpeg (Required for Processing Audio/Video Files)
   The program relies on FFmpeg for handling media files.

   On Windows:

      Download ffmpeg-release-full.7z from: FFmpeg Release Builds
      Extract the files and locate the bin folder.
      Copy the path to the bin folder (e.g., C:\ffmpeg\bin).
      Add it to your Windows Environment Variables under Path.

   On macOS/Linux:
    ```bash
   sudo apt update && sudo apt install ffmpeg -y  # Ubuntu/Debian
   brew install ffmpeg  # macOS (Homebrew)
    ```
   
   

## Usage

To transcribe an audio or video file, run:
```bash
python audiospeech2text.py


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

