#! /bin/bash

#assn03-1
for string in {808..8008}
do
echo "TR-"$string
done


#assn03-2
# make alias for "ls -al" so that we can do ls -al just by pressing l key only instead of typing the full command 'ls -al'; as follow:
alias l="ls -al"

# make another alias for showing the current directory, instead 'pwd', we can just use p, as follow:
alias p="pwd"

#assn03-3
find . -name "*.fasta" | wc -l

#assn03-4
find . -name "*.tre" | wc -l

#assn03-5
find . -name "*.sched" | wc -l

#assn03-6
ls gene_trees/ | grep .fasta | cut -d "_" -f1 > All_FASTA.fasta
ls gene_trees/ | grep .tre | cut -d "_" -f1 > All_TRE.fasta 
comm -32 All_FASTA.fasta All_TRE.fasta | wc -l



#assn03-7
for file in *.sched
do
    if grep -q "Program Return Code: 0" $file; 
then
        echo exists
    else
        echo not found
    fi
done > result.txt

grep "not found" result.txt | wc -l

grep "not found" -v result.txt | wc -l



#assn03-8
comm -32 All_FASTA.fasta All_TRE.fasta > Only_Fasta.fasta
while read file; do
    echo "write_raxml_job_script.py ${file}_alignment.fasta > ${file}_alignment.pbs" 
done < Only_Fasta.fasta






