from modules.modules import sp

def encode_data(dataset):
    label_encoder = sp.LabelEncoder()
    dataset['Date'] = label_encoder.fit_transform(dataset['Date'])
    return dataset