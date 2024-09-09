from fastapi import FastAPI
import requests
from fishregression.model.manager import get_model_path
import pickle
app = FastAPI()

def get_model():
    path = get_model_path()
    print(f" path :{path}")
    with open(path, "rb") as f:
        fish_model = pickle.load(f)
    return fish_model

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/get_weight")
def get_weight(length: float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """


    fish_model = get_model()
    weight = fish_model.predict([[length**2, length]])[0]

    return {
                "length": length,
                "weight": weight
            }
