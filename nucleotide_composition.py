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
print("Percent A = " + str(round(A_content,2)) + " %")
T_content = (T_number/dna_length) * 100
print("Percent T = " + str(round(T_content,2)) + " %")
C_content = (C_number/dna_length) * 100
print("Percent C = " + str(round(C_content,2)) + " %")
G_content = (G_number/dna_length) * 100
print("Percent G = " + str(round(G_content,2)) + " %")

#After running the above script; we get the following result;
#ACTGTAcGTGCAcTGaTC
#The Uppercase DNA sequence is as follow: 
#ACTGTACGTGCACTGATC
#Percent A = 22.22 %
#Percent T = 27.78 %
#Percent C = 27.78 %
#Percent G = 22.22 %
