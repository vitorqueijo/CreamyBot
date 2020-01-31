import os
from flask import Flask, request, Response, render_template

import slack


app = Flask(__name__)

#TODO: criar upload de imagens do diretorios e dois "post's"
creamy_card = "https://i.imgur.com/0imXa5E.jpg"
creamy_pr = 'https://i.imgur.com/whRfZrN.jpg'

@app.route("/")
def main():
    return render_template('slack_form.html')

@app.route("/", methods=['POST'])
def push_to_slack():
    token_id = request.form['user_id']
    channel_id = request.form['channel_id']
    client = slack.WebClient(token=token_id)
    try:
        response = client.chat_postMessage(
                channel=channel_id,
                text="Revise os seus cards pelo Creamy",
                attachments=[{
                    "title": "Creamy",
                    "image_url": creamy_card
                    }],
                username='CreamyBot',
                icon_emoji=':nyancat:'
                )
        return Response(response)
    except Exception as e:
        return Response("Creamy has failed due to: {}".format(e))

if __name__ == "__main__":
    app.run(debug=True)
