from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

# curl -H "Content-Type: application/json" -X POST -d '{"stripeAmount":"11","stripeCurrency":"22","stripeToken":"sss","stripeDescription":"xxxx" }' http://localhost:5000/stripetest

@app.route('/reply', methods=["POST"])
def replyX():

    # This is a dummy list, 2 nested arrays containing some
    # params and values
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)


@app.route('/stripetest', methods=["POST"])
def stripeTest():

    if request.method == "POST":
        json_dict = request.get_json()

        stripeAmount = json_dict['stripeAmount']
        stripeCurrency = json_dict['stripeCurrency']
        stripeToken = json_dict['stripeToken']
        stripeDescription = json_dict['stripeDescription']

        data = {'stripeAmountRet': stripeAmount, 'stripeCurrencyRet': stripeCurrency, 'stripeTokenRet': stripeToken, 'stripeDescriptionRet': stripeDescription}
        return jsonify(data)
    else:

        return """<html><body>
        Something went horribly wrong
        </body></html>"""

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

