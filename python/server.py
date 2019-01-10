#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 18:22:02
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import socket

flag = True

# 生成socket对象
server = socket.socket()

# 绑定ip和端口
server.bind(('localhost', 6666))

# 监听绑定的端口
server.listen()

# 方便识别打印一个我在等待
print("I'm waiting the connect...")


# 这里用两个值接受，因为链接上之后使用的是客户端发来请求的这个实例
# 所以下面的传输要使用conn实例操作
conn, addr = server.accept()

# 打印链接成功
print('Connect success!')

# 进入循环
while flag:

    # 接受数据并赋给data
    data = conn.recv(1024).decode()

    # 判断
    if data != 'q':

        # 打印收到数据
        print('收到：', data)

        # 发送我收到数据了
        conn.send('Send Successed!'.encode())

    else:

        # 条件为False
        flag = False

# 关闭socket链接
server.close()

