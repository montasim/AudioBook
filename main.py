"""
****************************************************************************
𝕻𝖗𝖔𝖌𝖗𝖆𝖒 𝕹𝖆𝖒𝖊 : 𝕬𝖚𝖉𝖎𝖔𝕭𝖔𝖔𝖐
𝕬𝖚𝖙𝖍𝖔𝖗       : 𝕸𝖔𝖓𝖙𝖆𝖘𝖎𝖒
𝕮𝖗𝖊𝖆𝖙𝖊𝖉 𝖔𝖓   : 10.11.2020
𝕮𝖔𝖓𝖙𝖆𝖈𝖙      : 𝖍𝖙𝖙𝖕𝖘://𝖌𝖎𝖙𝖍𝖚𝖇.𝖈𝖔𝖒/𝖒𝖔𝖓𝖙𝖆𝖘𝖎𝖒


# used variables in this program
pdfFile     - open file in read & binary mode
pdfReader   - read pdf file
speak       - speak what is readen
readPage    - read page number
pageNumber  - get page number from start to end
readSpeed   - set speed rate
voices      - change voices
*****************************************************************************
"""

#   importing pyttsx3 for speak sentances from pdf
import pyttsx3

#   importing PyPDF2 for handling pdf file
import PyPDF2

#   opening pdf file in read mode and binary mode
pdfFile = open('mypdf.pdf', 'rb')

#   reading pdf file
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#   initializing pyttsx3 for make it ready to speak
speak = pyttsx3.init()

#   change voice
voices = speak.getProperty('voices')

# changing index, changes voices. o for male
# speak.setProperty('voice', voices[0].id)

# changing index, changes voices. 1 for female
speak.setProperty('voice', voices[1].id)

#   set speak speed
rate = speak.getProperty('rate')
speak.setProperty('rate', rate - 25)

"""
#   speak what is inside say function
speak.say('speak now')

#   showing number of ages in a pdf file
print(pdfReader.numPages)
"""

#   getting page number from start to end
for pageNumber in range(0, pdfReader.numPages):
    #   read from a specific page 
    readPage = pdfReader.getPage(pageNumber)

    #   read page and extract text into a variable
    readText = readPage.extractText()

    #   speak what is in the pdf file
    speak.say(readText)

    #   save text as mp3 file
    speak.save_to_file(readText, 'mypdf.mp3')

    #   make speak function work
    speak.runAndWait()


"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████───██████████████────██████████████───████████──████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░██───██░░░░██──██░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░████░░░░██─██░░██████████────██░░██████░░██───████░░██──██░░████─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██──██░░██─────██░░░░██░░░░██───
─██░░██──██░░██──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░██████░░████───████░░░░░░████───
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░░░░░██─────████░░████─────
─██░░██──██████──██░░██─██░░██████░░██─██░░██──██░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────────────██░░██────██░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░████░░░░██─██░░██████████────██░░████████░░██───────██░░██───────
─██░░██──────────██░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██────██░░░░░░░░░░░░██───────██░░██───────
─██████──────────██████─██████──██████─████████████───██████████████────████████████████───────██████───────
────────────────────────────────────────────────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─██████──────────██████─██████████████─██████████████─██████████████─██████████─██████──────────██████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██████████████░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████░░██─██░░░░░░░░░░██──██░░██─██████░░██████─██░░██████░░██─██░░██████████─████░░████─██░░░░░░░░░░░░░░░░░░██─
─██░░██████░░██████░░██─██░░██──██░░██─██░░██████░░██──██░░██─────██░░██─────██░░██──██░░██─██░░██───────────██░░██───██░░██████░░██████░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██░░██████████───██░░██───██░░██──██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██───██░░██──██░░██──██░░██─
─██░░██──██████──██░░██─██░░██──██░░██─██░░██──██░░██──██░░██─────██░░██─────██░░██████░░██─██████████░░██───██░░██───██░░██──██████──██░░██─
─██░░██──────────██░░██─██░░██──██░░██─██░░██──██░░██████░░██─────██░░██─────██░░██──██░░██─────────██░░██───██░░██───██░░██──────────██░░██─
─██░░██──────────██░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██████████░░██─████░░████─██░░██──────────██░░██─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██──██████████░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░██──────────██░░██─
─██████──────────██████─██████████████─██████──────────██████─────██████─────██████──██████─██████████████─██████████─██████──────────██████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
