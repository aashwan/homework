#! /usr/bin/env python3

import argparse

import csv

parser = argparse.ArgumentParser()

parser.add_argument('gff')

parser.add_argument('fsa')

args = parser.parse_args()


with open(args.gff) as input:
    
    input.read = csv.reader(input, delimiter = "\t")
    
    List_of_Genes = []
    
    for line in input.read:
        
        print(line[8])

        



