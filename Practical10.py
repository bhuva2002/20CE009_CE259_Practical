# AIM: Generate PDF file of your 3rd Semester Mark-sheet.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

from PIL import Image

# Opening the Image from its path
img = Image.open(r'D:\SEM-4\Python\SEM3_RESULT.png')

# Converting the opened image into pdf file
image_ms = img.convert('RGB')

# Saving the generated pdf file at specified address
image_ms.save(r'D:\SEM-4\Python\Practical10_SEM3_RESULT.pdf')
