from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    code = request.values.get('Body', None)
    code = code.replace(" ", "")
    response = requests.get("https://naviator.herokuapp.com/?code=" + str(code))
    if response == 200:
        msg = response.json()['payload'].rstrip()
    else:
        if response == 404:
            msg = "You have submitted an invalid airport code, please try again."
        else:
            msg = "We are facing difficulties processing your request at the moment. Sorry for the inconvenience."
    resp = MessagingResponse()
    resp.message = msg
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
