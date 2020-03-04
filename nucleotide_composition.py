#! /usr/bin/env python3

my_file_name = "dna.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()
print(my_file_contents)
DNA_upper = my_file_contents.upper()
print("The Uppercase DNA sequence is as follow: \n" + DNA_upper)
dna_length = len(DNA_upper)
#print("Length of this DNA sequence = " + str(dna_length) + " bp")
A_number = DNA_upper.count('A')
#print("Numbers of A = " + str(A_number))
T_number = DNA_upper.count('T')
#print("Numbers of T = " + str(T_number))
C_number = DNA_upper.count('C')
#print("Numbers of C = " + str(C_number))
G_number = DNA_upper.count('G')
#print("Numbers of G = " + str(G_number))
A_content = (A_number/dna_length) * 100
print("Percent A = " + str(A_content) + " %")
T_content = (T_number/dna_length) * 100
print("Percent T = " + str(T_content) + " %")
C_content = (C_number/dna_length) * 100
print("Percent C = " + str(C_content) + " %")
G_content = (G_number/dna_length) * 100
print("Percent G = " + str(G_content) + " %")

