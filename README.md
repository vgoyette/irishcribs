Irish Cribs

Created by:
Vincent Goyette
Alan Johnson
Jacques Charboneau
Jack Conway

instructions for running our project

1. login to db server as follows:
ssh -L PORT:localhost:PORT NETID@db.cse.nd.edu

2. create a virtual environment as follows:
python3 -m venv venv

3. enter virtual environment
source venv/bin/activate

4. install requirements
pip3 install -r requirements.txt

5. run the server!
python manage.py runserver PORT

6. access webpage by going to localhost:PORT in your browser
