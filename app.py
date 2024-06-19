from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
import shutil

app = Flask(__name__)
audio_dir = None  # We'll set this later based on user input

def find_audio_files(directory):
    audio_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                txt_file = file.replace('.wav', '.txt')
                if txt_file in files:
                    audio_files.append((os.path.join(root, file), os.path.join(root, txt_file)))
    return audio_files

@app.route('/')
def index():
    return render_template('directory_input.html')

@app.route('/set_directory', methods=['POST'])
def set_directory():
    global audio_dir
    audio_dir = request.form['directory']
    audio_files = find_audio_files(audio_dir)
    if audio_files:
        return redirect(url_for('edit', idx=0))
    return "No audio files found in the specified directory."

@app.route('/edit/<int:idx>', methods=['GET', 'POST'])
def edit(idx):
    audio_files = find_audio_files(audio_dir)

    if request.method == 'POST':
        edited_text = request.form['transcription']
        current_txt = audio_files[idx][1]
        old_version_txt = current_txt.replace('.txt', '_oldversion.txt')
        
        # Save the old version
        if os.path.exists(current_txt):
            shutil.copy(current_txt, old_version_txt)
        
        # Save the new edited version with the original name
        with open(current_txt, 'w', encoding='utf-8') as f:
            f.write(edited_text)
        
        return redirect(url_for('edit', idx=idx + 1 if idx + 1 < len(audio_files) else 0))

    audio_file, txt_file = audio_files[idx]

    with open(txt_file, 'r', encoding='utf-8') as f:
        transcription = f.read()

    return render_template('index.html', audio_file=audio_file, txt_file=txt_file, transcription=transcription, idx=idx, total=len(audio_files))

@app.route('/audio/<path:filename>')
def audio(filename):
    return send_from_directory(os.path.dirname(filename), os.path.basename(filename))

if __name__ == '__main__':
    app.run(debug=True)
