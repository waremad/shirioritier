import random

class config:#設定用クラス
    longmather = False #最後の文字が長音だった場合,False:無視する,True:母音とする
    smallbig = True #最後の文字が拗音・促音だった場合,False:無視する,True:清音とする
    dullhalf = False #最後の文字が濁音・半濁音だった場合,False:そのまま,True:とってもよい

#タイプミス許容
def prnit(*tp):
    for i in tp:
        print(i,end="")
    print()

#単語の最後の文字
def lastcha(self,longm=config.longmather,small=config.smallbig,dullh=config.dullhalf):
    if self == "":
        raise ValueError("\"Null\"")
    if self[-1] == "ー":
        if len(self) == 1:
            raise ValueError("長音\"ー\"")
        if longm:
            mathe = {
                "ァ":"ア","ア":"ア","ィ":"イ","イ":"イ","ゥ":"ウ","ウ":"ウ","ェ":"エ","エ":"エ","ォ":"オ","オ":"オ",
                "カ":"ア","ガ":"ア","キ":"イ","ギ":"イ","ク":"ウ","グ":"ウ","ケ":"エ","ゲ":"エ","コ":"オ","ゴ":"オ",
                "サ":"ア","ザ":"ア","シ":"イ","ジ":"イ","ス":"ウ","ズ":"ウ","セ":"エ","ゼ":"エ","ソ":"オ","ゾ":"オ",
                "タ":"ア","ダ":"ア","チ":"イ","ヂ":"イ","ッ":"ウ","ツ":"ウ","ヅ":"ウ","テ":"エ","デ":"エ","ト":"オ","ド":"オ",
                "ナ":"ア","ニ":"イ","ヌ":"ウ","ネ":"エ","ノ":"オ",
                "ハ":"ア","バ":"ア","パ":"ア","ヒ":"イ","ビ":"イ","ピ":"イ","フ":"ウ","ブ":"ウ","プ":"ウ",
                "ヘ":"エ","ベ":"エ","ペ":"エ","ホ":"オ","ボ":"オ","ポ":"オ",
                "マ":"ア","ミ":"イ","ム":"ウ","メ":"エ","モ":"オ",
                "ャ":"ア","ヤ":"ア","ュ":"ウ","ユ":"ウ","ョ":"オ","ヨ":"オ",
                "ラ":"ア","リ":"イ","ル":"ウ","レ":"エ","ロ":"オ",
                "ヮ":"ア","ワ":"ア","ヰ":"イ","ヱ":"エ","ヲ":"オ","ン":"ン",
                "ヴ":"ウ","ヵ":"ア","ヶ":"エ","ヷ":"ア","ヸ":"イ","ヹ":"エ","ヺ":"オ",}
            if self[-2] in mathe:
                return mathe[self[-2]]
            else:
                raise ValueError("\""+self[-2]+"\"")
        else:
            return lastcha(self[:-1],longm,small,dullh)
    
    sma = {
        "ャ":"ヤ","ュ":"ユ","ョ":"ヨ","ッ":"ツ",
        "ァ":"ア","ィ":"イ","ゥ":"ウ","ェ":"エ","ォ":"オ",
        "ヮ":"ワ","ヶ":"ケ","ヵ":"カ"}
    if self[-1] in list(sma.keys()):
        if len(self) == 1:
            raise ValueError("\""+self[-1]+"\"")
        if small:
            return sma[self[-1]]
        else:
            return lastcha(self[:-1],longm,small,dullh)
    
    if dullh:
        dull = {
            "ガ":"カ","ギ":"キ","グ":"ク","ゲ":"ケ","ゴ":"コ",
            "ザ":"サ","ジ":"シ","ズ":"ス","ゼ":"セ","ゾ":"ソ",
            "ダ":"タ","ヂ":"チ","ヅ":"ツ","デ":"テ","ド":"ト",
            "バ":"ハ","ビ":"ヒ","ブ":"フ","ベ":"ヘ","ボ":"ホ",
            "パ":"ハ","ピ":"ヒ","プ":"フ","ペ":"ヘ","ポ":"ホ",
            "ヴ":"ウ","ヷ":"ワ","ヸ":"ヰ","ヹ":"ヱ","ヺ":"ヲ",}
        if self[-1] in dull:
            return dull[self[-1]]
        else:
            return self[-1]
    else:
        return self[-1]

#.txtから辞書にする。
def txt2dict(path):
    out = {}
    with open(path,mode="r",encoding="utf-8") as f:
        for i in f:
            out[i.strip()] = 0
    return out

#ある文字で始まる単語を辞書から抽出してリストで返す
def headsearch(chara,dict,longm=config.longmather,small=config.smallbig,dullh=config.dullhalf):
    if chara == "":
        ValueError("\"Null\"")
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    out = []
    dull = {
        "ガ":"カ","ギ":"キ","グ":"ク","ゲ":"ケ","ゴ":"コ",
        "ザ":"サ","ジ":"シ","ズ":"ス","ゼ":"セ","ゾ":"ソ",
        "ダ":"タ","ヂ":"チ","ヅ":"ツ","デ":"テ","ド":"ト",
        "バ":"ハ","ビ":"ヒ","ブ":"フ","ベ":"ヘ","ボ":"ホ",
        "パ":"ハ","ピ":"ヒ","プ":"フ","ペ":"ヘ","ポ":"ホ",
        "ヴ":"ウ","ヷ":"ワ","ヸ":"ヰ","ヹ":"ヱ","ヺ":"ヲ",}
    for i in list(dict.keys()):
        if dullh:
            if i[0] in dull:
                if dull[i[0]] == chara:
                    out.append(i)
            else:
                if i[0] == chara:
                    out.append(i)
        else:
            if i[0] == chara:
                out.append(i)
    return out

#辞書のvalueの最小値を返す
def mindict(dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    return min(list(dict.values()))

#最後の文字が「ン」のランクを0にする
def zeroend(dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    out = {}
    for i in list(dict.keys()):
        if i[-1] == "ン":
            out[i] = 0
        else:
            out[i] = dict[i]
    return out

#ランク付けされて、降順にソードされた辞書データをn個のtierに分ける
def tierrank(n,dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    #print("|",n,dict,"|")
    if n > len(list(dict.keys())):
        ValueError("n > len(list(dict.keys()))",n,">",len(list(dict.keys())))
    if n == 0:
        ValueError("n==0")
    if n%2 == 0:
        m = n//2
        #print("dict,dict.values(),list(dict.values())",dict,dict.values(),list(dict.values()))
        maxv = max(list(dict.values()))
        minv = min(list(dict.values()))
        long = len(list(dict.values()))
        if long%2 == 0:
            mid = list(dict.values())[long//2] + list(dict.values())[long//2-1]
            mid = mid/2 
        else:
            mid = list(dict.values())[long//2 - 1 + long%2]
        overs = []
        unders = []
        for i in list(dict.keys()):
            if dict[i] < mid:
                unders.append(i)
            else:
                overs.append(i)
        #print("overs,unders",overs,unders)
        #print("mid,m",mid,m)
        orange = (maxv - mid)/m
        urange = (mid - minv)/m
        #print("orange,urange",orange,urange)
        outovers = []
        outunders = []
        for i in range(m):
            outovers.append([])
            outunders.append([])
        if urange == 0:
            outunders = [unders]
        else:
            for i in unders:
                #print("(dict[i]-minv)//urange",(dict[i]-minv)//urange)
                """
                prnit("V--------------------")
                prnit("unders",unders)
                prnit("outunders",outunders)
                print("i,dict[i]",i,dict[i])
                print("minv,dict[i]-minv",minv,dict[i]-minv)
                prnit("urange,(dict[i]-minv)//urange",urange,(dict[i]-minv)//urange)
                prnit("^--------------------")
                prnit("Bf outunders",outunders)
                prnit(-1-int((dict[i]-minv)//urange))
                """
                outunders[-1-int((dict[i]-minv)//urange)].append(i)
                #prnit("Af outunders",outunders)
                
        if orange == 0:
            outovers = [overs]
        else:
            for i in overs:
                #print("int((dict[i]-mid)//orange)",int((dict[i]-mid)//orange))
                if dict[i] == maxv:
                    outovers[0].append(i)
                else:
                    outovers[-1-int((dict[i]-mid)//orange)].append(i)
        #print("outovers,outunders",outovers,outunders)
        return outovers + outunders
    else:
        wout = tierrank(n*2,dict)
        out = []
        for i in range(n):
            out.append(wout[i*2]+wout[i*2+1])
        return out

#辞書を降順にソート
def dictsort(dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    z = list(zip( list(dict.values()),list(dict.keys())))
    z = sorted(z,reverse=True)
    out = {}
    for i in z:
        out[i[1]] = i[0]
    return out

#辞書のkeyをランダムに返す
def dicranchoice(dict):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    return random.choice(list(dict.keys()))

#しりとり的に次に進む
def nextword(self,dict,alreadys):
    if dict == {}:
        ValueError("\"{"+"Null"+"}\"")
    ls = headsearch(lastcha(self),dict)
    out = []
    for i in ls:
        if not(i in alreadys):
            out.append(i)
    #print("ls",ls)
    #prnit("out",out)
    #prnit("alreadys",alreadys)
    if out == []:
        return ""
    else:
        return random.choice(out)

#85%の確率でTrueを返す
def percent85():
    return random.randint(1,100) <= 85

words = txt2dict("test5.txt")
#for i in range(1000):
while mindict(words) < 100:
    alreadys = []
    word = dicranchoice(words)
    alreadys.append(word)
    #prnit(word)
    words[word] += 1
    while percent85() and word != "":
        bfword = word
        word = nextword(word,words,alreadys)
        alreadys.append(word)
        #prnit(word)
        if word == "":
            words[bfword] += 1
            #prnit("word,bfword",word,bfword)
        else:
            words[word] += 1

with open("out.txt",mode="w",encoding="utf-8") as f:
    f.writelines("")

words = zeroend(words)
words = dictsort(words)

for i in words:
    if i[0] == "キ":
        print(i)

rankls = tierrank(5,words)
#for i in list(words.keys()):
#    prnit(i,words[i])
for i in range(len(rankls)):
    with open("out.txt",mode="a",encoding="utf-8") as f:
        f.write("\n"+str(i+1)+"\n")
    for j in rankls[i]:
        with open("out.txt",mode="a",encoding="utf-8") as f:
            f.write(str(j)+":"+str(words[j])+"\n")