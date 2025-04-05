from shirioritier import *

def test_lastcha():
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                assert lastcha("シリトリ",i,j,k) == "リ"

    for i in [0,1]:
        for j in [0,1]:
            assert lastcha("リンゴ",i,j,0) == "ゴ"
    for i in [0,1]:
        for j in [0,1]:
            assert lastcha("リンゴ",i,j,1) == "コ"

    assert lastcha("ジンジャー",0,0,0) == "ジ"
    assert lastcha("ジンジャー",0,0,1) == "シ"
    assert lastcha("ジンジャー",0,1,0) == "ヤ"
    assert lastcha("ジンジャー",0,1,1) == "ヤ"
    assert lastcha("ジンジャー",1,0,0) == "ア"
    assert lastcha("ジンジャー",1,0,1) == "ア"
    assert lastcha("ジンジャー",1,1,0) == "ア"
    assert lastcha("ジンジャー",1,1,1) == "ア"

    assert lastcha("サイダー",0,0,0) == "ダ"
    assert lastcha("サイダー",0,1,0) == "ダ"
    assert lastcha("サイダー",0,0,1) == "タ"
    assert lastcha("サイダー",0,1,1) == "タ"
    assert lastcha("サイダー",1,0,0) == "ア"
    assert lastcha("サイダー",1,1,0) == "ア"
    assert lastcha("サイダー",1,0,1) == "ア"
    assert lastcha("サイダー",1,1,1) == "ア"

def test_txt2list():
    assert txt2list("test.txt") == {"ゲツ":0,"カ":0,"スイ":0,"モク":0,"キン":0,"ド":0,"ニチ":0}

def test_headsearch():
    dict = {"リンゴ":0,"ゴール":0,"ルーブル":0,"ルーレット":0,"ルシフェル":0,"コイントス":0}
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                assert headsearch("ル",dict,i,j,k) == ["ルーブル","ルーレット","ルシフェル"]
    for i in [0,1]:
        for j in [0,1]:
            assert headsearch("コ",dict,i,j,0) == ["コイントス"]
    for i in [0,1]:
        for j in [0,1]:
            assert headsearch("コ",dict,i,j,1) == ["ゴール","コイントス"]

def test_mindict():
    assert mindict({"a":0,"b":1,"c":2}) == 0
    assert mindict({"a":3,"b":1,"c":2}) == 1

def test_zoroend():
    dict = {"リンゴ":3,"ゴール":4,"コイン":1,"ルーブル":4,"ルーレット":5,"アインシュタイン":30,"ルシフェル":99,"コイントス":2}
    assert zeroend({"コイン":1}) == {"コイン":0}
    assert zeroend(dict) == {"リンゴ":3,"ゴール":4,"コイン":0,"ルーブル":4,"ルーレット":5,"アインシュタイン":0,"ルシフェル":99,"コイントス":2}

def test_tierrank():
    assert tierrank(1,{"a":0}) == [["a"]]
    assert tierrank(1,{"b":1,"a":0}) == [["b","a"]]
    assert tierrank(2,{"b":1,"a":0}) == [["b"],["a"]]
    assert tierrank(2,{"e":6,"d":4,"c":2,"b":1,"a":0}) == [["e","d","c"],["b","a"]]
    assert tierrank(3,{"e":6,"d":3,"c":2,"b":1,"a":0}) == [["e"],["d","c"],["b","a"]]

def test_dictsort():
    assert dictsort({"b":2,"d":4,"a":1,"c":3,}) == {"d":4,"c":3,"b":2,"a":1}
    assert dictsort({"e":0,"d":3,"c":2,"b":1,"a":0}) == {"d":3,"c":2,"b":1,"e":0,"a":0}

