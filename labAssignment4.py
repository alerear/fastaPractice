##!/usr/bin/env python

#this prints out everything in sequence.fasta without header
f = open("sequence.fasta")
lines = f.readlines()
seq = []
for i in range(0, len(lines)):
    seq.append(lines[i].rstrip("\n"))

print("ACCESSION #", seq[0]) #prints the accession number
header = seq[0]
PUC = seq[1:len(seq)]
PUC = "".join(PUC)

#print(PUC)

#split by restriction enzyme SMAI
splitseq = PUC.split("CCCGGG")
#print (splitseq)

x = open("insert.fasta") #open insert fasta file
fastaFile = x.readlines()
newSeq = []
for y in range(0, len(fastaFile)):
    newSeq.append(fastaFile[y].rstrip("\n"))

dna = newSeq[1:len(newSeq)]
dna = "".join(dna)
dna = dna.lower()

final = splitseq[0]+ "CCC" + dna + "GGG" + splitseq[1]

print(final)

with open('output.txt', 'w') as k:
    k.write(header)
    k.write(final)

f.close()
