'''
=========================================================================
|pa01 - encrypting a plaintext file using the Hill Cipher
|
|   Author: Luis Cabral
|   Language: Python 3
|   To compile: not necessary
|   To execute: python3 PA1.py
|   Note:
|       All input files are simple 8 bit ASCII input
| 
================================================
'''
import numpy as np
import sys
import string

arg1 = sys.argv[1]
arg2 = sys.argv[2]
#opens and prints first argument file and reads all data
with open(arg1, 'r') as f:
   data = f.readlines()
   keyMatrixSize = int(data[0])
   keyMatrix = np.array([list(map(int, line.strip().split())) for line in data[1:]])
   print('Key Matrix: \n')
   print(keyMatrix)
   

#opens second argument file and reads all the data 
with open(arg2, 'r') as f2:  
   plaintext = f2.read().lower()
   plaintext = ''.join(char for char in plaintext if char.isalpha())
   print('\nPlaintext: \n')
   for i in range(0, len(plaintext), 80):
      print(plaintext[i:i+80])

#function to encrypt
def encrypt(plaintext, keyMatrix):
   
   ciphertextNumbers = []
   #number of rows needed for key matrix
   numRows = len(plaintext) // keyMatrixSize
   #if the length of the string cannot be broken down evenly with no remainder, then pad with X
   if len(plaintext) % keyMatrixSize != 0:
      numRows += 1
   paddingLength = numRows * keyMatrixSize - len(plaintext)
   plaintext += 'x' * paddingLength
   #convert letters to numbers
   letters_to_nums = [ord(char) - ord('a') for char in plaintext]
   #break plaintext down into blocks of key matrix size
   blocks = [letters_to_nums[i:i+keyMatrixSize]for i in range(0, len(plaintext), keyMatrixSize)]
   for block in blocks:
      blockMatrix = np.array(block)
      blockMatrix = blockMatrix.reshape((keyMatrixSize, -1))
      encryptedBlock = np.dot(keyMatrix, blockMatrix) % 26
      ciphertextNumbers.extend(encryptedBlock.flatten())
   #convert back ciphertext to letters
   ciphertext = ''.join(chr(num + ord('a'))for num in ciphertextNumbers)
   print('\nCiphertext: \n')
   for i in range(0, len(ciphertext), 80):
      print(ciphertext[i:i+80])

encrypt(plaintext, keyMatrix)