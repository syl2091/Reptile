__author__ = 'CQC'

import re


class Tool:
    def __init__(self):
        pass

    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')

    removeAddr = re.compile('<a.*?>|</a>')

    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    replaceTD = re.compile('<td>')

    replaceBR = re.compile('<br><br>|<br>')

    removeExtraTag = re.compile('<.*?>')

    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)

        return x.strip()