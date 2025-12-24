from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    medical_cost_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    medical_cost_model.fit(train_X, train_y)
    val_predictions = medical_cost_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    return val_mae