# -*- coding: utf-8 -*-

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import requests
import json
import re
import jieba
import time
from collections import Counter

def request_url(url):
  headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
  }

  cont=requests.get(url, headers=headers).content
  rex=re.compile(r'\w+[(]{1}(.*)[)]{1}')
  content=rex.findall(cont)[0]
  resData=json.loads(content,"gbk")
  return resData

def getData():
  print("1. 拉取淘宝评论数据")
  text=''
  with open('./inputData/inputData.txt', 'r') as f:
    line = f.read()

    if line != '\n':
      base_url=line
      content=request_url(base_url)

      # 获取评论页数
      pageNum=content['rateDetail']['paginator']['lastPage']

      with open('outputData/getData.txt', 'w') as op:
        for i in range(1,pageNum,1):
          url = base_url + '&currentPage=%s' % str(i)
          resData=request_url(url)
          count=len(resData['rateDetail']['rateList'])
          for p in xrange(count):
            text=text + content["rateDetail"]["rateList"][p]['rateContent']
            op.write(content["rateDetail"]["rateList"][p]['rateContent'] + '\n')
          time.sleep(1)
    return text

def splitWord(text):
  print("2. 精确模式分词")
  words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
  return words

def countWord(words):
  print("3. 统计分词")
  c = Counter(words)

  with open('./outputData/outputData.txt', 'w') as wf:
    for word_freq in c.most_common(100):
      word, freq = word_freq
      wf.write(word+' '+str(freq)+'\n')

def showData():
  print("4. 可视化显示数据")

def main():
  # 1.获取数据源
  text = getData()

  # 2.分词
  words = splitWord(text)

  # 3. 词频统计
  countWord(words)

  # 4. 数据可视化
  showData()

if __name__ == '__main__':
  main()