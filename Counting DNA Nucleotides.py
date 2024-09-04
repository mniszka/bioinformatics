# count how many nucleotides (A, T, C, G) are in the DNA sequence
# https://rosalind.info/problems/dna/

def count_nucleotides(dna_sequence):
  A = dna_sequence.count("A")
  T = dna_sequence.count("T")
  C = dna_sequence.count("C")
  G = dna_sequence.count("G")
  
  return A, T, C, G



if __name__ == "__main__":
  with open('rosalind.txt','r') as file:
    dna_sequence = file.read().strip()

  A, T, C, G = count_nucleotides(dna_sequence)
  print(f"A: {A}, T: {T}, C: {C}, G: {G}")


