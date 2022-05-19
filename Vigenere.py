#Stefan Buys
#EHN 410 - Toets voorbereiding
#Vigenere cipher - polyalphabetic substitution
#April 2021

import numpy as np

key = ""
plaintext = ""

def alphaToNum(alpha):
    alpha = alpha.lower()
    return ord(alpha) - 96

def numToAlpha(num):
    num = num + 96
    return chr(num)

#Copy the key repeatedly:
while len(key) < len(plaintext):
    key = key + key

#Convert the key to numbers:
keyNum = []
for i in range(len(key)):
    keyNum.append(alphaToNum(key[i]))
    
#Convert the alphabet letters to numbers:
plaintextNum = []
for i in range(len(plaintext)):
    plaintextNum.append(alphaToNum(plaintext[i]))
    
#Go through the plaintext, creating the ciphertext:
cipherTextNum = []
for i in range(len(plaintextNum)):
    cipherTextNum[i] = (keyNum[i] + plaintextNum[i]) % 26
    
#Convert the ciphertext number to characters:
cipherout = ""
for i in range(len(cipherTextNum)):
    cipherout = cipherout + numToAlpha(cipherTextNum[i])
    
print(cipherout)