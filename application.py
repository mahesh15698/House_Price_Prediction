from flask import Flask
from Housing.logger import logging
from Housing.exception import HousingException
import sys
application = Flask(__name__)
app = application


@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "Starting House Prediction Project"

if __name__ == '__main__':
    app.run(debug=True)