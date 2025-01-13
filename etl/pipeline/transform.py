import pandas as pd
from sklearn.preprocessing import RobustScaler


def transform_data(data):
    rob_scaler = RobustScaler()
    data['scaled_amount'] = rob_scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
    data['scaled_time'] = rob_scaler.fit_transform(data['Time'].values.reshape(-1, 1))

    data.drop(['Time', 'Amount'], axis=1, inplace=True)
    scaled_amount = data['scaled_amount']
    scaled_time = data['scaled_time']
    
    data.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
    data.insert(0, 'scaled_amount', scaled_amount)
    data.insert(1, 'scaled_time', scaled_time)
    
    return data