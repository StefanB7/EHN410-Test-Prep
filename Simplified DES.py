#Stefan Buys
#EHN 410 - Toets voorbereiding
#DES Algoritme vir Toetse
#April 2021

import numpy as np

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


###############################################################################
#                           S-BOXES DEFINE
###############################################################################

S0 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

S1 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

S2 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]


###############################################################################
#                   SIMPLIFIED DES ALGORITME BEGIN
###############################################################################



###############################################################################
#                           ENCRYPTION
###############################################################################
    
#10-bit key:
key = "1100011110"
keyPermuteP10 = [3,5,2,7,4,10,1,9,8,6]
keyPermuteP8 = [6,3,7,4,8,5,10,9]

#8-bit plaintext
plaintext = "00101000" #plaintext was: 00101000
plaintextPermuteIP = [2,6,3,1,4,8,5,7]

#### KEY GENERATION ##########################
subkey = ['1']*2
permutedKeyP10 = permutation(keyPermuteP10,key,1)

leftHalfKey = permutedKeyP10[0:5]
rightHalfKey = permutedKeyP10[5:10]

#Calculating subkey 1
leftHalfKeyLS1 = shiftLeft(leftHalfKey,1)
rightHalfKeyLS1 = shiftLeft(rightHalfKey,1)
subkey1 = leftHalfKeyLS1 + rightHalfKeyLS1

subkey1 = permutation(keyPermuteP8,subkey1,1)
subkey[0] = subkey1

#Calculating subkey 2
leftHalfKeyLS2 = shiftLeft(leftHalfKey,3)
rightHalfKeyLS2 = shiftLeft(rightHalfKey,3)
subkey2 = leftHalfKeyLS2 + rightHalfKeyLS2

subkey2 = permutation(keyPermuteP8,subkey2,1)
subkey[1] = subkey2

#NBNBNB Uncomment for encryption:

#NBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNB

#Uncomment for decryption

#For decryption:
#subKeyTemp = subkey
#subkey = []
#for i in range(len(subKeyTemp)-1,-1,-1):
#    subkey.append(subKeyTemp[i])


#NBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNBNB


################################################

#Perform the initial permutation:
plaintextPerm = permutation(plaintextPermuteIP,plaintext,1)

LHS = plaintextPerm[0:4]
RHS = plaintextPerm[4:8]

EP = [4,1,2,3,2,3,4,1]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

#Do the mapping F:
RHSexpandedPermuted = permutation(EP,RHS,1)
RHSexpandedPermuted = xor(RHSexpandedPermuted,subkey[0])
RHSleftbit = sLookupSimplified(S0,RHSexpandedPermuted[0:4])
RHSleftbit = RHSleftbit + sLookupSimplified(S1,RHSexpandedPermuted[4:8])

P4 = [2,4,3,1]
Foutput = permutation(P4,RHSleftbit,1)

Stage1out = xor(LHS,Foutput) + RHS

#########################################

Switch = Stage1out[4:8] + Stage1out[0:4]

#########################################

LHS = Switch[0:4]
RHS = Switch[4:8]

EP = [4,1,2,3,2,3,4,1]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

#Do the mapping F:
RHSexpandedPermuted = permutation(EP,RHS,1)
RHSexpandedPermuted = xor(RHSexpandedPermuted,subkey[1])
RHSleftbit = sLookupSimplified(S0,RHSexpandedPermuted[0:4])
RHSleftbit = RHSleftbit + sLookupSimplified(S1,RHSexpandedPermuted[4:8])

P4 = [2,4,3,1]
Foutput = permutation(P4,RHSleftbit,1)

Stage2out = xor(LHS,Foutput) + RHS

#######################################
invIP = [4,1,3,5,7,2,8,6]

ciphertext = permutation(invIP,Stage2out,1)

print(ciphertext)    