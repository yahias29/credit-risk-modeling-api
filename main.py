from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialisation de l'API FastAPI
app = FastAPI(title="API de Prédiction du Risque de Crédit", version="1.0")

# 2. Chargement du modèle au démarrage de l'application
# Le modèle est chargé une seule fois pour plus d'efficacité.
final_model = joblib.load("models/final_model.pkl")

# 3. Définition du format des données d'entrée avec Pydantic
# C'est ici qu'on définit toutes les caractéristiques qu'un client doit avoir.
# FastAPI validera automatiquement que les données reçues correspondent à ce format.
class ClientInfo(BaseModel):
    ID: int
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float
    # On ne met pas ID_CLIENT car il n'est pas utilisé pour la prédiction

# 4. Définition de l'endpoint de prédiction
@app.post("/predict")
def predict(client_info: ClientInfo):
    """
    Prédit la probabilité de défaut de paiement pour un client.
    """
    # Convertir les données d'entrée en DataFrame pandas
    input_data = pd.DataFrame([client_info.dict()])

    # Obtenir la prédiction de probabilité (on veut la probabilité de la classe 1 'Défaut')
    prediction_proba = final_model.predict_proba(input_data)[:, 1]

    # Formater la réponse
    return {
        "probabilite_de_defaut": float(prediction_proba)
    }

# Endpoint racine pour vérifier que l'API est en ligne
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction du risque de crédit"}