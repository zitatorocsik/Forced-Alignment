import subprocess
import speech_recognition as sr
import os

def transcribe_audio_to_text(audio_path, text_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    # Perform speech recognition using Google's free API
    try:
        # Transcribe audio to text
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)

        # Save the transcription to a text file
        with open(text_path, 'w') as f:
            f.write(text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def run_montreal_forced_aligner(audio_dir, output_dir):
    # Run Montreal Forced Aligner
    subprocess.run([
        'mfa',
        'align',
        audio_dir,
        'english_us_mfa',
        'english_mfa',  # Specify language or path to a pretrained model
        output_dir
    ])

# File paths
audio_file_path = 'audio/audio.wav'
text_file_path = 'text/transcipt.txt'
audio_dir = 'audio'
output_dir = 'output'

# Step 1: Transcribe the audio to a text file
# transcribe_audio_to_text(audio_file_path, text_file_path)

# Step 2: Run Montreal Forced Aligner with the generated text file
# Ensure the directories contain the appropriate files before running MFA
run_montreal_forced_aligner(audio_dir, output_dir)
