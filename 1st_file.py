#   This file does the work of creating the data which can be trained.
import pandas as pd
import numpy as np 
df= pd.read_csv('/Users/chavishaarora/Downloads/train.data')
print(df)
L=17
AddingX='X'*int((L-1)/2)
finaldata=pd.DataFrame(columns=['Binary','Interactive'])
for i in df['Amino Acid Sequence']:
    numofnucleotides=len(i)
    print('length of protein sequence is- '+str(numofnucleotides))
    i=AddingX+i+AddingX
    for j in range(int(numofnucleotides)):
        peptide=i[j:j+17]
        ATPinteracting=peptide[8:9].islower()
        peptidedf=  (pd.DataFrame(np.zeros((L, 21)))).astype(int)
        peptidedf.rename(columns={0:'A',1:'C',2:'D',3:'E',4:'F',5:'G',6:'H',7:'I',8:'K',9:'L',10:'M',11:'N',12:'P',13:'Q',14:'R',15:'S',16:'T',17:'V',18:'W',19:'Y',20:'X'}, inplace=True)
        for k in range(L):
            peptidedf.at[k,(peptide[k]).upper()]=1
        binaryofpeptide=[]
        for itera in range(L):
            binaryofpeptide=binaryofpeptide+(peptidedf.iloc[itera,:]).tolist()
        finaldata=finaldata.append({'Binary':binaryofpeptide,'Interactive':ATPinteracting},ignore_index=True)
        
print(finaldata)
finaldata.to_pickle('/Users/chavishaarora/Desktop/dataready2.pkl')

# peptide='XXXXXXXXVNIKTNPfk'
# peptidedf=  (pd.DataFrame(np.zeros((L, 21)))).astype(int)
# peptidedf.rename(columns={0:'A',1:'C',2:'D',3:'E',4:'F',5:'G',6:'H',7:'I',8:'K',9:'L',10:'M',11:'N',12:'P',13:'Q',14:'R',15:'S',16:'T',17:'V',18:'W',19:'Y',20:'X'}, inplace=True)
# for k in range(L):
#     peptidedf.at[k,(peptide[k]).upper()]=1
# print(peptidedf)
# binaryofpeptide=[]
# print('type of binary is= '+str(type(binaryofpeptide)))
# for i in range(L):
#     print((peptidedf.iloc[i,:]).tolist())
#     binaryofpeptide=binaryofpeptide+(peptidedf.iloc[i,:]).tolist()

# print(binaryofpeptide)
# print('type of binary is= '+str(type(binaryofpeptide)))
# finaldata=finaldata.append({'Binary':binaryofpeptide,'Interactive':False},ignore_index=True)
# print(finaldata)
# - ACDEFGHIKLMNPQRSTVWYX
# X
# X
# X
# X
# X
# X
# X
# X
# V
# N
# I
# K
# T
# N
# P
# f
# k
