"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
import os, sys
import chemprop.train
#from chemprop.train import chemprop_predict
from chemprop.args import PredictArgs

#intermediate features file created
root = os.path.dirname(os.path.abspath(__file__))
features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
checkpoint_dir = os.path.abspath(os.path.join(root,"..", "..","checkpoints", "model6"))
#features_file = sys.argv[-1]

# arguments = [
#     '--test_path', 'test_checkpoints_transfer/fold_0/test_smiles.csv',
#     '--preds_path', 'test_preds_transfer.csv',
#     '--checkpoint_dir', 'test_checkpoints_transfer',
# ]

# args = chemprop.args.PredictArgs().parse_args(arguments)
# preds = chemprop.train.make_predictions(args=args)

if __name__ == '__main__':
    print("Now predicting")
    chemprop.train.make_predictions(checkpoint_dir, features_file)
    print("Done predicting")
    os.remove(features_file)
