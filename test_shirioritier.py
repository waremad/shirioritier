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

