from aplicaciotion1.models import PredictionRequest
from aplication_utils.utils import get_model,transform_to_dataframes


model = None
def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, prediction)