#coding: utf-8

import MeCab
import pandas as pd
#日本語エンコードする場合はencoding="utf-8"のオプションを忘れずに。
import codecs
from collections import Counter

def simple_parser(t):
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(t)

    a = []
    while node:
        a.append(node.surface)
        node = node.next

    print(a)

def words_counter():

    f = open('parsed_sample.txt', 'r', encoding = 'utf-8', errors = 'ignore')

    tweets = f.readlines()

    f.close()

    tagger = MeCab.Tagger('-Ochasen')
    counter = Counter()
    for tweet in tweets:
        tagger.parse('')
        node = tagger.parseToNode(tweet)
        while node:
            word = node.surface
            counter[word] += 1
            node = node.next

    stop_word_list = []
#counter.most_commonの内部は[(word, cnt),...]のdict型になっている
    for word, cnt in counter.most_common(100):
        stop_word_list.append(word)
        #print (word, cnt)

def stop_word_geneater():
    f = open('parsed_sample.txt', 'r', encoding = 'utf-8', errors = 'ignore')

    tweets = f.readlines()

    f.close()

    tagger = MeCab.Tagger('-Ochasen')
    counter = Counter()
    for tweet in tweets:
        tagger.parse('')
        node = tagger.parseToNode(tweet)
        while node:
            word = node.surface
            #counter[word] += 1
            node = node.next

    stop_word_list = []
#counter.most_commonの内部は[(word, cnt),...]のdict型になっている
    for word in counter.most_common(100):
        stop_word_list.append(word)
        #print (word, cnt)

    print(stop_word_list)

#test text
t = u"明日松戸のアニメイトに行く"

#words_counter()
#simple_parser(t)

stop_word_geneater()
