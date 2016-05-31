from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.messages import TextMessage

from ..entry import app

import gscholar

conf = WechatConf(
        token= app.config['WXTOKEN'],
        appid= app.config['WXAPPID'],
        appsecret= app.config['WXSECRET'],
        encrypt_mode='normal',
        encoding_aes_key=app.config['AESKEY']
)


wc = WechatBasic(conf=conf)



def validate(signature,timestamp,nonce):
    return wc.check_signature(signature,timestamp,nonce) == 'Accept'


def process(dat):
    wc.parse_data(dat)

    if isinstance(wc.message, TextMessage):
        return wc.response_text(gscholar.google_scholar_query(wc.message.content))

    return "success"
