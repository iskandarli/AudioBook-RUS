import os
import platform
import PyPDF2
from googletrans import Translator
from gtts import gTTS
import time

# Provide the correct path to the PDF file
pdf_path = 'oop.pdf'



try:
    # Open the PDF file
    with open(pdf_path, 'rb') as book:
        # Create a PDF reader object
        pdfReader = PyPDF2.PdfReader(book)

        # Specify the page number (0-indexed)
        target_page_number = 6 # Page 7 (0-indexed)

        # Get the spelified page
        target_page = pdfReader.pages [target_page_number]

        # Extract text from the page
        page_text = target_page.extract_text()

        #Translate the text to Russian
        translator = Translator()
        translated_text = translator.translate(page_text, dest='ru').text

        # Print the original and translated text
        print(f'Original text from page {target_page_number + 1}: \n{page_text}')
        print(f'Translated text to Russian: \n{translated_text}')

        # Use gTTS to convert translated text to speech
        tts = gTTS(translated_text, lang='ru')
        tts.save("output_ru.mp3")

        # Play the MP3 file based on the platform
        if platform.system() == 'Darwin':
            os.system("open output_ru.mp3")
        elif platform.system() == 'Windows':
            os.system("start output_ru.mp3")
        else:
            print("Unsupported platform. Please manually open 'output_ru.mp3'.")

        # Add a delay to ensure the audio playback completes before the program ends
        time.sleep(5)

except FileNotFoundError:
    print(f'Error: The file {pdf_path} was not found.')

except Exception as e:
    print(f'Error during text-to-speech: {e}')
