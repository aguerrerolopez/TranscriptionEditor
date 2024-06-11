# 📜 Manual Transcription Editor

This is a simple yet useful app that helps you manually correct automatic transcriptions made by Whisper. The app allows you to play audio files and edit their corresponding transcriptions.

## ✨ Features

- 🔊 Play audio files directly from the browser.
- ✍️ Edit and save transcriptions.
- 📁 Automatically saves the old version of the transcription with `_oldversion.txt`.

## 🛠 Prerequisites

- 🐍 Python 3.x

## 💾 Installation

1. Clone this repository to your local machine.
2. Place your audio dataset in the `audios` folder. For each `.wav` file, the transcription MUST have the same name but with a `.txt` extension.

### Steps

1. **Run the Installation Script**

    This script will create a virtual environment, install the necessary dependencies, and run the Flask application.

    ```bash
    ./install.sh
    ```

2. **Run the Application**

    Use the following command to run the application if it's not already running from the installation script.

    ```bash
    ./run.sh
    ```

3. **Access the Application**

    Open your web browser and go to `http://127.0.0.1:5000/`.

## 📂 Directory Structure

Your project directory should look like this:



```
project/
├── app.py
├── requirements.txt
├── install.sh
├── run.sh
├── README.md
├── static/
│ └── play.png # (Optional: sound icon if needed)
├── templates/
│ └── index.html
├── audios/ # Directory containing subfolders with .wav and .txt files
```


## 🚀 Usage

1. Place your `.wav` audio files and their corresponding `.txt` transcription files in the `audios` directory. Ensure that each `.wav` file has a corresponding `.txt` file with the same name.
2. Run the application using the installation script.
3. Use the web interface to play audio files and manually correct transcriptions.
4. Press the "Next" button to save the edited transcription and proceed to the next file. The old version of the transcription will be saved with `_oldversion.txt`.

## 🙏 How to cite or acknowledge

If you find this tool useful in your research or work, please consider citing or acknowledging it as follows:

```markdown
Guerrero-López, Alejandro. 2024. Manual Transcription Editor: A tool for manually correcting automatic transcriptions. Available at https://github.com/aguerrerolopez/TranscriptionEditor.

```	

## 🙏 Acknowledgements

Thanks to GPT for programming almost all of this project. Am I now a prompt engineer? 😉


## 📜 License

This project is licensed under the MIT License.

