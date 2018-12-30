#coding=utf-8
import itchat,time
import matplotlib.pyplot as plt

itchat.login()
#微信好友男女比例分析
friends=itchat.get_friends(update=True)[0:]

male=female=other=0 
for i in friends[1:]:
	sex=i["Sex"]
	if sex==1:
		male+=1
	elif sex==2:
		female+=1 
	else:other+=1 

total=len(friends[1:])
print("男性好友: %.2f%%"%(float(male)/total*100)+"\n"
	+ "女性好友: %.2f%%"%(float(female)/total*100)+"\n"
	+ "性别不明:  %.2f%%"%(float(other)/total*100))

print "好友数量: ",male+female+other
print "男性好友: ",male
print "女性好友: ",female
print "性别不明: ",other

labels="male","female","other"
sizes=[(float(male)/total*100),(float(female)/total*100),(float(other)/total*100)]
colors=['yellowgreen','gold','lightskyblue']
explode=(0,0.1,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()

#微信好友信息获取

"""import itchat as it
it.login()
friends=it.get_friends(update=True)[0:]
print(type(friends))
#性别
dict_sex=dict()
dict_sex[0]=0#未知
dict_sex[1]=0#男
dict_sex[2]=0#女
#省份
dict_province=dict()
for user in friends:
    print()
    print('user.NickName:',user.NickName)
    print('user.Sex:', user.Sex)
    print('user.City:', user.City)
    print('user.Signature:',user.Signature)
    print('user.Province:', user.Province)
    dict_sex[user.Sex] = dict_sex[user.Sex] + 1
    if dict_province.keys().__contains__(user.Province):
        dict_province[user.Province]=dict_province[user.Province]+1
    else:
        dict_province[user.Province]=1
#性别统计结果
print('none:',dict_sex[0])
print('male:',dict_sex[1])
print('female:',dict_sex[2])
#省份统计结果
print(dict_province)

#出去特殊字符
import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace('span','').replace('class','').replace('emoji','').replace('\n','')
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
#分词
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)
print(word_space_split)
#绘制词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("/home/guo/图片/1.jpg"))#自定义词云的图片
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42,font_path='/home/guo/.fonts/AvantGarde_LT_Medium.ttf',scale=2).generate(word_space_split)#wget http://labfile.oss.aliyuncs.com/courses/756/DroidSansFallbackFull.ttf中文字符文件

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
"""






