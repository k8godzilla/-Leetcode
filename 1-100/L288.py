# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:38:06 2019

@author: admin
"""

'''
一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。

以下是一些单词缩写的范例：

a) it                      --> it    (没有缩写)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
假设你有一个字典和一个单词，请你判断该单词的缩写在这本字典中是否唯一。若单词的缩写在字典中没有任何 其他 单词与其缩写相同，则被称为单词的唯一缩写。

示例：

给定 dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-word-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ValidWordAbbr:

    def __init__(self, dictionary: list):
        # dictionary: List[str]
        self.d = {}
        self.pool = set()
        for w in  dictionary:
            if len(w) > 0:
                if len(w) in self.d.keys():
                    if w[0] + w[-1] in self.d[len(w)]:
                        self.d[len(w)][w[0] + w[-1]].add(w)
                    else:
                        self.d[len(w)][w[0] + w[-1]] = set()
                        self.d[len(w)][w[0] + w[-1]].add(w)
                else:
                    self.d[len(w)] = {}
                    self.d[len(w)][w[0] + w[-1]] = set()
                    self.d[len(w)][w[0] + w[-1]].add(w)
                
        


    def isUnique(self, word: str) -> bool:
        if len(word) == 0:
            return 1 in self.d.keys()
        if len(word) not in self.d.keys():
            return True
        else:
            if word[0] + word[-1] not in self.d[len(word)]:
                return True
            else:
                if word not in self.d[len(word)][word[0] + word[-1]] or len(self.d[len(word)][word[0] + word[-1]]) > 1:
                    return False
                else:
                    return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
















