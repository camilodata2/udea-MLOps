from fastapi import FastAPI
#from aplication.models import PredictionResponse
#from aplication.views import PredictionRequest
from models.PredictionResponse import PredictionResponse
from views.PredictionRequest import PredictionRequest
import sys
print(sys.path)


app = FastAPI(docs_url='/')
@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    return response(worldwide_gross=get_prediction(request))
