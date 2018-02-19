# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import xlwt

def data(url, n):
    response = requests.get(url)
    html = response.text
    div_bf = BeautifulSoup(html, 'lxml')
    div_title = div_bf.find_all('div', class_='title')
    div_title_bf = BeautifulSoup(str(div_title), 'lxml')
    a = div_title_bf.find_all('a')
    location = div_bf.find_all('span', class_='location-limited-text')

    name = [each.text for each in a]
    locate = [i.text for i in location]
    request_data = []

    for x in range(len(locate)):
        request_data = name[x] + '——' + locate[x]
        ws.write(n, 0, request_data)
        n = n + 1

if __name__ == '__main__':
    wb = xlwt.Workbook()  # 创建工作簿
    ws = wb.add_sheet('beijing')  # 添加表格，并定义表格名称
    n = 0

    for page in range(1, 5):
        print(page)    # 作用是跟踪程序爬取到第几页
        url = 'https://house.focus.cn/loupan/p{}/'.format(page)
        data(url, n)
        n = page * 20

    wb.save('F:\ beijing.xls')
