import pandas as pd
dataset = pd.read_excel('Dry_Bean_Dataset.xlsx')
dataset.head(5)

X = dataset.iloc[:, [0,1,2,3,4]].values
y = dataset.iloc[:, -1].values

print(X)

def klasifikasi(x):
    classes = None
    if x == 1:
        classes = 'SEKER'
    elif x== 2:
        classes = 'BARBUNYA'
    elif x== 3:
        classes = 'BOMBAY'
    elif x== 4:
        classes = 'CALI'
    elif x== 5:
        classes = 'HOROZ'  
    elif x== 6:
        classes = 'SIRA'
    else :
        classes = 'DERMASON'
    return classes

