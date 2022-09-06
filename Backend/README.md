# Instruction to Run and Execute

## After cloning the repository

### SetUp

1. First of install virtualenv in conda environment using command : conda install virtualenv
2. create virtual environment using the command : virtualenv venv --python=python3.8
3. Activate the virtual env using the command : source venv/bin/activate
4. Install the required library
   Method - 1 : using the command : pip install flask flask_RESTful flask-JWT flask_sqlalchemy
   Method - 2 : using the requirement.txt file : pip install -r requirement.txt
### Execution

1. Move to code folder
2. Open the terminal and run the app.py file using the command : python app.py
3. Then go to postman and make the relevent queries as per resources mentioned in app.py
