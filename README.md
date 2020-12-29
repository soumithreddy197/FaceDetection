# FaceDetection
python3 FaceDetector.py [data-directory] 
This command is used to generate results.json file by taking images present in the path provided in place of data-dictionary

python3 ComputeFBeta.py ./results.json [ground-truth.json]
This will compare the results.json file with the ground-truth.json and computes F1 score.
