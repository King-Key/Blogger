#coding=utf8
import requests
import itchat
import time
import pyttsx3 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

engine = pyttsx3.init()

#中文播放
engine.setProperty('voice','zh')


#语速控制
rate = engine.getProperty('voice')
engine.setProperty('rate', rate)

volume=engine.getProperty('volume')
print("volume:",volume)
engine.setProperty('volume',1.0)




KEY = '8edce3ce905a4c1dbb965e6b35c3834d'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # global exec_count
    # exec_count+=1
    # if exec_count<60 ||msg==None:

    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        print msg['FromUserName']
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        engine.say("先生,您的好友")
        engine.say(msg['User']['NickName'])
        print(u"发件人:"+msg['User']['NickName'])
        engine.say("发来消息")
        engine.say(msg['Text'])
        print(u"消息:"+msg['Text'])
        engine.runAndWait()



        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
    
"""itchat.auto_login(hotReload=True)
itchat.run()"""
