from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import *

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if event.message.text=='Buyer':
            line_bot_api.reply_message(
                event.reply_token,
                    ImagemapSendMessage(
                        base_url='https://stu-web.tkucs.cc/404411091/linebot/ButtonBuy/1040.png?_ignored=',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=520, width=1040),
                        actions=[
                            URIImagemapAction(
                                link_uri='https://youtube.com/',
                                area=ImagemapArea(
                                    x=0, y=0, width=520, height=520
                                )
                            ),
                            MessageImagemapAction(
                                text='hello',
                                area=ImagemapArea(
                                    x=520, y=0, width=520, height=520
                                )
                            )
                        ]
                    )
            )
            continue
        elif event.message.text=='Seller':
            line_bot_api.reply_message(
                event.reply_token,
                    ImagemapSendMessage(
                        base_url='https://stu-web.tkucs.cc/404411091/linebot/ButtonSell/1040.png?_ignored=',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=520, width=1040),
                        actions=[
                            URIImagemapAction(
                                link_uri='https://youtube.com/',
                                area=ImagemapArea(
                                    x=0, y=0, width=520, height=520
                                )
                            ),
                            MessageImagemapAction(
                                text='hello',
                                area=ImagemapArea(
                                    x=520, y=0, width=520, height=520
                                )
                            )
                        ]
                    )
            )
            continue
        elif event.message.text=='no1':
            line_bot_api.reply_message(
                event.reply_token,
                    ImagemapSendMessage(
                        base_url='https://stu-web.tkucs.cc/404411091/linebot/Change/260.png?_ignored=',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=260, width=1040),
                        actions=[
                            MessageImagemapAction(
                                text='商品名',
                                area=ImagemapArea(
                                    x=0, y=0, width=346, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='單價',
                                area=ImagemapArea(
                                    x=347, y=0, width=346, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='數量',
                                area=ImagemapArea(
                                    x=694, y=0, width=346, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='介紹及優惠',
                                area=ImagemapArea(
                                    x=0, y=130, width=520, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='取消更改',
                                area=ImagemapArea(
                                    x=520, y=130, width=520, height=130
                                )
                            )
                        ]
                    )
            )
            continue
        elif event.message.text=='no2':
            line_bot_api.reply_message(
                event.reply_token,
                    ImagemapSendMessage(
                        base_url='https://stu-web.tkucs.cc/404411091/linebot/Change/130.png?_ignored=',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=130, width=1040),
                        actions=[
                            MessageImagemapAction(
                                text='商品',
                                area=ImagemapArea(
                                    x=0, y=0, width=346, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='數量',
                                area=ImagemapArea(
                                    x=347, y=0, width=346, height=130
                                )
                            ),
                            MessageImagemapAction(
                                text='取消更改',
                                area=ImagemapArea(
                                    x=694, y=0, width=346, height=130
                                )
                            )
                        ]
                    )
            )
        
    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()
    app.run(debug=options.debug, port=options.port)
