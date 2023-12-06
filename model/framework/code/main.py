# # imports
# import os
# import csv
# import sys
# from rdkit import Chem
# from rdkit.Chem.Descriptors import MolWt

# # parse arguments
# input_file = sys.argv[1]
# output_file = sys.argv[2]

# # current file directory
# root = os.path.dirname(os.path.abspath(__file__))

# # my model
# def my_model(smiles_list):
#     return [MolWt(Chem.MolFromSmiles(smi)) for smi in smiles_list]


# # read SMILES from .csv file, assuming one column with header
# with open(input_file, "r") as f:
#     reader = csv.reader(f)
#     next(reader)  # skip header
#     smiles_list = [r[0] for r in reader]

# # run model
# outputs = my_model(smiles_list)

# #check input and output have the same lenght
# input_len = len(smiles_list)
# output_len = len(outputs)
# assert input_len == output_len

# # write output in a .csv file
# with open(output_file, "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["value"])  # header
#     for o in outputs:
#         writer.writerow([o])



#First Possible solution
import os
import csv
import sys
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
import torch

# Parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Current file directory
root = os.path.dirname(os.path.abspath(__file__))

# Function to load pretrained model and make predictions
def load_and_predict(model_path, smiles_list):
    # Load the pretrained model
    model = torch.load(model_path, map_location=torch.device('cpu'))
    model.eval()  # Set the model to evaluation mode

    # Run predictions for each SMILES
    predictions = [MolWt(Chem.MolFromSmiles(smi)) for smi in smiles_list]

    return predictions

# Read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    smiles_list = [r[0] for r in reader]

# Get a list of model files in the "checkpoints" directory
checkpoints_dir = os.path.join(root, "checkpoints")
model_files = [f for f in os.listdir(checkpoints_dir) if f.endswith(".pt")]

# Iterate through each model and make predictions
all_predictions = []
for model_file in model_files:
    model_path = os.path.join(checkpoints_dir, model_file)
    predictions = load_and_predict(model_path, smiles_list)
    all_predictions.append(predictions)

# Transpose the list of predictions to have one row per model
all_predictions_transposed = list(map(list, zip(*all_predictions)))

# Write output to a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    # Header with model names
    writer.writerow(["Model_" + os.path.splitext(model)[0] for model in model_files])
    # Write predictions
    for row in all_predictions_transposed:
        writer.writerow(row)
