#!/usr/bin/env python
# coding: utf-8

# # 8.1 DNA 프로젝트
# ## 파이썬으로 DNA 데이터 열고 가공하기

# In[1]:


#p134
f = open("NM_207618.2.fasta", "r")
sequence = f.read()
sequence


# In[2]:


#p135
with open("NM_207618.2.fasta", "r") as inf:
    data = inf.read().splitlines(True)
with open('dna1.txt', 'w') as outf:
    outf.writelines(data[1:])
f = open("dna1.txt", "r")
sequence = f.read()
sequence


# In[3]:


#p136
print(sequence)


# In[4]:


#p137
sequence = sequence.replace('\n', '')    # "\n"를 공란으로 대체
sequence


# In[5]:


sequence = sequence.replace('\r', '')


# In[6]:


sequence = sequence.replace(' ', '')


# In[7]:


sequence[0:3]


# ## DNA를 아미노산으로 변환하는 알고리즘

# In[8]:


#p138
genetic_code = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}


# In[9]:


genetic_code['ATA']


# In[10]:


#p139
def read_seq(inputfile):
    with open(inputfile, 'r') as f:
        sequence = f.read()
    sequence = sequence.replace(' ', '')
    sequence = sequence.replace('\n', '')
    sequence = sequence.replace('\r', '')
    return sequence
with open('NM_207618.2.fasta', 'r') as inf:
    data = inf.read().splitlines(True)
with open('dna.txt', 'w') as outf:
    outf.writelines(data[1:])
dna = read_seq('dna.txt')
print(dna)


# In[11]:

print('-----------')

#p140
def convert(seq):
    """DNA 시퀀스를 아미노산 시퀀스로 변환!"""
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    if len(seq) % 3 == 0: # 데이터의 길이가 3의 배수이면 아래를 실행!
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += genetic_code[codon]
    return protein
print(convert(dna[20:941]))




# In[12]:


#p141
# print(convert(dna[20:935]))


# In[13]:


prot = read_seq('protein.txt')
# print(prot)


# In[14]:


prot == convert(dna[20:935])


# In[ ]:




