<div align="center">
    <h1>Gemstone Price Prediction</h1>
</div>

## Description
The **Gemstone Price Prediction** project leverages machine learning techniques to predict the prices of gemstones based on various attributes. This project demonstrates the integration of **MLOps** tools and practices for building scalable and reproducible machine learning pipelines.  

## Key Features
- **Data Version Control (DVC):** Tracks dataset changes and ensures version control for reproducibility.  
- **MLflow:** Monitors and manages machine learning experiments, logging metrics and parameters.  
- **Apache Airflow:** Orchestrates workflows for automation and pipeline scheduling.  
- **Docker & Docker Compose:** Containerizes the application to ensure consistent deployment across different environments.  


## Demo
🚨This instance will spin down with inactivity, which can delay requests by 50 seconds or more

https://gemstone-price-prediction-flask.onrender.com/
## Screenshots

**Home Page**  
![Home Page](/images/home.jpeg)

**Data Table View**  
![Data Table](/images/table.jpeg)

**Price Prediction Output**  
![Prediction](/images/prediction.jpeg)

## Tech Stack

**Client:** Scikit-Learn , Seaborn , Numpy, MLflow, DVC , Pandas , Docker

**Server:** Flask

## Run Locally:

Clone the repository:

```bash
git clone https://github.com/suyash-04/Gemstone_Price_Prediction
cd Gemstone_Price_Prediction

```
Create virtual envirnment:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

Install required packages :
```bash
pip install -r requirements_dev.txt
```

Run the flask server:
```bash
python3 app.py
```
## Setup DVC

Initialize DVC and pull the dataset:
```bash
dvc init
dvc pull
dvc add  /exprimentsdata/raw_data.csv
dvc commit
```

## Track Experiments with MLflow
Install the project with npm:

```bash
mlflow ui
```
Access the MLflow UI at http://localhost:5000.

## Run With Docker
-**Build and run containers with Docker Compose:**
```bash
docker-compose up --build
```
This command will build the Docker image and run all the services defined in the docker-compose.yml file.

-**Access the Application:**
Once the containers are up and running, the Flask app will be available at http://localhost:80. 

And the airflow ui will be available at http://http://localhost:8080

## Access Apache-Airflow UI
If you're using  **Apache Airflow**  for orchestrating your pipelines, you can access the Airflow UI to monitor workflows:

1.**Start the Airflow Scheduler and Web Server** (if not using Docker Compose):
```bash
airflow db init
airflow scheduler -D
airflow webserver -D
```
2.**Access Airflow UI*:

Once the Airflow services are running, open the Airflow UI at:
```arduino
http://localhost:8080
```
2.**Login to Airflow UI**:
The default login credentials are:

**Username**: admin

**Password**: admin

**⚠️ Note: If you’re using Docker Compose, the Airflow UI will be available at http://localhost:8080 as well. Ensure you have the correct configurations in your docker-compose.yml file to enable the Airflow webserver and scheduler.**

## Contributing

Contributions are always welcome!  

1. Fork the repository.  
2. Create your feature branch: `git checkout -b feature-name`.  
3. Commit changes: `git commit -m "Add new feature"`.  
4. Push to the branch: `git push origin feature-name`.  
5. Submit a pull request.


## Contact

For any inquiries or feedback, reach out to us:

- **Email**: [suyashadhikari04@gmail.com]
- **Social Media**: [http://tiny.cc/suyashlinkedin]

We look forward to hearing from you!

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details on terms and conditions.

Feel free to use and contribute to the project under these terms!

