"""
https://rosalind.info/problems/rna/

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
 """



with open('rosalind_rna.txt', 'r') as file:
  DNA_string =file.read().strip()

RNA_string = ""

for i in DNA_string:
  if i == "T":
    RNA_string += "U"
  else:
    RNA_string += i



print(RNA_string)
