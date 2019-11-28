
import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselTemplate, \
    CarouselColumn, URIAction

import api
import scraping

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route('/')
def index():
    return 'You call index()'


@app.route('/push_sample')
def push_sample():
    """プッシュメッセージを送る"""
    user_id = os.environ['USER_ID']
    line_bot_api.push_message(user_id, TextSendMessage(text='Hello World!'))

    return 'OK'


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'foodword':
        url = api.recipe_search()
        rank = scraping.recipe_scraping(url)

        notes = [CarouselColumn(thumbnail_image_url=rank[0]['img'],
                                title=rank[0]['title'],
                                actions=[URIAction(label="CLICK!", uri=rank[0]['url'])]),

                 CarouselColumn(thumbnail_image_url=rank[1]['img'],
                                title=rank[1]['title'],
                                actions=[URIAction(label="CLICK!", uri=rank[1]['url'])]),

                 CarouselColumn(thumbnail_image_url=rank[2]['img'],
                                title=rank[2]['title'],
                                actions=[URIAction(label="CLICK!", uri=rank[2]['url'])]),
                 ]

        messages = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(columns=notes),
        )

        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(messages=messages))
    else:
        print('hoge')

    # push_text = event.message.text
    # msg = api.recipe_search(foodword=push_text)
    # line_bot_api.reply_message(event.reply_token,
    #                            TextSendMessage(text=msg))


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
