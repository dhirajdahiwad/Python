try:
    from PIL import Image
    from spellchecker import SpellChecker
except ImportError:
    import Image
import pytesseract

spell = SpellChecker()

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('ocr.jpg')))

stringdataset = pytesseract.image_to_string(Image.open('ocr.jpg'))

mywordlist = stringdataset.split(".")

print(mywordlist)

for word in mywordlist:
    mysingalword = word.split(" ")
    print(mysingalword)

# find those words that may be misspelled
misspelled = spell.unknown(mywordlist)

#for word in misspelled:
    # Get the one `most likely` answer
    # print(spell.correction(word))

    # Get a list of `likely` options
    # print(spell.candidates(word))