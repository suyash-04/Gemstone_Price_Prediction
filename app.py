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
            carat = float(request.form.get('carat')) # type: ignore
            depth = float(request.form.get('depth')) # type: ignore # type: ignore
            table = float(request.form.get('table')) # type: ignore # type: ignore
            x = float(request.form.get('x')) # type: ignore
            y = float(request.form.get('y')) # type: ignore
            z = float(request.form.get('z')) # type: ignore # type: ignore
            cut = request.form.get('cut')
            color = request.form.get('color')
            clarity = request.form.get('clarity')

            # Check for missing values
            if not all([carat, depth, table, x, y, z, cut, color, clarity]):
                return "Missing values in form data", 400

            # Prepare data for prediction
            data = CustomData(
                carat=carat,
                depth=depth,
                table=table,
                x=x,
                y=y,
                z=z,
                cut=cut, # type: ignore
                color=color, # type: ignore
                clarity=clarity # type: ignore
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
    app.run(host="0.0.0.0", port=80, debug=True)
