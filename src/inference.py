import pickle
from URLFeatureExtraction import featureExtraction
import numpy as np
import path
import sys
import os

dir = path.Path(__file__).abspath()
print("Current working directory is:",dir)
print(sys.path.append(dir.parent))
pwd = os.getcwd()
print(pwd)

# print(os.path.join("/XGBoostClassifier.pickle.dat"))

def inference(url):
    loaded_model = pickle.load(open(os.path.join("XGBoostClassifier.pickle.dat"), "rb"))
    features = featureExtraction(url)
    predictions_probability = loaded_model.predict_proba(np.array([features]))
    prediction = loaded_model.predict(np.array([features]))   
    
    return features,predictions_probability,prediction
     

if __name__ == "__main__":
    f = inference("google.com")
    print(f)