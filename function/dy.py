# -*- coding=utf-8 -*-

from flask import Flask, request
import json
import requests
import re
from time import time, sleep


app = Flask(__name__)

# ua就是玄学 要安卓手机才行
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; EVA-AL10 Build/HUAWEIEVA-AL10;\
         wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89\
          Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.0.0)",
}

# 功能

# 在一堆杂七杂八的东东里边提取链接


def getUrl(content):
    pat = re.compile(r"[a-zA-z]+://[^\s]*")
    url = pat.search(content)
    return url

# 获取视频id 传入任意链接都可


def getVideoId(urlShare):
    # 先访问传入的链接 获取跳转后的链接(针对短链接)
    tUrl = requests.get(url=urlShare, headers=header).url
    # 返回的链接应该是 https://www.iesdouyin.com/share/video/视频ID/ 通过正则寻找视频id
    pat = re.compile(r"/video/(\d+)/")
    result = pat.search(tUrl)  # 寻找的结果
    if result == None:
        print("[DY]id获取失败")
        id = "0"  # 失败返回0
    else:
        id = pat.search(tUrl).group(1)
    return id

# 返回视频无水印链接和描述和音频地址，传入视频id


def dyVideoUrl(id):
    b_time = time()
    # 网页抓的视频接口
    url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + \
        str(id)
    # 视频接口json解析 取得无水印的视频链接 但是没跳转
    resp = requests.get(url, headers=header).json()
    # print(resp)
    title = resp["item_list"][0]["desc"]
    wm_url = resp["item_list"][0]["video"]["play_addr"]["url_list"][0].replace(
        'playwm', 'play')
    mp3_url = resp["item_list"][0]["music"]["play_url"]["uri"]
    photo_url = resp["item_list"][0]["video"]["origin_cover"]["url_list"][0]

    # 访问无水印链接，获取跳转后的链接要用安卓手机ua访问
    video_url = requests.get(url=wm_url, headers=header).url
    e_time = time()
    print("[DY]视频解析成功啦 耗时:", str(round(e_time-b_time, 2))+"s")
    return title, video_url, mp3_url, photo_url

# 只接受get方法访问


def run(url):
    return_dict = {'status': '200'}
    try:

        result = str(getUrl(url))
        if result == None:
            return_dict["status"] = "无法提取URL"
            pass
        else:
            # 获取视频id
            id = getVideoId(url)
            if id == "0":
                return_dict["status"] = "视频id获取失败请检查url"
                print("[DY]视频id获取失败请检查url")
            else:
                return_dict["video_id"] = id

                title, video_url, mp3_url, photo_url = dyVideoUrl(id)
                return_dict["title"] = title
                return_dict["video_url"] = video_url
                return_dict["mp3_url"] = mp3_url
                return_dict["photo_url"] = photo_url

        return return_dict
    except Exception as e:
        return_dict = {'status': '500'}
        return_dict["video_id"] = "0"
        return_dict["title"] = "发生不可预料的错误!爬!%s" %(e)
        return_dict["video_url"] = "0"
        return_dict["mp3_url"] = "0"
        return_dict["photo_url"] = "0"
        return return_dict


if __name__ == "__main__":
    pass
