import re
def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    # Messy brute force approach
    words = re.findall(r'(\S+)+' , morse_code)
    for txt in words: 
        morse_code = morse_code.replace(txt, MORSE_CODE[txt], 1)
    space = re.findall(r'\s\s+', morse_code)
    for white in space:
        morse_code = morse_code.replace(white, '_')
    morse_code = morse_code.replace(' ', '').replace('_', ' ')
    morse_code = morse_code.strip()
    return morse_code
