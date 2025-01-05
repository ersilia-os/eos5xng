# imports
import os
import csv
import sys
import subprocess
import tempfile 

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]


# current file directory
root = os.path.dirname(os.path.abspath(__file__))

#checkpoints
dir_model= os.path.abspath(os.path.join(root,"..","..","checkpoints"))

#scripts
generate_features_= os.path.join(root, "Scripts/save_features.py")
predict_= os.path.join(root, "Scripts/predict.py")

#features
tmp_folder = tempfile.mktemp(prefix="ersilia-")
features_path = os.path.join(tmp_folder, "features.npz")  
temp_ouput = os.path.join(tmp_folder, "output.csv")  

# commands to run model
def my_model():   
    cmd1 = 'python {} --data_path {} --save_path {} --features_generator rdkit_2d_normalized'.format(generate_features_,input_file,features_path)
    subprocess.Popen(cmd1, shell=True).wait() 
    cmd2 = 'python {} --no_features_scaling --test_path {} --checkpoint_dir {} --preds_path {} --features_path {}'.format(predict_, input_file, dir_model, temp_ouput, features_path)
    subprocess.Popen(cmd2, shell=True).wait()

 
# run model  
my_model() #this will return the output file from the chemprop model, saved in temp_output


#read the temp output, so that only predictions column is saved in the ouput file
with open(temp_ouput, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    outputs = [r[1] for r in reader] 

# write output in a .csv file (outputfile)
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["bcenocepacia_inhibition"])  # header
    for o in outputs:
        writer.writerow([o])
