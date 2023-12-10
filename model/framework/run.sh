python $1/code/save_features.py --data_path $2 --save_path 'features.npz' --features_generator rdkit_2d_normalized
python $1/code/predict.py --no_features_scaling --features_path 'features.npz' --test_path $2 --checkpoint_dir 'checkpoints/model6' $3 --preds_path '/code' $4


