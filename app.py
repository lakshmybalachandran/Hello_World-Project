# WEB API WRAPPER

from Console_app_main import Helloworld

from flask import Flask, jsonify, request

app = Flask("__name__")

@app.route('/', methods = ['GET', 'POST'])

def home():

 obj = Helloworld()
     
 if (request.method == 'POST'):
  post_json = request.get_json()
  return jsonify({'you sent':post_json})

 else:
  result = obj.do_helloworld() # Get Function
  return(result)


if __name__ == '__main__':
 app.run(debug=True)


