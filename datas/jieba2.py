# -*- coding: utf-8 -*-

import jieba
import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    #jieba.set_dictionary('jieba_dict/dict.txt.big')

    # load stopwords set
    #stopwordset = set()
    #with open('jieba_dict/stopwords.txt','r',encoding='utf-8') as sw:
    #    for line in sw:
    #        stopwordset.add(line.strip('\n'))
    
    filee= 'yangqing2GBK.txt'
    output = open(filee+'-segment2.txt','w')

    texts_num = 0

    with open(filee, "rb") as f:
      #if(f.readline() == ""):
      print("geting data")
      bookdata = f.read(190000000).decode('GBK')#,'ignore'
      print("geting data  OK ")
      lineu = bookdata
      p = 0
      for p in range(0,len(bookdata),500):
            line = bookdata[p:p+500]
            #print(line)
            words = jieba.cut(line, cut_all=False)
            for word in words:
                output.write(word +' ')
            texts_num += 500
            if texts_num % 1000000 == 0:
                logging.info("已完成前 %d 字的斷詞" % texts_num)
    output.close()

if __name__ == '__main__':
	main()
