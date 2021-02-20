'''
Author: whalefall
Date: 2021-02-20 17:33:34
LastEditTime: 2021-02-20 18:58:57
Description: 简易版的小鸡词典爬虫,可能有限制,供聚合api调用使用
'''
import requests
import json

from urllib import parse  # url编码


def checkWord(word):

    headers = {
        'Host': 'api.jikipedia.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'https://jikipedia.com',
        'XID': 'Sy2mcDa6hc6UH4q5W696OtmrHbmwsh0h2x88BKScmhluiJGIZo1eJLQzZoEpBkBOS1jXDCU4KydLz80Jqpk+EFLqi+w5qWc7f4fIrIoARTA=',
        'Client-Version': '2.4.1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'Client': 'web',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Dest': 'empty',
        'Token': '',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        # 进行url编码
        'Referer': 'https://jikipedia.com/searching?phrase={}'.format(parse.quote(word)),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {"phrase": "{}".format(word), "page": 1}
    try:
        response = requests.post(
            'https://api.jikipedia.com/go/search_definitions', headers=headers, json=data, verify=False).json()

        # print(response)
        title = response["data"][0]["term"]["title"]
        content = response["data"][0]["content"].replace(" ","")
        # print(title, content)
        dict = {
            "title": title,
            "content": content,
        }
    except Exception as e:
        print("[xiaojiDict]查%s出现错误! 错误信息:%s" % (word, e))
        dict = {
            "title": "查%s出现错误!" % (word),
            "content": "错误信息:%s" % (e),
        }
    return dict


if __name__ == "__main__":

    checkWord("时代峰峻")
