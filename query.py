import requests
from bs4 import BeautifulSoup
def query_card_detail(userName, password):
    loginUrl = 'http://apex104.apex.com.tw/ehrportal/LoginFOpen.asp'
    session = requests.session()
    beforeLoginPage = session.get(loginUrl)
    payload = {'op': 'act', 'companyno': '23131763', 'companyid': 1, 'username': userName,
            'password': password, 'selLanguage': 0, 'imageField.x': 45, 'imageField.y': 8}
    loginResult = session.post(loginUrl, data=payload)
    loginResultSoup = BeautifulSoup(loginResult.content, 'html.parser')

    cardDetailUrl = 'http://apex104.apex.com.tw/ehrportal//DEPT/Personal_CardData_DataList.asp'
    cardDetailResult = session.post(cardDetailUrl)



    soup = BeautifulSoup(cardDetailResult.content, 'html.parser')
    return str(soup)
