from modules.modules import jb
from modules.modules import pd
from helper.encoder import encode_data

model = jb.load('train/sales_model.joblib')
input = pd.DataFrame({
    'Date': ['2009-02-05'],      
    'Holiday_Flag': [False],      
    'Temperature': [30.0],        
    'Fuel_Price': [2.666],       
    'CPI': [205.940],            
})

input = encode_data(input)

prediction = model.predict(input)
weekly_sales = prediction[0]
print(f'Las ventas semanales son: $ {weekly_sales:.2f}')