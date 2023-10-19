from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_validate
import numpy as np
from data_cleaning import *
X = full_movie_data.drop(['worldwide_gross'], axis = 1)
y = full_movie_data['worldwide_gross']

pipeline = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
    ('core_model', GradientBoostingRegressor())
])

results = cross_validate(pipeline ,X,y,return_train_score=True,cv=10)
results


train_score = np.mean(results['train_score'])
test_score = np.mean(results['test_score'])
assert train_score > 0.7
assert test_score > 0.65
print(f'Train Score: {train_score}')
print(f'Test Score: {test_score}')