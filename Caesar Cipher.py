shift = 5
alphabet ='abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
text = 'hello world'
