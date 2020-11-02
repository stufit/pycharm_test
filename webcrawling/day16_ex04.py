# f = open('NM_207618.2.fasta','r')
# sequence = f.read()
# print(sequence)

print('------------------------------------')
#
# with open('NM_207618.2.fasta','r') as inputfile:
#     data = inputfile.read().splitlines(True)
# with open('protein.txt','w') as outputfile:
#     outputfile.writelines(data[1:])
# f= open('protein.txt','r')
# sequence = f.read()
# sequence = sequence.replace('\t','')
# print(sequence)
#
def read_seq(inputfile):
    with open(inputfile,'r') as f:
        sequence = f.read()
    sequence = sequence.replace(' ','')
    sequence = sequence.replace('\n','')
    sequence = sequence.replace('\r','')
    return sequence
with open('NM_207618.2.fasta','r') as inf:
    data = inf.read().splitlines(True)
with open('dna.txt','w') as outf:
    outf.writelines(data[1:])
dna =read_seq('dna.txt')
print(dna)
