"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
from chemprop.train import chemprop_predict
from chemprop.args import PredictArgs

#intermediate features file created
root = os.path.dirname(os.path.abspath(__file__))
features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
#features_file = sys.argv[-1]

def run_chemprop_prediction():
    # Setting the path to my checkpoint directory
    checkpoint_dir = os.path.abspath(os.path.join(root,"..", "..","checkpoints", "model6"))

    # Create PredictArgs to configure prediction arguments
    predict_args = PredictArgs()
    predict_args.checkpoint_dir = checkpoint_dir

    # Run chemprop prediction with the specified arguments
    chemprop_predict(args=predict_args)

if __name__ == '__main__':
    print("Now predicting")
    run_chemprop_prediction()
    print("Done predicting")
    os.remove(features_file)
