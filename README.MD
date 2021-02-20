# Python API合集
## 运行
- 建议使用`genvent`做协程，解决高并发
  > 注意:windowns平台不支持`genvent`
- 运行:
  ```shell
  gunicorn -c gun.py main:app # 使用genvent
  python3 main.py # 使用原生Python
  ```
- 设置为`systemclt`服务
  > 参考:[阮一峰老师的教程](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html)
  ```shell
  sudo cp PythonAPI.service /usr/lib/systemd/system
  ```
  
## 抖音无水印解析
## PZEZ查人系统
## 光遇随机图API
## 小鸡词典查网词API
## .......
## .......
## .......
## 其他
- 导出项目依赖
  > 参考 [https://blog.csdn.net/wzx77/article/details/106898688](https://blog.csdn.net/wzx77/article/details/106898688)
```shell
pipreqs --encoding utf8 ./ # 导出
pip3 install -r requirements.txt # 安装
```



