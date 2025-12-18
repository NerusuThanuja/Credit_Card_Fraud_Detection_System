import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_fraud(input_data):
    """
    input_data: list of numeric values
    returns: 0 (Not Fraud) or 1 (Fraud)
    """
    data = np.array(input_data).reshape(1, -1)
    prob=model.predict_proba(data)[0][1]
    if prob>0.3:
        return 1
    else:
        return 0