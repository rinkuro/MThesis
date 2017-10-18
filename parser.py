#coding: utf-8

import MeCab
import pandas as pd
#日本語エンコードする場合はencoding="utf-8"のオプションを忘れずに。


def parser(t):
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(t)

    a = []
    while node:
        a.append(node.surface)
        node = node.next

    print(a)

t = u"明日松戸のアニメイトに行く"

parser(t)
