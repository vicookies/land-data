import csv
from linecache import getline
from math import ceil
import re
import sys
import os
from time import sleep
from tkinter import N
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions


#--------------------------------------------------------------------
#在此输入想要获取的参数 -----------------------------------------------
dataName = [
    "合同签订日期：",
    "项目位置："
]
#--------------------------------------------------------------------



dataLen = len(dataName)

def getpage(browser):
    data = {}
    i = 0
    count = 0
    while (i < dataLen):
        titleStr = ("//td[text()='"+str(dataName[i])+"']")
        dataStr = ("//td[text()='"+str(dataName[i]) + "']/following-sibling::td[1]")
        try:
            titleElement = browser.find_element(By.XPATH, titleStr)
            dataElement = browser.find_element(By.XPATH, dataStr)
            if ((titleElement.text == '' or dataElement.text == '' or dataElement.text == '--') and count < 5):
                sleep(1)
                browser.refresh()
                count = count + 1
            else:
                data[i] = (dataElement.text)
                count = 0
                i = i + 1
        except:
            data[i] = ('NULL')
        

    f = open('chinaland.csv', 'a+', encoding='utf-8-sig')
    f.truncate()
    writer = csv.DictWriter(f, fieldnames=dataName)

    deal = {}
    for i in range(dataLen):
        deal[dataName[i]] = data[i]
    # 将信息保存为csv文件
    writer.writerow(deal)
    f.close()
    return


def getData(date_begin=None, date_end=None, zero=None):
    options = EdgeOptions()
    options.use_chromium = True
    # 浏览器的位置
    options.binary_location = r'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    # 相应的浏览器的驱动位置
    browser = Edge(options=options, executable_path=r'./msedgedriver')
    # 用chrome浏览器自动打开爬取的网页
    browser.get('https://www.landchina.com/#/')
    input("打开供地结果页面，并设置好所有限制条件后，按任何键以继续")
    f = open('chinaland.csv', 'w', encoding='utf-8-sig')
    f.truncate()
    writer = csv.DictWriter(f, fieldnames=dataName)
    writer.writeheader()
    f.close()
    if (date_begin != None or date_end != None):
        setdate(browser, date_begin, date_end)
    if (zero != None):
        setzero(browser, zero)
    browser.find_element_by_xpath(
        '//*[@id="appMain"]/div/div[3]/div[3]/form[2]/div[4]/div').click()

    itemsNum = re.findall(
        '\d+', browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/div/div[1]').text)
    if (int(itemsNum[0]) != int(itemsNum[1])):
        print("结果有"+itemsNum[0]+"个，超过6000,建议多次分时执行本脚本")
    # 设置点击翻页次数为999//*[@id="appMain"]/div/div[5]/table/tr[3]
    for n in range(ceil(int(itemsNum[0])/10)):
        index = 3
        sleep(1)
        remain = int(itemsNum[0])-n*10
        if (remain > 10):
            remain = 10
        for m in range(remain):
            flag = 1
            #name=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/table/tr['+ str(index) +']').text.split('\n')
            while (flag):
                try:
                    browser.find_element_by_xpath(
                        '//*[@id="appMain"]/div/div[5]/table/tr[' + str(index) + ']').click()
                    flag = 0
                except:
                    sleep(1)
                    flag = 1
            handle = browser.window_handles  # 获取当前页句柄
            #print (handle)
            # 切换到新的网页窗口//*[@id="appMain"]/div/div[3]/div[3]
            browser.switch_to.window(handle[1])
            getpage(browser)
            browser.close()
            browser.switch_to.window(handle[0])
            index = index + 1
            sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="appMain"]/div/div[5]/div/div[2]/button[2]').click()
    return


if __name__ == "__main__":
    getData()
    print("/****************完成******************/")
    input("按任何键以继续")
