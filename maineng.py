from gtts import gTTS
import os
import platform
import PyPDF2

# Provide the correct path to the PDF file
pdf_path = 'oop.pdf'

try:
    # Open the PDF file
    with open(pdf_path, 'rb') as book:
        # Create a PDF reader object
        pdfReader = PyPDF2.PdfReader(book)

        # Specify the page number (0-indexed)
        target_page_number = 6  # Page 7 (0-indexed)

        # Get the specified page
        target_page = pdfReader.pages[target_page_number]

        # Extract text from the page
        page_text = target_page.extract_text()

        # Print the text from the specified page
        print(f'Text from page {target_page_number + 1}: \n{page_text}')

        # Use the extracted text for text-to-speech
        tts = gTTS(page_text)

        # Save the spoken text to an MP3 file
        tts.save("output.mp3")

except FileNotFoundError:
    print(f'Error: The file {pdf_path} was not found.')

# Play the MP3 file based on the platform
if platform.system() == 'Darwin':
    os.system("open output.mp3")
elif platform.system() == 'Windows':
    os.system("start output.mp3")
else:
    print("Unsupported platform. Please manually open 'output.mp3'.")
