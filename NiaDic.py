class NiaDic:
    Dic = dict([])
    userDic = dict([])

    def __init__(self):
        f = open('./dict.txt', 'r', encoding='utf8')
        ff = open('./userdict.txt', 'r',encoding='utf8')
        wordnum = 0
        userdefword = 0
        for line in f:
            tmp = line.strip().split('\t')
            self.Dic[tmp[0]] = 'ncn'
            wordnum += 1

        for line in ff:
            tmp = line.strip().split('\t')
            self.userDic[tmp[0]] = 'ncn'
            wordnum += 1
            userdefword += 1
        f.close()
        ff.close()
        print(f'{wordnum}개의 단어가 로드되었습니다. ({userdefword}개의 사용자 지정 단어)')

    def addword(self, word, wordtype='ncn'):
        self.Dic[word] = wordtype
        f = open('userdict.txt', 'a')
        f.write(word + '\t' + wordtype)
        f.close()
        print(f'단어 추가 완료({word})')

    def findword(self, word):
        if word in self.userDic.keys():
            return [word, self.userDic[word]]
        elif word in self.Dic.keys():
            return [word, self.Dic[word]]
        else:
            return [word, 'unk']

