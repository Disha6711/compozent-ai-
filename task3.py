import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
from flask import Flask, request, jsonify, render_template

# Step 1: Load dataset
data = pd.read_csv('housing_prices.csv')

# Step 2: Prepare the dataset
X = data[['sqft_living', 'bedrooms', 'bathrooms']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train a regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Root Mean Squared Error: {rmse}')

# Step 5: Export the model
with open('regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Step 6: Create a Flask API
app = Flask(__name__)

# Load the trained model
with open('regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = loaded_model.predict([features])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'Predicted Price: ${output}')

if __name__ == '__main__':
    app.run(debug=True)


frontend_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>House Price Prediction</title>
</head>
<body>
    <h1>House Price Prediction</h1>
    <form action="/predict" method="post">
        <label for="sqft_living">Square Feet Living:</label>
        <input type="text" id="sqft_living" name="sqft_living"><br><br>
        <label for="bedrooms">Bedrooms:</label>
        <input type="text" id="bedrooms" name="bedrooms"><br><br>
        <label for="bathrooms">Bathrooms:</label>
        <input type="text" id="bathrooms" name="bathrooms"><br><br>
        <input type="submit" value="Predict">
    </form>
    <h2>{{ prediction_text }}</h2>
</body>
</html>
'''

with open('templates/index.html', 'w') as f:
    f.write(frontend_code)
