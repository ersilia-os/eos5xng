python $1/code/save_features.py --data_path $2 --save_path TEMP_Feat --features_generator rdkit_2d_normalized
python $1/code/predict.py --no_features_scaling --test_path $2 --checkpoint_dir  $1/../checkpoints --preds_path $3 --features_path TEMP_Feat.npz
