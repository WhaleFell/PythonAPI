'''
Author: your name
Date: 2021-02-20 19:22:44
LastEditTime: 2021-02-20 20:26:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonAPI\gun.py
'''
# gunicorn 并不支持windows，只能在linux 上跑
bind = "0.0.0.0:5000" #绑定的ip端口号 
backlog = 512 #监听队列 
timeout = 30 #超时 
worker_class = "gevent" #使用gevent模式，还可以使用sync 模式，默认的是sync模式 
workers = 4 #进程数
threads = 16 #指定每个进程开启的线程数