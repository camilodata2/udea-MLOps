from Hyperparameter_tunning import estimator

estimator = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
    ('core_model', GradientBoostingRegressor(n_estimators=220,
                                             alpha=0.9,
                                             ccp_alpha=0.0,
                                             criterion='friedman_mse',
                                             init=None,
                                             learning_rate=0.1,
                                             loss='squared_error',
                                             max_depth=3,
                                             max_features=None,
                                             max_leaf_nodes=None,
                                             min_impurity_decrease=0.0,
                                             min_samples_leaf=1,
                                             min_samples_split=2,
                                             min_weight_fraction_leaf=0.0,
                                             n_iter_no_change=None,
                                             random_state=None,
                                             subsample=1.0,
                                             tol=0.0001,
                                             validation_fraction=0.1,
                                             verbose=0,
                                             warm_start=False))
])

estimator.fit(X_train,y_train)

estimator.score(X_test, y_test)