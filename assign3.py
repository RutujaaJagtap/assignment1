str = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def Pangram(str,alphabet):
    flag = True
    for char in alphabet:
        if char not in str.lower():
            flag = False

    if (flag == True):
        print("Pangram")
    else:
        print("Not Pangram")

Pangram(str,alphabet)