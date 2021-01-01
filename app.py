import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
	
    app.logger.info('inside webhook')

    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
	
    result = req.get("queryResult")

    log.write_log(sessionID, "Bot Says: hello ")

    intent = result.get("intent").get('displayName')
	
	log.write_log(sessionID, "Bot Says: "+intent)
    
    if (intent=='final'):
        fulfillmentText= "The is working"
        log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
		
    
	       
if __name__ == '__main__':
    app.run()
#if __name__ == '__main__':
#    port = int(os.getenv('PORT', 5000))
#    print("Starting app on port %d" % port)
#    app.run(debug=False, port=port, host='0.0.0.0')
