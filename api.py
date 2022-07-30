import requests
import urllib
import csv

CSV_PATH = 'ranking.csv'

def get_api(url, params: dict):
    result = requests.get(url, params=params)
    return result.json()

# CSV書き込み
def write_csv(name, rank):
    with open(CSV_PATH, 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        print(rank)
        writer.writerow([str(rank)]+[name])

def main():
    keyword = "鬼滅"
    # 課題1,2
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    
    # 課題3
    #url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
    
    # 課題4
    #url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    
    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1019079537947262807",
        "minPrice": 111,
        "genreId": "100283", #課題4
    }
    
    #print(get_api(url, params=params))
    res = get_api(url, params=params)
    
    # 課題2
    # for i in res['Items']:
    #     item = i['Item']
    #     name = item['itemName']
    #     price = item['itemPrice']
    #     print("--------------------------")
    #     print("商品名:"+name)
    #     print("価格:"+str(price))
    
    # 課題3
    # for i in res['Products']:
    #     product = i['Product']
    #     name = product['productName']
    #     minPrice = product['minPrice']
    #     maxPrice = product['maxPrice']
    #     print("--------------------------")
    #     print("商品名:"+name)
    #     print("最低価格:"+str(minPrice))
    #     print("最高価格:"+str(maxPrice))

    # 課題4
    for i in res['Items']:
        item = i['Item']
        name = item['itemName']
        rank = item['rank']
        # CSV出力
        write_csv(name, rank)

main()
