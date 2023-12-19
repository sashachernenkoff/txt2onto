import pandas as pd

df = pd.read_csv('CrossValidatedModels.txt', sep='\t', header=None)

names = df.iloc[:,0]

with open('output_input.txt', 'w') as file:
    # Iterate through the list of strings
    for name in names:
        # Append ".txt" to each string and write to the file
        file.write('python3.11 input.py --ont ' + name + ' --out ../training_inputs/\n')

names_output = [name.replace(':', '-') for name in names]

with open('output_train.txt', 'w') as file:
    # Iterate through the list of strings
    for name in names_output:
        # Append ".txt" to each string and write to the file
        file.write('python3.11 train.py --input ../training_inputs/' + name + '_NLP-ML-input.txt --out ../user_trained_models/\n')