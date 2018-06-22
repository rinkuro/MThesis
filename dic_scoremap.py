#coding:utf-8
import win_unicode_console
import math
import random

win_unicode_console.enable()

w_list = []
w_score = []
w_dict = []

c = 0

def lis_2_dic(key_list, val_list):
    return dict(zip(key_list, val_list))

#step幅決めてrange指定
def drange(begin, end, step):
    n = begin
    while n + step < end:
     yield n
     n += step


#randomにn個、No_Scoreになるように辞書listの書き換えを行う
#既存語を未知語とした際の検証
def makedata_rand(num):
    
    #seed値固定　※本実験の際には外すこと
    random.seed(0)

    n = 0

    while n < 10:
        rand = random.randint(0,num)
        w_score[rand] = "No_Score"

        print(rand, w_list[rand], w_score[rand])
        n += 1

def make_dic():

    global c

    f = open('pn_ja.dic.txt', 'r')
    
    for line in f:
        line = line.rstrip()
        term = line.split(':')

        w_list.append(term[0])
        w_score.append(term[3])

        # of words
        c += 1

    f.close()


if __name__ == "__main__":

    make_dic()

    w_dict = lis_2_dic(w_list, w_score)

#55125 words in dictionary
#print(c)

    sorted(w_dict.items(), key = lambda x: x[1])
 # print(str(k) + ": " + str(v))

    check = 0
    count = 0
    miss, miss_c = 0, 0

    for i in drange(-1.0, 1.0, 0.1):
        for v in w_dict.values():
    
            if float(v) >= i and float(v) < i+0.1:

                count += 1
            
            else:
                continue

    #roundバグってんだけど！
        #print(str(round(i,1)) + " ~ " + str(round(i,1)+ round(0.10,1)) + ": " + str(count))
        check += count
        count = 0

#randomにNo_Scoreにする
makedata_rand(check)

#総単語数(あってないけど)
#print(check)
