#coding:utf-8
import random

def zundoko():
    result=0

    while result!= 0b011110:
        rand=random.randint(0,1)
        print (u"ドコ",u"ズン")[rand]
        result=(result<<1)+rand&0b111111

    print u"キ・ヨ・シ!"
if __name__=="__main__":
    zundoko()
