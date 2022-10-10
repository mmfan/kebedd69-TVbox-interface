# coding=utf-8
# !/usr/bin/python
import sys
import re
sys.path.append('..')
from base.spider import Spider
import urllib.parse
import requests
import base64
from Crypto.Cipher import AES

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "磁力狗"

    def init(self, extend=""):
        print("============{0}============".format(extend))
        pass

    def homeContent(self, filter):
        result = {}
        return result

    def homeVideoContent(self):
        result = {
            'list': []
        }
        return result

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        return result

    def detailContent(self, array):
        tid = array[0]
        url = 'https://clg010.xyz/{0}'.format(tid)

        header = {"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"}
        rsp = self.fetch(url,headers=header)
        root = self.html(self.cleanText(rsp.text))
        title = root.xpath(".//div[@class='bt_title']/h2/text()")[0]
        vod = {
            "vod_id": tid,
            "vod_name": title,
            "vod_pic": "",
            "type_name": "",
            "vod_year": "",
            "vod_area": "",
            "vod_remarks": "",
            "vod_actor": "",
            "vod_director": "",
            "vod_content": title
        }
        vod_play_from = ''
        playFrom = []
        playFrom.append("thunder")
        vod_play_from = vod_play_from.join(playFrom)
        vod_play_url = ''
        playList = []
        vodList = root.xpath(".//div[contains(@class,'ssbox')]")
        for vl in vodList:
            vodItems = []
            sids = vl.xpath(".//div[contains(@class,'title')]/h3/text()")
            if len(sids) >0:
                sid = sids[0]
                if "磁力链接下载" in sid:
                    playurl = vl.xpath(".//div[contains(@class,'content')]/a/@href")[0]
                    #vod['vod_id'] = playurl
                    vodItems.append(title + "$" + playurl)
            joinStr = '#'
            joinStr = joinStr.join(vodItems)
            playList.append(joinStr)
        vod_play_url = vod_play_url.join(playList)
        vod['vod_play_from'] = vod_play_from
        vod['vod_play_url'] = vod_play_url
        result = {
            'list': [
                vod
            ]
        }
        return result

    def searchContent(self, key, quick):
        url = 'https://clg010.xyz/search-{0}-1-0-1.html'.format(key)
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "referer":"https://clg010.xyz",
            "origin":"https://clg010.xyz",
        }
        rsp = self.fetch(url,header)
        root = self.html(self.cleanText(rsp.text))
        aList = root.xpath("//div[contains(@class,'ssbox')]/div/h3/a")
        videos = []
        for a in aList:
            sid = a.xpath(".//@href")[0]
            names = a.xpath(".//text()")
            name = "".join(names).replace(" ","")
            if format(key) in name:
                videos.append({
                    "vod_id": sid,
                    "vod_name": name
                })
        result = {
            'list': videos
        }
        return result


    def playerContent(self, flag, id, vipFlags):
        result = {}
        if id == '00000':
            return {}
        purl = id
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = purl
        result["header"] = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {}

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def localProxy(self, param):
        action = {
            'url': '',
            'header': '',
            'param': '',
            'type': 'string',
            'after': ''
        }
        return [200, "video/MP2T", action, ""]