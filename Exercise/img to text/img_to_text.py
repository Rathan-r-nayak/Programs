import pytesseract
import shutil
import os
import random
from PIL import Image


extractedInformation = pytesseract.image_to_string(Image.open('img.png'))
print(extractedInformation)