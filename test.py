import os
from src.utils.utils import load_object
preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
preprocessor = load_object(preprocessor_path)

import pandas as pd

# Example input data
input_data = {
    'carat': [0.23],
    'depth': [61.5],
    'table': [57.0],
    'x': [3.95],
    'y': [3.98],
    'z': [2.43],
    'cut': ['Ideal'],
    'color': ['G'],
    'clarity': ['VS1']
}

# Convert to DataFrame
features = pd.DataFrame(input_data)
transformed_features = preprocessor.transform(features)

# Print transformed features
print(transformed_features)
model_path = os.path.join('artifacts', 'model.pkl')
model = load_object(model_path)

# Make a prediction
predictions = model.predict(transformed_features)
print(predictions)