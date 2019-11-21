import json
import os
import urllib
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable

line_bot_api = LineBotApi(os.environ['ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    data = {
        "apikey": "YOUR_API_KEY",
        "query": event.message.text,
    }

    data = urllib.parse.urlencode(data).encode("utf-8")
    with urllib.request.urlopen("https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk", data=data) as res:
        # response = res.read().decode("utf-8")
        reply_json = json.loads(res.read().decode("unicode_escape"))

        if reply_json['status'] == 0:
            reply = reply_json['results'][0]['reply']
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply))


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port ] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)

# import os
#
# from flask import Flask, request, abort
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
#
# app = Flask(__name__)
#
# line_bot_api = LineBotApi(os.environ['ACCESS_TOKEN'])
# handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
#
#
# @app.route('/')
# def index():
#     return 'You call index()'
#
#
# @app.route('/push_sample')
# def push_sample():
#     """プッシュメッセージを送る"""
#     user_id = os.environ['USER_ID']
#     line_bot_api.push_message(user_id, TextSendMessage(text='Hello World!'))
#
#     return 'OK'
#
#
# @app.route('/callback', methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)
#     app.logger.info('Request body: ' + body)
#
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError as e:
#         abort(400)
#
#     return 'OK'
#
#
# # @handler.add(MessageEvent, message=TextMessage)
# # def handle_message(event):
# #     line_bot_api.reply_message(event.reply_token,
# #                                TextSendMessage(text=event.message.text))\
#
#
#
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(event.reply_token,
#                                StickerSendMessage(package_id='11537', sticker_id='52002735'))
#
#
# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
