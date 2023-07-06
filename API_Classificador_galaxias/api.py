import pickle

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class InputData(BaseModel):
    u: float
    r: float
    g: float
    i: float
    z: float
    deVAB_u: float
    deVAB_g: float
    deVAB_r: float
    deVAB_i: float
    deVAB_z: float
    mCr4_u: float
    mCr4_g: float
    mCr4_r: float
    mCr4_i: float
    mCr4_z: float
    petroR50_r: float
    petroR90_r: float
    petroR50_u: float
    petroR90_u: float
    petroR50_z: float
    petroR90_z: float

model = None

try:
    model = pickle.load(open('modelo-treinado-final000.pkl','rb'))
except Exception as e:
    print("Erro ao carregar  modelo:", str(e))

app = FastAPI()

@app.post("/classify")
def classify_galaxy(data: InputData):
    # Converter os dados de entrada em um array numpy
    data_eccentricity = (data.deVAB_u + data.deVAB_g + data.deVAB_r + data.deVAB_i + data.deVAB_z) / 5
    data_concentration_u = data.petroR50_u / data.petroR90_u
    data_concentration_r = data.petroR50_r / data.petroR90_r
    data_concentration_z = data.petroR50_z /data.petroR90_z
    data_u_g =data.u - data.g
    data_g_r = data.g - data.r
    data_r_i =data.r - data.i
    data_i_z = data.i - data.z
    data_mCr4_r = data.mCr4_r
    data_mCr4_g = data.mCr4_g
    data_mCr4_i = data.mCr4_i
    data_mCr4_z = data.mCr4_z
    data_mCr4_u = data.mCr4_u

    features = np.array([[data_eccentricity,data_concentration_u,data_concentration_r,data_concentration_z, data_u_g,data_g_r,data_r_i,data_i_z,data_mCr4_r,data_mCr4_g,data_mCr4_i,data_mCr4_z,data_mCr4_u]])

    # Fazer a previsão usando o modelo, se o modelo estiver carregado
    if model is not None:
        prediction = model.predict(features)[0]
        predicted_class = [prediction]
    else:
        predicted_class = 'Modelo não encontrado'

    return {"predicted_class": predicted_class}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
