import numpy as np
from flask import Flask, request, make_response
import json
import pickle
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import cross_origin

app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))

@app.route('/')
def hello():
    print('this is logging appplication')
    return 'Hello World'

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
	
    result = req.get("queryResult")

    #app.logger.info('logged in successfully')

    intent = result.get("intent").get('displayName')
	
	#log.write_log(sessionID, "Bot Says: "+intent)
    
    if (intent=='final'):
	
	owner = result.get("outputContexts")[1].get("parameters").get("owner")
	dealer = result.get("outputContexts")[1].get("parameters").get("dealer")
	modelyear= result.get("outputContexts")[1].get("parameters").get("modelyear")
	price= result.get("outputContexts")[1].get("parameters").get("price")
	kilometer= result.get("outputContexts")[1].get("parameters").get("kilometer")
	fueltype= result.get("outputContexts")[1].get("parameters").get("fueltype")
	
	print ('owner is ' + owner )
	#parameters = result.get("queryResult").get(outputContexts[0])
	print('inside final')
	print 
        fulfillmentText= "The is working"
        #log.write_log(se
	ssionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
		
    #user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    Petal_length=parameters.get("number")
    Petal_width = parameters.get("number1")
    Sepal_length=parameters.get("number2")
    Sepal_width=parameters.get("number3")
    int_features = [Petal_length,Petal_width,Sepal_length,Sepal_width]
    
    final_features = [np.array(int_features)]
	 
    intent = result.get("intent").get('displayName')
    
    if (intent=='irisdata'):
        prediction = model.predict(final_features)
    
        output = round(prediction[0], 2)
    
    	
        if(output==0):
            flowr = 'Setosa'
    
        if(output==1):
            flowr = 'Versicolour'
        
        if(output==2):
            flowr = 'Virginica'
       
        fulfillmentText= "The Iris type seems to be..  {} !".format(flowr)
        #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
	       
if __name__ == '__main__':
    app.run()
#if __name__ == '__main__':
#    port = int(os.getenv('PORT', 5000))
#    print("Starting app on port %d" % port)
#    app.run(debug=False, port=port, host='0.0.0.0')
