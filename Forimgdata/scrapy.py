#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-26 18:34:00
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import requests
import json
def getdata(index):
    a=input("调用gedata方法")
    print("正在抓取{index}页数据")
    payload = {"pageIndex":index,
            "pageSize":700,
            "relativeOffset":50,
            "frontCategoryId":400000001295013,
            "searchTimeType":-1,
            "orderType":50,
            "priceType":-1,
            "activityId":0,
            "keyword":""
    }
    print(type(payload))
    payload = json.dumps(payload)
    print(type(payload))
    headers = {"Accept":"application/json",
               "Host":"study.163.com",
               "Origin":"https://study.163.com",
               "Content-Type":"application/json",
               "Referer":"https://study.163.com/courses",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
    print(type(headers))
    req = requests.post("https://study.163.com/p/search/studycourse.json",data=payload,headers=headers)
    e=input("成功post到数据")
    print(type(req))
    res_json = json.loads(req.text)
    print(type(res_json))
    with open("wangyiPublic.json","w") as f:
        json.dump(res_json,f)
        print("写入文件完成...")
    
a=getdata(1)
b=input("运行到了这")