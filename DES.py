#Stefan Buys
#EHN 410 - Toets voorbereiding
#DES Algoritme vir Toetse
#April 2021

import numpy as np

###############################################################################
#                           HELPER FUNCTIONS
###############################################################################

def hexToBinary(string, length = -1):
    mappingTable = {
          '0' : "0000", 
          '1' : "0001",
          '2' : "0010", 
          '3' : "0011",
          '4' : "0100",
          '5' : "0101", 
          '6' : "0110",
          '7' : "0111", 
          '8' : "1000",
          '9' : "1001", 
          'A' : "1010",
          'B' : "1011", 
          'C' : "1100",
          'D' : "1101", 
          'E' : "1110",
          'F' : "1111" }
    
    binary = ""
    for i in range(len(string)):
        binary = binary + mappingTable[string[i]]

    #Remove leading zeros:
    while binary[0] == '0':
        binary = binary[1:]
        
    if not(length == -1):
        while (len(binary) < length):
            binary = '0' + binary
            
    return binary

#print(hexToBinary("ABC",20))

def binaryToHex(string, length = -1):
    mappingTable = {
          "0000" : '0', 
          "0001" : '1',
          "0010" : '2', 
          "0011" : '3',
          "0100" : '4',
          "0101" : '5', 
          "0110" : '6',
          "0111" : '7', 
          "1000" : '8',
          "1001" : '9', 
          "1010" : 'A',
          "1011" : 'B', 
          "1100" : 'C',
          "1101" : 'D', 
          "1110" : 'E',
          "1111" : 'F'  }
    
    #Fill in 0's at the front:
    while not(len(string) % 4 == 0):
        string = "0" + string
    
    hexOut = ""
    
    for i in range(0,len(string),4):
        binary = ""
        for j in range(4):
            binary += string[i+j]
    
        hexOut = hexOut + mappingTable[binary]

    #Remove the leading 0's:
    while hexOut[0] == '0':
        hexOut = hexOut[1:]

    if not(length == -1):
        while (len(hexOut) < length):
            hexOut = '0' + hexOut
        
    return hexOut

#print(binaryToHex("00000000101010111100",5))

def shiftLeft(binary,num=1):
    temp = ""
    for numShifts in range(num):
        for j in range(1,len(binary)):
            temp = temp + binary[j]
        temp = temp + binary[0]
        binary = temp
        temp = ""

    return binary
        
def shiftRight(binary,num=1):
    temp = ""
    for numShifts in range(num):
        temp = temp + binary[len(binary) - 1]
        for j in range(0,len(binary)-1):
            temp = temp + binary[j]
        binary = temp
        temp = ""

    return binary

#print(shiftLeft("1010"))

def xor(a,b):
    answer = ""
    if not(len(a) == len(b)):
        raise Exception("XOR with binary len (a) != binary len (b)")

    for i in range(len(a)):
        if a[i] == b[i]:
            answer = answer + "0"
        else:
            answer = answer + "1"

        if not(a[i] == "0" or a[i] == "1") or not(b[i] == "1" or b[i] == "0"):
            raise Exception("XOR only works with binary, Hex inserted")

    return answer

#print(xor("101","111"))

def permutation(permuteArrInput,binary,indexOrPosition = 0):
    permuteArr = permuteArrInput.copy()

    #If position, decrement all values in permuteArr:
    if indexOrPosition == 1:
        for i in range(len(permuteArr)):
            if permuteArr[i] - 1 < 0:
                print("WARNING: key permutation decremented resulted in a -1 index")
            permuteArr[i] = permuteArr[i] - 1


    #Check if there are enough values:
    if (max(permuteArr) >= len(binary)):
        raise Exception("Permutation, but too few indexes in binary array.")

    output = ""
    for i in range(len(permuteArr)):
        output = output + binary[permuteArr[i]]

    return output

#print(permutation([3,2,1],"110",1))


# Binary to decimal conversion
def binaryToDecimal(binaryIn):
    binary = binaryIn
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
        
        
#print(binaryToDecimal("1011"))

# Decimal to binary conversion
def decimalToBinaryForSsimplified(num):
    res = bin(num).replace("0b", "")
    if len(res) == 1:
        res = '0' + res
    # if(len(res)%4 != 0):
    #     div = len(res) / 4
    #     div = int(div)
    #     counter =(4 * (div + 1)) - len(res)
    #     for i in range(0, counter):
    #         res = '0' + res
    return res

#print(decimalToBinaryForSsimplified(3))

def sLookupSimplified(S, binary):
    row = binary[0] + binary[3]
    column = binary[1] + binary[2]

    rowNum = binaryToDecimal(row)
    columnNum = binaryToDecimal(column)

    return decimalToBinaryForSsimplified(S[rowNum][columnNum])
        
#hello = "HelloHoeGaanDit"
#print(hello[0:5])

def permutationsToIndex(permutation):
    output = []
    for i in range(permutation):
        output.append(permutation[i] - 1)
        if permutation[i] - 1 < 0:
            print("WARNING: key permutation decremented resulted in a -1 index")
            return permutation
    return output


#NBNBNB The function that operates on the Left data block:
def F(right, key):
    return xor(right,key)


    #NB -> S-box calculations left out...
    

###############################################################################
#                          DES ALGORITME BEGIN
###############################################################################
    
#Website as riglyn gebruik: https://web.archive.org/web/20201118130935/http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm

#NB -> as die key 64 bits het, gooi elke 8ste een weg
key = "11110000110011001010101011110101010101100110011110001111"

plaintext = "0000000100100011010001010110011110001001101010111100110111101111"

# KEY GENERATION

#NB No initial key permutation, insert thatr here:

keyLeft = key[0:28]
keyRight = key[28:56]

subkeys = []
oneBitShifts = [1,2,9,16]
#(Compression P Box)
keyPermutation = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
for i in range(16):
    #Shift the keys left (NB: geekforgeeks, doen hulle 2x shift by party, werk in indien nodig)
    if (i+1) in oneBitShifts:
        numshifts = 1
    else:
        numshifts = 2
    
    keyLeft = shiftLeft(keyLeft,numshifts)
    keyRight = shiftLeft(keyRight,numshifts)
    intermediateKey = keyLeft + keyRight
    subkeys.append(permutation(keyPermutation,intermediateKey,1))
    
#NBNBNB Uncomment for encryption:

#NBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNB

#Uncomment for decryption

#For decryption:
#subKeyTemp = subkey
#subkey = []
#for i in range(len(subKeyTemp)-1,-1,-1):
#    subkey.append(subKeyTemp[i])


#NBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNB
    
#========= KEYS GENERATED
    

# ENCRYPTION ALGORITHM START

ciphertextTemp = plaintext

#Do the initial permuation
IP=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

ciphertextTemp = permutation(IP,ciphertextTemp,1)


for round in range(16):
    ciphertextTempL0 = ciphertextTemp[0:32]
    ciphertextTempR0 = ciphertextTemp[32:64]
    
    rightperm = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
    ciphertextTempR0perm = permutation(rightperm,ciphertextTempR0)
    
    ciphertextTempL1 = ciphertextTempR0
    ciphertextTempR1 = F(ciphertextTempR0,subkeys[round])
    ciphertextTempR1 = xor(ciphertextTempL0, ciphertextTempR1)
    
    ciphertextTemp = ciphertextTempL1 + ciphertextTempR1
    
#Do the inverse permuation
invIP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
ciphertext = permutation(invIP,ciphertextTemp,1)