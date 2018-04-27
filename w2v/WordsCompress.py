import numpy as np
import os
import pickle

db_path = os.path.dirname(os.path.realpath(__file__)) + '/w2v.pkl'


def getEntrysByWord(word, data):
    return list(filter(lambda e: e['word'] == word, data))


class WordsCompress(object):

    def __init__(self):
        self.data = self.getDbData()

    def feedWordlist(self, wordlist):
        wordlist = self.uniq(wordlist)
        entrylist = self.wordlist2entrylist(wordlist)
        combinationList = self.combine2list(entrylist)
        sortedList = sorted(combinationList, key=lambda dic: dic['devi'])
        interception = sortedList[:10]
        return self.getBackWordlist(interception)

    def getBackWordlist(self, interception):
        wordlist = []
        for item in interception:
            wordlist.append(item['entry1'])
            wordlist.append(item['entry2'])
        wordlist = self.uniq(wordlist)
        return wordlist

    def wordlist2entrylist(self, wordlist):
        entrylist = []
        for word in wordlist:
            entrys = getEntrysByWord(word, self.data)
            if len(entrys) != 0:
                entrylist.append(entrys[0])
        return entrylist

    def uniq(self, wordlist):
        uniqList = []
        for word in wordlist:
            if word not in uniqList:
                uniqList.append(word)
        return uniqList

    def combine2list(self, entrylist):
        combinationList = []
        for i in range(len(entrylist)):  # len = 3, i = 1
            entry = entrylist[i]

            for j in range(len(entrylist) - i - 1):  # len = 1, j = 0
                _entry = entrylist[i + j + 1]  # i+j+1 = 2
                combinationList.append({'entry1': entry['word'], 'entry2': _entry[
                                       'word'], 'devi': self.calcDevi(entry, _entry)})
        return combinationList

    def getDbData(self):
        data = []
        if os.path.exists(db_path):
            with open(db_path, 'rb') as f:
                data = pickle.load(f)
        else:
            data = []
        return data

    def calcDevi(self, entry, _entry):
        deviationVec = entry['vec'][:8] - _entry['vec'][:8]
        deviationVec = np.square(deviationVec)
        return np.sum(deviationVec)


# f = FindSimilar()
# f.byWordlist(["##", "定义", "手上", "工作", "类型", "###", "逻辑", "梳理", "###", "事务", "规划", "类", "习惯", "形成", "对比", "旧习惯", "概念", "建立", "联系", "范畴", "本质", "类型", "工作", "阅读", "代码", "熟悉业务",
#               "转换", "事务", "分析方法", "范畴", "技能", "处理", "快乐", "Handle", "局面", "##", "笔记", "类型", "加标签", "根本", "搜", "不到", "node", "npm", "版本", "很难", "碰到", "难", "想到", "丢", "这里", "不管"])
