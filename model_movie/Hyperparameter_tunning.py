from sklearn.model_selection import GridSearchCV
from modeling import *

param_tunning = {'core_model__n_estimators': range(20,501,20)} 

estimator = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
    ('core_model', GradientBoostingRegressor())
])

grid_search= GridSearchCV(estimator,
                       param_grid = param_tunning,
                       scoring='r2',
                       cv=5) 

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.35,random_state= 42)


grid_search.fit(X_train, y_train)

final_result = cross_validate(grid_search.best_estimator_,X_train,y_train,return_train_score=True,cv=7)

train_score = np.mean(final_result['train_score'])
test_score = np.mean(final_result['test_score'])
assert train_score > 0.7
assert test_score > 0.65
print(f'Train Score: {train_score}')
print(f'Test Score: {test_score}')

grid_search.best_estimator_.get_params()


