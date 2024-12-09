from flask import Flask , render_template , jsonify, request 


from src.pipeline.prediction_pipeline import PredictPipeline , CustomData


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"]) # type: ignore
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else :
        data = CustomData(
            carat = float(request.form.get('carat')), # type: ignore
            depth = float(request.form.get('depth')), # type: ignore 
            table = float(request.form.get('table')), # type: ignore
            x = float(request.form.get('x')), # type: ignore 
            y = float(request.form.get('y')), # type: ignore
            z = float(request.form.get('z')), # type: ignore
            cut =request.form.get('cut'), # type: ignore
            color =request.form.get('color'), # type: ignore
            clarity = request.form.get('clarity') # type: ignore
        )
    final_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    predict = predict_pipeline.predict(final_data)
    
    result = round(predict[0],2)
    
    return render_template("result.html", final_result = result)

if __name__ == "__main__":
    app.run(debug=True)
