# this file trains the data and saves the predictions in new file
import pandas as pd
import numpy as np 
from ast import literal_eval
df= pd.read_pickle('/Users/chavishaarora/Desktop/dataready2.pkl')
binary=np.array(list(map(np.array, df['Binary'])))
interactive=np.array(list(map(np.array, df['Interactive'])))
print(binary.shape)
print(interactive.shape)
print(interactive[0])
print(type(interactive[0]))

print('Starting')
from sklearn import svm
classifier = svm.SVC(C=4.0,gamma=0.001,class_weight='balanced')
classifier.fit(binary,interactive)

print('trained successfully')

test=pd.read_csv('/Users/chavishaarora/Downloads/test1.txt')

L=17
AddingX='X'*int((L-1)/2)

residues=''
for i in test['Lable']:
    residues=residues+i

numofresidues=len(residues)
residues=AddingX+residues+AddingX

X_test=[]
for i in range(numofresidues):
    peptide=residues[i:i+17]
    peptidedf=  (pd.DataFrame(np.zeros((L, 21)))).astype(int)
    peptidedf.rename(columns={0:'A',1:'C',2:'D',3:'E',4:'F',5:'G',6:'H',7:'I',8:'K',9:'L',10:'M',11:'N',12:'P',13:'Q',14:'R',15:'S',16:'T',17:'V',18:'W',19:'Y',20:'X'}, inplace=True)
    for k in range(L):
        peptidedf.at[k,(peptide[k]).upper()]=1
    binaryofpeptide=[]
    for itera in range(L):
        binaryofpeptide=binaryofpeptide+(peptidedf.iloc[itera,:]).tolist()
    X_test.append(binaryofpeptide)

X_test=np.array(X_test)
print(X_test.shape)
estimate=classifier.predict(X_test)

predictions=pd.DataFrame({'ID':test.ID, 'Lable':estimate})
predictions.to_csv('/Users/chavishaarora/Desktop/Predictions.csv',index=False)
