from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import sys
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/')
def new():
    try:
        raise Exception("We are testing custon exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info('We are testing the logging module')
    return 'Hello World Changed'

if __name__ == '__main__':
    app.run()