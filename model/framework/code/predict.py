# """Loads a trained chemprop model checkpoint and makes predictions on a dataset."""
# import os, sys
# import chemprop.train
# #from chemprop.train import chemprop_predict
# from chemprop.args import PredictArgs

# #intermediate features file created
# root = os.path.dirname(os.path.abspath(__file__))
# features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
# checkpoint_dir = os.path.abspath(os.path.join(root,"..", "..","checkpoints", "model6"))
# #features_file = sys.argv[-1]

# # arguments = [
# #     '--test_path', 'test_checkpoints_transfer/fold_0/test_smiles.csv',
# #     '--preds_path', 'test_preds_transfer.csv',
# #     '--checkpoint_dir', 'test_checkpoints_transfer',
# # ]

# # args = chemprop.args.PredictArgs().parse_args(arguments)
# # preds = chemprop.train.make_predictions(args=args)

# if __name__ == '__main__':
#     print("Now predicting")
#     chemprop_predict(checkpoint_path='', features_path='features.npz')
#     print("Done predicting")
    
# # if __name__ == '__main__':
# #     print("Now predicting")
# #     chemprop.train.make_predictions(checkpoint_dir, features_file)
# #     print("Done predicting")
# #     os.remove(features_file)

import os, sys
from chemprop.train import chemprop_predict
from chemprop.args import PredictArgs

if __name__ == '__main__':
    print("Now predicting")

    # Specify the path to the pretrained model checkpoint
    root = os.path.dirname(os.path.abspath(__file__))
    checkpoint_path = os.path.abspath(os.path.join(root,"..", "..","checkpoints", "model6"))  # Replace with the actual path

    # Specify the path to the computed features file
    features_file =  os.path.abspath(os.path.join(root, "..","features.npz"))
    features_path = features_file  # Replace with the actual path

    # Create PredictArgs object with specified arguments
    predict_args = PredictArgs(
        checkpoint_path=checkpoint_path,
        features_path=features_path,
        preds_path='predictions.csv',  # Specify the desired path for predictions
    )

    # Make predictions using chemprop_predict function
    chemprop_predict(args=predict_args)

    print("Done predicting")

