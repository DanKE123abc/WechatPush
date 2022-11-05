import requests
import json
import os

#Another: DanKe

__version__ = "0.1.5"

def version():
    print("WechatPush " + __version__)

def checksetting():
    try:
        import setting
    except:
        print("setting.py not found")
        if os.path.exists("setting.py") == False:
            newsetting = "#--------------------wechatpush-----------------------"+"\n\n"+"APPID = ''"+"\n"+"APPSECRET = ''"
            f = open("setting.py", 'w')
            f.write(newsetting)
            f.close()
            print("setting.py is created. Please re run it after configuration")
            exit()

def push_text(openid,message):
    access_token = AccessToken().get_access_token()
    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    result = response.json()
    print(result)

def push_textcard(templateid,openid,message,url=""):
    access_token = AccessToken().get_access_token()
    body = {
        "touser":openid,
        "template_id":templateid,
        "url":url,
        "topcolor":"#FF0000",
        "data": message
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    result = response.json()
    print(result)

def push_url(openid, url="https://weixin.qq.com/",label="点击查看链接",message=""):#微信推送
    access_token = AccessToken().get_access_token()
    if message=="":
        msg = message + "<a href='"+ url +"'>"+label+"</a>"
    else:
        msg = message +"\n"+ "<a href='"+ url +"'>"+label+"</a>"
    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    result = response.json()
    print(result)

def push_voice(openid,message,person=0,volume=2):
    msg = message
    seconds = int(len(msg)/4)
    if seconds <= 60:
        url = "https://tts.baidu.com/text2audio?tex="+msg+"&cuid=baike&lan=ZH&ie=utf-8&ctp=1&pdt=301&vol="+str(volume)+"&rate=32&per="+str(person)
        push_url(openid,url,label='◁ '+ str(seconds) + '" ' + " "*seconds)

class AccessToken(object):
    checksetting()
    try:
        import setting
        APPID = setting.APPID
        APPSECRET = setting.APPSECRET
    except:
        print("appid or appsecret not found")
    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:
       # 获取access_token凭证
       # :return: access_token
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)

def help():
    print("Hello WechatPush"+__version__+" !")
    print(" __      __              .__            __ __________             .__   ")         
    print("/  \    /  \ ____   ____ |  |__ _____ _/  |\______   \__ __  _____|  |__  ")
    print("\   \/\/   // __ \_/ ___\|  |  \\\\__  \\\\   __\     ___/  |  \/  ___/  |  \ ")
    print(" \        /\  ___/\  \___|   Y  \/ __ \|  | |    |   |  |  /\___ \|   Y  \\")
    print("  \__/\  /  \___  >\___  >___|  (____  /__| |____|   |____//____  >___|  /")
    print("       \/       \/     \/     \/     \/                         \/     \/ ")
    print("Python微信公众号/订阅号/测试号推送库")
    print("Website: http://WechatPush.DanKe.ml")
    print("Github: http://github.com/DanKE123abc/WechatPush")
    print("Another: DanKe (http://github.com/DanKE123abc)")
    print("LICENSE: MIT")

def main():
  help()

if __name__ == '__main__':
    main()