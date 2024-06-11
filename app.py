from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import shutil

app = Flask(__name__)
audio_dir = "audios"  # path to your audio directory

@app.route('/')
def index():
    audio_files = []
    for root, _, files in os.walk(audio_dir):
        for file in files:
            if file.endswith('.wav'):
                txt_file = file.replace('.wav', '.txt')
                if txt_file in files:
                    audio_files.append((os.path.join(root, file), os.path.join(root, txt_file)))
    if audio_files:
        return redirect(url_for('edit', idx=0))
    return "No audio files found."

@app.route('/edit/<int:idx>', methods=['GET', 'POST'])
def edit(idx):
    audio_files = []
    for root, _, files in os.walk(audio_dir):
        for file in files:
            if file.endswith('.wav'):
                txt_file = file.replace('.wav', '.txt')
                if txt_file in files:
                    audio_files.append((os.path.join(root, file), os.path.join(root, txt_file)))
    
    if request.method == 'POST':
        edited_text = request.form['transcription']
        current_txt = audio_files[idx][1]
        old_version_txt = current_txt.replace('.txt', '_oldversion.txt')
        
        # Save the old version
        shutil.copy(current_txt, old_version_txt)
        
        # Save the new edited version with the original name
        with open(current_txt, 'w') as f:
            f.write(edited_text)
        
        return redirect(url_for('edit', idx=idx + 1 if idx + 1 < len(audio_files) else 0))

    audio_file, txt_file = audio_files[idx]

    with open(txt_file, 'r') as f:
        transcription = f.read()

    return render_template('index.html', audio_file=audio_file, txt_file=txt_file, transcription=transcription, idx=idx, total=len(audio_files))

@app.route('/audio/<path:filename>')
def audio(filename):
    return send_from_directory(os.path.dirname(filename), os.path.basename(filename))

if __name__ == '__main__':
    app.run(debug=True)
