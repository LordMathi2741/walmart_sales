# Walmart Sales Prediction

Modelo de Machine Learning para predecir las ventas semanales de tiendas Walmart utilizando un árbol de decisión (Decision Tree Regressor).

## Descripción

Este proyecto implementa un sistema de predicción de ventas semanales basado en diversas características como la fecha, días festivos, temperatura, precio del combustible e índice de precios al consumidor (CPI).

## Estructura del Proyecto

```
Walmart-Sales/
├── app.py                      # Aplicación para realizar predicciones
├── train.py                    # Script de entrenamiento del modelo
├── dataset/
│   └── Walmart_Sales.csv       # Dataset de ventas de Walmart
├── helper/
│   ├── encoder.py              # Funciones de codificación de datos
│   └── pandas.py               # Funciones de carga y limpieza de datos
├── modules/
│   └── modules.py              # Importación centralizada de librerías
├── train/
│   └── sales_model.joblib      # Modelo entrenado
├── README.md
└── LICENSE
```

## Requisitos

- Python 3.8+
- pandas
- scikit-learn
- joblib

### Instalación de dependencias

```bash
pip install pandas scikit-learn joblib
```

## Uso

### Entrenar el modelo

```bash
python train.py
```

Esto entrenará un Decision Tree Regressor con los siguientes parámetros:
- `max_depth`: 5
- `random_state`: 42
- `test_size`: 20%

El modelo entrenado se guardará en `train/sales_model.joblib`.

### Realizar predicciones

```bash
python app.py
```

Para modificar los valores de entrada, edita el DataFrame en `app.py`:

```python
input = pd.DataFrame({
    'Date': ['2012-06-15'],      # Fecha (YYYY-MM-DD)
    'Holiday_Flag': [False],      # Día festivo (True/False)
    'Temperature': [75.0],        # Temperatura (°F)
    'Fuel_Price': [3.200],        # Precio del combustible (USD)
    'CPI': [215.500],             # Índice de precios al consumidor
})
```

## Dataset

El dataset `Walmart_Sales.csv` contiene las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| Store | Número de tienda |
| Date | Fecha de la semana |
| Weekly_Sales | Ventas semanales (variable objetivo) |
| Holiday_Flag | Indica si la semana incluye un día festivo |
| Temperature | Temperatura promedio de la región |
| Fuel_Price | Precio del combustible en la región |
| CPI | Índice de precios al consumidor |
| Unemployment | Tasa de desempleo |

## Modelo

Se utiliza un **Decision Tree Regressor** de scikit-learn debido a:

- Fácil interpretación
- Manejo de relaciones no lineales
- No requiere normalización de datos
- Buen rendimiento con datasets de tamaño medio

### Características utilizadas

- `Date` (codificada con LabelEncoder)
- `Holiday_Flag`
- `Temperature`
- `Fuel_Price`
- `CPI`

### Características excluidas

- `Store` - No relevante para predicción general
- `Unemployment` - Excluido del modelo actual

## Métricas

El modelo utiliza **Mean Squared Error (MSE)** para evaluar el rendimiento durante el entrenamiento.

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

Desarrollado como proyecto de aprendizaje supervisado.
