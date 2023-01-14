#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='校園位置在這裡呦~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/o0yFe73.png",
                    action=URITemplateAction(
                        label="處室",
                        uri="https://i.imgur.com/o0yFe73.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Mqapuwb.png",
                    action=URITemplateAction(
                        label="學餐",
                        uri="https://i.imgur.com/Mqapuwb.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/KXTqJND.png",
                    action=URITemplateAction(
                        label="大樓",
                        uri="https://i.imgur.com/KXTqJND.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/jTE7qhD.png",
                    action=URITemplateAction(
                        label="ATM",
                        uri="https://i.imgur.com/jTE7qhD.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/6MWL98Z.png",
                    action=URITemplateAction(
                        label="地圖",
                        uri="https://i.imgur.com/6MWL98Z.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/FwDCGV5.png",
                    action=URITemplateAction(
                        label="郵局",
                        uri="https://i.imgur.com/FwDCGV5.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/D6ILoUg.png",
                    action=URITemplateAction(
                        label="公車站牌",
                        uri="https://i.imgur.com/D6ILoUg.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/STLcnNo.png",
                    action=URITemplateAction(
                        label="老師辦公室",
                        uri="https://i.imgur.com/STLcnNo.png"
                    )
                )
            ]
        )
    )
    return message