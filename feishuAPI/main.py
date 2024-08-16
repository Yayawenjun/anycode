#!/usr/bin/env python

# -- coding: utf-8 --
# @Time : 2024/8/15 17:51
# @Author : junwen Liu
# @Site : 
# @File : main.py
# @Email   : junwenLiu0201@126.com
# @Software: PyCharm
from feishu import FeiShuTalkChatBot


feishu = FeiShuTalkChatBot(webhook="XXX")   #你的飞书机器人的key
#具体的使用方法在feishu.py，可选参数message，title，ats
feishu.success( message=f"""hello world""") #发送成功状态
feishu.error(message="123")                 #失败的提示