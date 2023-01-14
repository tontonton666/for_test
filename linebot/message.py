#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/VDNOUZH.jpeg",
        alt_text='靜宜大學校門',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://goo.gl/maps/nQcac2C4FmiRvy9R7",
                area=ImagemapArea(
                    x=0, y=0, width=2000, height=2000
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='校園資訊在這裡喔~',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/zpZGMcV.png",
            title="校園資訊",
            text="你在尋找什麼~?",
            actions=[
                URITemplateAction(
                    label="行事曆",
                    uri="https://secretary.pu.edu.tw/var/file/45/1045/img/11102.pdf"
                ),
                URITemplateAction(
                    label="網站",
                    uri="https://alcat.pu.edu.tw/"
                ),MessageTemplateAction(
                    label="位置",
                    text="詳細位置"
                )
                
                # PostbackTemplateAction(
                #     label='營業時間',
                #     text='周一~周五 08:00-17:00',
                #     data='營業時間'
                # ),
                # PostbackTemplateAction(
                #     label='聯絡方式',
                #     text='04-26328001',
                #     data='聯絡方式'
                # )
            ]
        )
    )
    return message



#關於LINEBOT聊天內容範例