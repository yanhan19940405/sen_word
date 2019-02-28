# -*- coding:utf-8 -*-
import time
time1=time.time()
# coding=utf-8
class Trie:
    root = {}
    leaf = '/'
    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.leaf] = None

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.leaf in node
    def output(self):
        test={}
        test[""]=self.root
        return test
def searchword(trie,sen,value):
    uptemp=0
    i=0
    j=0
    k=0
    senword=[]
    for i in range(len(sen)):
        if sen[i] in trie.root:
            uptemp=i
            if int(uptemp+value)<=len(sen):
                for j in range(value+1):
                    if trie.find(str(sen[uptemp:uptemp+j])) == True:
                        senword.append(sen[uptemp:uptemp+j])
                    else:
                        pass
                    j=j+1
            elif int(uptemp+value)>len(sen):
                for k in range(len(sen)-uptemp+1):
                    if trie.find(str(sen[uptemp:uptemp+k])) == True:
                        senword.append(sen[uptemp:uptemp+k])
                    else:
                        pass
                    k=k+1
        elif sen[i] not in trie.root:
            uptemp=0
        uptemp=0
        i=i+1
    return senword


if __name__ == '__main__':
    trie_obj = Trie()
    # 添加关键词
    trie_obj.add('3月21日')
    trie_obj.add('帝国')
    trie_obj.add('高加索')
    trie_obj.add('苏联最高统帅部')
    # 打印构建的Trie树
    print(trie_obj.root)
    a=trie_obj.output()
    sen="1944年3月21日，帝国中央司令部下发施罗德作战计划，第三突击装甲集团军群配合中央集团军群向高加索地区展开钳形攻势，以便于对于未知局面进行突破。苏联最高统帅部针对局面严重性，决定立刻启动应急预案。"
    print("文本句子:",sen)
    print("提取关键词:",searchword(trie_obj,sen,7))
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')



