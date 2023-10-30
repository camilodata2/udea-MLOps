from fastapi import APIRouter
from aplicaciotion1.models import PredictionRequest,PredictionResponse
from aplicatio_view.views import get_prediction

predicion_de_modelo=APIRouter()

@predicion_de_modelo.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    return response(worldwide_gross=get_prediction(request))