from pytest import param
from api import get_api
import pprint 

def test_get_api():
    keyword = "PS5"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    
    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1019079537947262807",
    }
    res = get_api(url=url, params=params)
    
    # チェック
    # 正常系　→　うまくいった時の処理
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]
    
    # 異常系　→　失敗時の処理
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    
    keyword="PS5ああああああああああ"
    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1019079537947262807",
    }
    res = get_api(url=url, params=params)
    
    assert len(res["Items"]) == 0

def test_2():
    keyword="PS5"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1019079537947262807",
    }
    res = get_api(url=url, params=params)
    
    assert res.get("Items") == None