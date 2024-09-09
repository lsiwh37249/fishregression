from fastapi import FastAPI
import requests

app = FastAPI()


def lr_api(l):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
    }

    response = requests.get('http://localhost:8001/get_weight', params=params, headers=headers)    
    j = response.json()
    r = j.get("weight")
    return r

def knn_api(l,w,n):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        'weight': w,
        'neighbor': n,
    }

    response = requests.get('http://localhost:8002/fish', params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    return r

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/predict")
def predict():
    length =3

    neighbor = 5

    # weight 예측 선형회귀 API 호출
    weight = lr_api(length)
    
    # 물고기 분류 API 호출
    fish_class = knn_api(length, weight, neighbor)

    print(f"length:{length} 물고기는 weight:{weight} 으로 예측되며 종류는 {fish_class}입니다")
