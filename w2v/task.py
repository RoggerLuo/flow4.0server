import numpy as np
from train.train import Train
from config import Config


class Task(object):

    def __init__(self):
        self.train = Train()

    def basic(self, string):
        for i in range(Config.repeate_times):
            cost = self.train.sentence_str(string)
            print(cost)
        self.train.save()

    def readTxtLine(self, line):
        if len(line) > 20 :
            self.basic(line)


