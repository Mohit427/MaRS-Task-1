# Morse Code Dictionary
MORSE_CODE = {
    '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E',    '..-.': 'F', '--.': 'G',  '....': 'H',
    '..': 'I',   '.---': 'J', '-.-': 'K',  '.-..': 'L',
    '--': 'M',   '-.': 'N',   '---': 'O',  '.--.': 'P',
    '--.-': 'Q', '.-.': 'R',  '...': 'S',  '-': 'T',
    '..-': 'U',  '...-': 'V', '.--': 'W',  '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?',
    '-..-.': '/',  '---...': ':', '-.-.--': '!'
}

def decode_morse(morse_string):
    morse_string = morse_string.strip()#To Remove leading and trailing white spaces
    morse_string = morse_string.replace('  ', '/')#To replace all the white spaces with /

    decoded_words = []#List for all decoded words
    words = morse_string.split('/')#Splitting the string into words by occurence of /

    for word in words:#Looping over the words list(in morse code)
        decoded_letters = []
        letters = word.strip().split(' ')

        for code in letters:
            if code in MORSE_CODE:
                decoded_letters.append(MORSE_CODE[code])#Decoding Letters corresponding in the morse code dictionary
            else:
                decoded_letters.append('?')#Appening ? if the code is not available in dictionary

        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)#Joining decoded words with space

if __name__ == "__main__":
    print("=== Morse Code Decoder ===")
    print("1. Enter Morse code manually")#Getting Input manually from rover
    print("2. Read Morse code from a file")#Reading from a Rover Log file(if required)

    choice = input("\nChoose option (1 or 2): ").strip()

    if choice == '1':#Calling Function directly for the given input
        print("\nTip: Separate letters with single space, words with '/'")
        morse_input = input("Enter Morse code: ").strip()
        result = decode_morse(morse_input)
        print(f"\nDecoded message: {result}")

    elif choice == '2':#Handling the text file, then calling the fuction for output
        file_path = input("Enter file path: ").strip()
        try:
            with open(file_path, 'r') as f:
                morse_input = f.read()
            print(f"\nMorse code from file:\n{morse_input}")
            result = decode_morse(morse_input)
            print(f"\nDecoded message: {result}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found!")

    else:#Handling Invalid Choices
        print("Invalid choice! Please enter 1 or 2.")