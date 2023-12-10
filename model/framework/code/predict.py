"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
import chemprop.train
from chemprop.train import chemprop_predict
from chemprop.args import PredictArgs

#intermediate features file created
root = os.path.dirname(os.path.abspath(__file__))
features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
checkpoint_dir = os.path.abspath(os.path.join(root,"..", "..","checkpoints", "model6"))
#features_file = sys.argv[-1]

if __name__ == '__main__':
    print("Now predicting")
    chemprop_predict()
    print("Done predicting")
    


