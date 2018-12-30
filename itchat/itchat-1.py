#9.1-wechat.py
#coding:utf-8
#爬取微信好友头像并进行拼接
import itchat
import math
import PIL.Image as Image
import os
#登录
itchat.auto_login(True) 
#获取好友信息
friends = itchat.get_friends(update=True)[0:]
#获取好友头像并保存在目录文件夹下
num = 0
for friend in friends:
    image = itchat.get_head_img(userName=friend["UserName"]) #用 itchat.get_head_img(userName=None)来爬取好友列表的头像
    fileImage = open("/home/guo/桌面/Work/chat/img/" + "/" + str(num) + ".jpg",'wb') #将好友头像下载到本地文件夹
    fileImage.write(image)
    fileImage.close()
    num += 1
#将微信图像进行拼接
dirs = os.listdir("/home/guo/桌面/Work/chat/img/")
each_size = int(math.sqrt(float(640*640)/len(dirs))) 
line = int(640.0/each_size) 
photographic = Image.new("RGB",(640,640))
x = 0
y = 0
for i in range(0,len(dirs)): 
    try:
        imageOfFriends = Image.open("/home/guo/桌面/Work/chat/img/" + "/" + str(i) + ".jpg") #打开一张照片，PIL库的应用
    except IOError:
        print "error"
    else:
        image_resize = imageOfFriends.resize((each_size,each_size)) 
        photographic.paste(image_resize,(x*each_size,y*each_size)) 
        x += 1
        if x == line:
            x = 0
            y += 1
#保存图像，发送给文件助手，显示图像
photographic.save("/home/guo/桌面/Work/chat/img/" + "/" + "all.jpg") 
itchat.send_image("/home/guo/桌面/Work/chat/img/" + "/" + "all.jpg","filehelper") #把图片发送给微信文件助手（filehelper
photographic.show()
