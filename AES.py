#Stefan Buys
#EHN 410 - Toets voorbereiding
#DES Algoritme vir Toetse
#April 2021

import numpy as np
import copy

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

def binaryToHex(stringIn, length = -1):
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
    
    string = stringIn
    #Fill in 0's at the front:
    while not(len(string) % 4 == 0):
        string = "0" + string
    
    hexOut = ""
    
    for i in range(0,len(string),4):
        binary = ""
        for j in range(4):
            binary += string[i+j]
    
        hexOut = hexOut + mappingTable[binary]
        

    
    #if there are 1s in hexOut:
    if '1' in hexOut:
        #Remove the leading 0's:
        while hexOut[0] == '0':
            hexOut = hexOut[1:]

    if not(length == -1):
        while (len(hexOut) < length):
            hexOut = '0' + hexOut
        
    return hexOut

#print(binaryToHex("00000000101010111100",5))

def shiftLeft(binaryIn,num=1):
    binary = binaryIn
    temp = ""
    for numShifts in range(num):
        for j in range(1,len(binary)):
            temp = temp + binary[j]
        temp = temp + binary[0]
        binary = temp
        temp = ""

    return binary
        
def shiftRight(binaryIn,num=1):
    binary = binaryIn
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

def decimalToBinary(num,numDigits):
    res = bin(num).replace("0b", "")
    while len(res) < numDigits:
        res = '0' + res
    return res

###############################################################################
#                           Variables:
###############################################################################

Sbox = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
]

def SboxLookup(binaryIn):
    binary = binaryIn
    while len(binary) < 8:
        binary = '0' + binary
    
    lefttext = binary[0:4]
    righttext = binary[4:8]

    hexAnswer = Sbox[binaryToDecimal(lefttext)][binaryToDecimal(righttext)]

    return decimalToBinary(hexAnswer,8)  

#For key generation:
def functionG(w,roundnum):
    wcopy = w
    while len(wcopy) < 32:
        wcopy = '0' + wcopy

    B = []
    B.append(wcopy[0:8])
    B.append(wcopy[8:16])
    B.append(wcopy[16:24])
    B.append(wcopy[24:32])
        
    #Shift left the Bs:
    temp = B[0]
    B[0] = B[1]
    B[1] = B[2]
    B[2] = B[3]
    B[3] = temp

    #S-box lookups:
    for i in range(4):
        B[i] = SboxLookup(B[i])
       
    RC = ["00000001","00000010","00000100","00001000","00010000","00100000","01000000","10000000","00011011","00110110"]
    
    B[0] = xor(B[0],RC[roundnum])
    
    answer = ""
    for i in range(len(B)):
        answer = answer + B[i]
        
    return answer

def generateMatrix(binarystring):
    matrix = [["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]
    
    if len(binarystring) < 128:
        raise Exception("generateMatrix with binarystring with len < 128")
        
    index = 0
    for column in range(4):
        for row in range(4):
            temp = ""
            for bit in range(8):
                temp = temp + binarystring[index]
                index += 1
                
                matrix[row][column] = temp      
    return matrix

def matrixBinaryToHex(matrix):
    return [[binaryToHex(c) for c in cs] for cs in matrix]

def printMatrix(matrix):
    print(np.array(matrixBinaryToHex(matrix)))
    

def xorMatrix(A,B):
    temp = copy.deepcopy(A)
    for i in range(4):
        for j in range(4):
            temp[i][j] = xor(A[i][j],B[i][j])
    return temp

def subByteForMatrix(matrix):
    answer = copy.deepcopy(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            answer[row][column] = SboxLookup(matrix[row][column])
            
    return answer

def shiftRows(matrix):
    answer = copy.deepcopy(matrix)
    
    for row in range(1,len(answer)):
        for shifts in range(row):
            temp = answer[row][0]
            for i in range(len(answer[0])-1):
                answer[row][i] = answer[row][i+1]
            answer[row][len(answer[0])-1] = temp
    
    return answer
   
def shiftleftMixColumns(binaryIn,num=1):
    binary = binaryIn
    temp = ""
    for numShifts in range(num):
        for j in range(1,len(binary)):
            temp = temp + binary[j]
        temp = temp + "0"
        binary = temp
        temp = ""

    return binary

def mixColumns(matrix):
    mixColMatrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    
    answer = copy.deepcopy(matrix)

    irreducible = "00011011"
    
    for columnMaster in range(4):
        for rowMaster in range(4):    
            rowSlave = rowMaster
            accumulation = "00000000"
            for i in range(4):
                multiplier = mixColMatrix[rowSlave][i]
                
                if multiplier == 1:
                    accumulation = xor(accumulation,matrix[i][columnMaster])
                elif multiplier == 2:    
                    if matrix[i][columnMaster][0] == '0':
                        temp = shiftleftMixColumns(matrix[i][columnMaster])
                    elif matrix[i][columnMaster][0] == '1':
                        temp = shiftleftMixColumns(matrix[i][columnMaster])
                        temp = xor(temp,irreducible)                                 #NBNB NB NB NB As die fixed polinomial verander, verander dit hier
                    accumulation = xor(accumulation,temp)
                elif multiplier == 3:
                    if matrix[i][columnMaster][0] == '0':
                        temp = shiftleftMixColumns(matrix[i][columnMaster])
                    elif matrix[i][columnMaster][0] == '1':
                        temp = shiftleftMixColumns(matrix[i][columnMaster])
                        temp = xor(temp,irreducible)
                    #Multiply with the value itself:
                    temp = xor(temp,matrix[i][columnMaster])
                    accumulation = xor(accumulation,temp)
                    
            #Add the result to its place:
            answer[rowMaster][columnMaster] = accumulation
            
    return answer
                    
            
###############################################################################
#                           AES Algorithm
###############################################################################
    
#SOURCE:
#Used the example at https://kavaliro.com/wp-content/uploads/2014/03/AES.pdf to test


#AES input:
key = hexToBinary("5468617473206D79204B756E67204675",128)

plaintext = hexToBinary("54776F204F6E65204E696E652054776F",128)

ciphertext = ""
    
###############################################################################
#                           KEY GENERATION
###############################################################################

#print(SboxLookup(hexToBinary("95")))
#print(hexToBinary("95"))
#print(functionG("10101010"*4))
#print(hexToBinary("67204675"))
#print(functionG(hexToBinary("7F8D292F"),8))

#Add original key to subkeys:
subkeys = []
subkeys.append(key[0:32])
subkeys.append(key[32:64])
subkeys.append(key[64:96])
subkeys.append(key[96:128])

#We have the first 4 keys, calculate 5+
index = 4

while index <= 43:
    if index % 4 == 0:
        subkeys.append(xor(subkeys[index-4],functionG(subkeys[index-1], (index // 4) - 1)))
    else:
        subkeys.append(xor(subkeys[index-4],subkeys[index-1]))
    index += 1

#subkeysHex = []
#for i in range(len(subkeys)):
#    subkeysHex.append(binaryToHex(subkeys[i]))
#print(subkeysHex)

###############################################################################
#                           ENCRYPTION
###############################################################################

#Initial addroundkey:
#get matrix:

status = generateMatrix(plaintext)
#first long key:
subkeyTemp = subkeys[0] + subkeys[1] + subkeys[2] + subkeys[3]
subkeyTemp = generateMatrix(subkeyTemp)

status = xorMatrix(status,subkeyTemp)

keyIndex = 4

for roundNum in range(10):
    #Substitute bytes:
    status = subByteForMatrix(status)
    #ShiftRows:
    status = shiftRows(status)
    #Mix columns, note no mixcolumns at last round
    if not(roundNum == 9):
        status = mixColumns(status)
    #Add roundkey
    subkeyTemp = subkeys[keyIndex] + subkeys[keyIndex+1] + subkeys[keyIndex+2] + subkeys[keyIndex+3]
    keyIndex += 4
    subkeyTemp = generateMatrix(subkeyTemp)

    status = xorMatrix(status,subkeyTemp)

print("Status matrix:")
printMatrix(status)

#Translate this back to one long ciphertext
ciphertext = ""
for column in range(4):
    for row in range(4):
        ciphertext = ciphertext + status[row][column]

print("Resulting ciphertext (bin): " + str(ciphertext))
print("Resulting ciphertext (hex): " + str(binaryToHex(ciphertext)))