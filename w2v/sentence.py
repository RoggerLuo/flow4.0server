import jieba
import numpy as np

ignoreds = ['，', ',', '的', '是', '\n', ' ', '(', ')', '.', '/']


class Sentence(object):

    def __init__(self,string):
        self.word_list = []
        self.string = string

    def segment(self):
        self.word_list = jieba.lcut(self.string)  # 默认是精确模式
        return self

    def filter(self):
        filtered_list = []
        for word in self.word_list:
            if word not in ignoreds:
                filtered_list.append(word)
        self.word_list = filtered_list
        return self
