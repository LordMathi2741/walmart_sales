from modules.modules import st
from helper.encoder import encode_data
from helper.pandas import load_data, clean_data
from modules.modules import ms
from modules.modules import pd
from modules.modules import jb
from modules.modules import sm


model = st.DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

dataset = load_data()
dataset = clean_data(dataset)
dataset = encode_data(dataset)


features = dataset.drop(columns=['Weekly_Sales', 'Store','Unemployment'])
label = dataset['Weekly_Sales']

X_train, X_test, y_train, y_test = ms.train_test_split(
    features, 
    label,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(sm.mean_squared_error(y_test, prediction))
jb.dump(model, 'train/sales_model.joblib')


