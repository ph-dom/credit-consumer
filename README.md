# mac/linux
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip3 install -r requirements.txt
    $ export FLASK_APP=credit-consumer
    $ export FLASK_ENV=development
    $ flask run
    $ deactivate

# windows (powershell)
    > py -3 -m venv venv
    > venv\Scripts\activate
    > pip install -r requirements.txt
    > $env:FLASK_APP = "credit-consumer"
    > $env:FLASK_ENV = "development"
    > flask run
    > deactivate

# for new packages
    pip freeze > requirements.txt