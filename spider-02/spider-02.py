# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import xlwt

def data(url, n):
    response = requests.get(url)
    html = response.text
    div_bf = BeautifulSoup(html, 'lxml')
    div_ProjectList = div_bf.find_all('div', class_='investmentName')
    div_ProjectList_bf = BeautifulSoup(str(div_ProjectList), 'lxml')
    a = div_ProjectList_bf.find_all('a')
    href = ['https://www.gzjkp2p.com/'+each.get('href') for each in a]
    print(href)

    for each in href:
        response = requests.get(each)
        html = response.text
        div_bf = BeautifulSoup(html, 'lxml')
        h2 = div_bf.find('h2').text
        h6 = div_bf.find('h6').text
        print(h2, h6)
        ws.write(n, 0, h2)
        ws.write(n, 1, h6)
        n = n + 1

if __name__ == '__main__':
    wb = xlwt.Workbook()  # 创建工作簿
    ws = wb.add_sheet('jinrong')  # 添加表格，并定义表格名称
    n = 0
    for page in range(1, 3):
        url = 'https://www.gzjkp2p.com/finance.do?curPage={}'.format(page)
        data(url, n)
        n = page * 8

    wb.save('F:\jinrong.xls')