'''
Author: your name
Date: 2021-02-20 19:22:44
LastEditTime: 2021-02-20 19:46:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonAPI\gun.py
'''
# gunicorn 并不支持windows，只能在linux 上跑
import os 
import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing

# 服务地址（adderes:port） 
bind = 0.0.0.0:5000 
# 启动进程数量
workers = multiprocessing.cpu_count() * 2 +1
worker_class = 'gevent'
threads = 20
preload_app = True
reload = True
x_forwarded_for_header = 'X_FORWARDED-FOR'