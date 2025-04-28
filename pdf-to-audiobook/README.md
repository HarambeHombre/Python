# PDF to Speech Converter - ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**PDF to Speech Converter** is a Python script that extracts text from a PDF file and converts it to speech in the form of an MP3 file. It utilizes the `PyPDF2` library for PDF text extraction, `gTTS` (Google Text-to-Speech) for speech synthesis, and `playsound` for playing the generated audio file.

---

## Features
- Extracts text from any PDF file.
- Converts extracted text into an MP3 audio file.
- Enables playback of the generated audio file using `playsound`.

---

## Installation

Before you use this script, ensure that you have Python installed on your system. You also need to install the following Python libraries:

1. `gtts` - Google Text-to-Speech
2. `PyPDF2` - A library for working with PDF files
3. `playsound` - A library for playing audio files

To install these libraries, run the following commands in your terminal:

```bash
pip install gtts
pip install PyPDF2
pip install playsound
```

---

## Usage
- Prepare the PDF file: Place the PDF file (`text-to-convert.pdf`) in the same directory as the script.
- Run the script: Execute the Python script using the following command:
```bash
  python main.py
```
- Generated Audio File: The script will create an MP3 file (`audio.mp3`) containing the converted speech.
- Optional Playback: Uncomment the playsound(filename) line at the end of the script to listen to the audio file immediately after it is created.

---

## Script Breakdown
### Import Libraries
The script begins by importing necessary libraries:
```bash
from gtts import gTTS
import PyPDF2
import playsound
```

---

## Open and Read the PDF
A PDF file is opened in read-binary mode, and the `PyPDF2` library reads its contents:
```bash
pdf_file = open('text-to-convert.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
```

---

### Extract Text
The text is extracted from all pages of the PDF:
```bash
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()
```

---

### Convert Text to Speech
Using `gTTS`, the extracted text is converted to speech:
```bash
filename = 'audio.mp3'
tts = gTTS(text)
tts.save(filename)
```

---

### Play the Audio File
Optionally, you can play the generated audio file:
```bash
playsound(filename)
```

---

### Example Output
After running the script, you will get:
- The extracted text printed in the console.
- An MP3 file named `audio.mp3`.

---

### Notes
- Ensure the PDF file is not password-protected, as `PyPDF2` may not be able to extract text from secured files.
- This script assumes that the PDF contains readable text. Scanned PDFs might require Optical Character Recognition (OCR) software for text extraction.



