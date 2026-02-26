from modules.modules import pd
def load_data():
    dataset = pd.read_csv('dataset/Walmart_Sales.csv')
    return dataset

def clean_data(dataset):
    dataset = dataset.dropna()
    return dataset