import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize Tkinter
root = tk.Tk()
root.title("Text to Speech / Speech to Text")

# Function to convert text to speech
def text_to_speech():
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Get text from user input
    text = text_entry.get()

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Function to convert speech to text
def speech_to_text():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Ask user to select an audio file
    audio_file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=(("WAV files", "*.wav"), ("All files", "*.*")))

    # Check if a file is selected
    if not audio_file_path:
        messagebox.showerror("Error", "No audio file selected.")
        return

    # Load audio file
    with sr.AudioFile(audio_file_path) as source:
        # Record the audio
        audio_data = recognizer.record(source)

        # Recognize speech using Google Speech Recognition
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            messagebox.showinfo("Speech to Text", "The text in the audio file is:\n{}".format(text))
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, could not understand the audio.")
        except sr.RequestError as e:
            messagebox.showerror("Error", "Error fetching results from Google Speech Recognition service; {0}".format(e))

# GUI elements
text_label = tk.Label(root, text="Enter text:")
text_label.grid(row=0, column=0, padx=5, pady=5)

text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=5, pady=5)

text_to_speech_button = tk.Button(root, text="Text to Speech", command=text_to_speech)
text_to_speech_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")

speech_to_text_button = tk.Button(root, text="Speech to Text", command=speech_to_text)
speech_to_text_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Run the Tkinter event loop
root.mainloop()
