# coding: utf-8

# 既存研究の実装しような。
import sys, io, codecs
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import re
import json
import csv
import MeCab
import pandas as pd
# from pyknp import Jumanapp

def extracter():
    #.jsonを一行ずつ読み込む（JSON Lines）
    #f = open('T1_201401-201412_1M.json', 'r')
    f = open('a_data.json','r', encoding = 'cp932', errors = 'ignore')
    #all_text = json.loads(f)

    all_text = {i : json.loads(line) for i, line in enumerate(f)}
    #総ツイート数カウント
    counter = 0
    for i in range(len(all_text)):

        t = all_text[i]['text']
        # @以下を削除
        edited_t = re.sub(r'@[a-zA-Z0-9_-]+|https?://[-_.!~*\'()a-zA-Z0-9;/?:@&=+$,%#]+| RT[:ｆ]+', "", t).strip()
        counter += 1
    #500,000 tweets/file
    print(counter)
    print(t)

extracter()

#def juman(s):
#    jumanpp = Jumanpp()


#def mecab(s):
#    tagger = MeCab.Tagger('Owakati')
#    t = tagger.parse(s)

#def w2b(s):
