from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        try:
            # Get form data and ensure proper conversion to float
            carat = float(request.form.get('carat', 0))  # Default to 0 if not provided
            depth = float(request.form.get('depth', 0))
            table = float(request.form.get('table', 0))
            x = float(request.form.get('x', 0))
            y = float(request.form.get('y', 0))
            z = float(request.form.get('z', 0))
            cut = request.form.get('cut', '')
            color = request.form.get('color', '')
            clarity = request.form.get('clarity', '')

            # Check for missing values
            if not all([carat, depth, table, x, y, z, cut, color, clarity]) or "" in [carat, depth, table, x, y, z, cut, color, clarity]:
                return "Missing values in form data", 400

            # Prepare data for prediction
            data = CustomData(
                carat=carat,
                depth=depth,
                table=table,
                x=x,
                y=y,
                z=z,
                cut=cut,
                color=color,
                clarity=clarity
            )
            final_data = data.get_data_as_dataframe()

            # Make prediction
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)

            # Return prediction result
            result = round(pred[0], 2)
            return render_template("result.html", final_result=result)

        except (ValueError, TypeError) as e:
            print(f"Error processing input: {e}")
            return "Invalid input data", 400

# Execution begins here
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
