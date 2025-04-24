from gtts import gTTS
import PyPDF2
import playsound

pdf_file = open('text-to-convert.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

print(text)
filename = 'audio.mp3'

tts = gTTS(text)
tts.save(filename)

# playsound(filename)