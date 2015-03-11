import sys
import csv


prot_names=list()
prot_len=list()
sequence=list()

f = open('ProtSeq.csv', 'rt')

reader = csv.reader(f)
your_list = list(reader)

for i in range(1,len(your_list)): #skip the first one
    prot_names = prot_names+[your_list[i][0]]
    prot_len   = prot_len+[your_list[i][1]]
    sequence   = sequence+[your_list[i][2]]

# print prot_names[0]
# print prot_len[2]
# print sequence[0]

f.close()