echo [$(date)] : "Start"


sudo  apt install python3.11-venv

echo [$(date)] : "creating env with python"

python3 -m venv venv 

echo [$(date)] : "activating the environment"

source venv/bin/activate

echo [$(date)] : "installing the required packages"

pip install -r requirements_dev.txt

echo [$(date)] : "End"