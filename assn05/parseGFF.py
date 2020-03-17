#! /usr/bin/env python3

my_data = open("watermelon.gbf", "r")
List_of_Genes = []
for row in my_data:
    if "gene=" in row:
        item = row.split("=", 1)
        item = item[1].rstrip()
        item = item.strip("\"")
        if item in List_of_Genes:
            print(item, "was already found")
        else:
            List_of_Genes.append(item)
            print(item, "was added to List of the Genes")
my_data.close()
List_of_Genes.sort()
print(List_of_Genes)
