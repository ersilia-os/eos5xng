"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
from chemprop.train import chemprop_predict

#intermediate features file created
root = os.path.dirname(os.path.abspath(__file__))
features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
#features_file = sys.argv[-1]

if __name__ == '__main__':
    print("now predicting")
    chemprop_predict()
    #Remove intermediate features file after making predictions
    print("done predicting")
    os.remove(features_file)
