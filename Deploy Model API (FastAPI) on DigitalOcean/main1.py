# 1. Library imports
import pandas as pd
from sklearn.linear_model import RidgeClassifier
import pickle
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

# 3. Load trained Pipeline
model = pickle.load(open('RidgeClassifier.sav', 'rb'))

# 4. Test Server


@app.get('/')
def get_root():
    return "Server start!"

# 5. Define predict function:


@app.post('/predict')
def predict(b, c, d, e, f, g, h, i):
    # create data frame
    raw = [{'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i}]
    data = pd.DataFrame(data=raw)
    # predictions
    predictions = model.predict(data)
    return {'prediction': int(predictions[0])}
