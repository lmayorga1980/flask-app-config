from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/dev/app123', methods = ['GET'])
def return_app123_dev():
    if(request.method == 'GET'):
        data = {
            "application_name" : "app123",
            "environment": "dev",
            "details": {
              "config1" : { 
                  "subconfig11": "val1",
                  "subconfig12": "val2",
              },
              "config2" : { 
                  "subconfig2": "val1",
                  "subconfig1": "val2", }
            }
        }
  
        return jsonify(data)

@app.route('/prod/app123', methods = ['GET'])
def return_app123_prod():
    if(request.method == 'GET'):
        data = {
            "application_name" : "app123",
            "environment": "prod",
            "details": {
              "config1" : { 
                  "subconfig11": "val1",
                  "subconfig12": "val2",
              },
              "config2" : { 
                  "subconfig2": "val1",
                  "subconfig1": "val2", }
            }
        }
  
        return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)
