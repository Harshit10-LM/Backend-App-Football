from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/products")
def index():
   return {
       "products": [
           {
               "title": "Bag",
           },
           {
               "title": "Mat",
           },
       ]
   }
app.run(port=5001, debug=True)