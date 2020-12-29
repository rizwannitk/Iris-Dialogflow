import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin

app = Flask(__name__)
#model = pickle.load(open('rf.pkl', 'rb'))

@app.route('/')
def hello():
    return 'Hello World'



if __name__ == '__main__':
    app.run()
#if __name__ == '__main__':
#    port = int(os.getenv('PORT', 5000))
#    print("Starting app on port %d" % port)
#    app.run(debug=False, port=port, host='0.0.0.0')
