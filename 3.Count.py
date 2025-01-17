import os, math
import pandas as pd

# Specify the path to your Excel file
file_path = 'input/test_smiles_csv.csv'
# file_path = 'input/pubchem_D1.csv'

# Load the Excel file into a DataFrame
df = pd.read_csv(file_path)

def decode_text(text):
    rows = text.split('\n')
    del rows[0]
    
    res = []
    
    for row in rows:
        r = row.split(' ')
        del r[0]
        
        res.append(r)
        
    return res

max_columns = 300
columns = [i+1 for i in range(max_columns)]
smiles = []

# Iterate through each row using `iterrows()`
for index, row in df.iterrows():
    #print(f"Row {index}:")

    #counter_elem = dict.fromkeys(columns, 0)
    counter_elem = [0 for _ in range(max_columns)]
    
    id = row['CID']
    
    if math.isnan(id):
        continue
    else:
        id = int(id)
    
    if not os.path.exists('output/'+str(id)+'.txt'):
        continue

    with open('output/'+str(id)+'.txt', 'r') as file:
        txt = file.read().split('\n')[1:]
        for t in txt:
            values = t.split(' ')
            value = int(float(values[1]))
            cnt = int(values[2])

            counter_elem[value]+=cnt

    
    counter_elem.insert(0, id)
    smiles.append(counter_elem)

columns = [i for i in range(max_columns)]
columns.insert(0, 'CID')
dfo = pd.DataFrame(smiles, columns=columns)

# Save the DataFrame to an Excel file
excel_file_path = "output.csv"
dfo.to_csv(excel_file_path, index=False)

