import csv
from linecache import getline
from math import floor
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

def setdate (browser,date_begin,date_end):
    browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[3]/form[2]/div[1]/div/div[1]/input').send_keys(date_begin)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[3]/form[2]/div[1]/div/div[2]/input').send_keys(date_end)
    sleep(1)
    return

def setzero (browser,zero):
    browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[3]/form[1]/div[1]/div/div/div/span').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cascader-menu-9577-0-14"]/span/span').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cascader-menu-5637-1-14"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="cascader-menu-1341-2-1"]').click()
    sleep(1)
    return
def enter (browser):
    browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[3]/form[2]/div[4]/div').click()
    sleep(1)
    return

def getpage (browser):
    getflag=0
    countflag=0
    while(getflag==0 or countflag<5):
        try:
            region=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[2]/td[2]').text
        except:
            region='NULL'
        if(region!=''):
            getflag=1
        else:
            sleep(1)
            countflag=countflag+1
            browser.refresh()


    try:
        EMnumber=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[2]/td[4]').text
    except:
        EMnumber='NULL'
    try:
        PROJname=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[3]/td[2]').text
    except:
        PROJname='NULL'
    try:
        PROJlocat=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[4]/td[2]').text
    except:
        PROJlocat='NULL'
    try:
        area=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[5]/td[2]').text
    except:
        area='NULL'
    try:
        landsources=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[5]/td[4]').text
    except:
        landsources='NULL'
    try:
        landusage=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[6]/td[2]').text
    except:
        landusage='NULL'
    try:
        landway=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[6]').text
    except:
        landway='NULL'
    try:
        agelimit=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[7]/td[2]').text
    except:
        agelimit='NULL'
    try:
        landclass=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[7]/td[4]').text
    except:
        landclass='NULL'
    try:
        landlevel=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[8]/td[2]').text
    except:
        landlevel='NULL'
    try:
        landprince=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[8]/td[4]').text
    except:
        landprince='NULL'
    try:
        issue=0
        while(browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr['+str(10+issue)+']/td[1]').text.isalnum()):
            issue=issue+1
        paymentissue=issue
        if(issue==0):
            paymentissue='NULL'
    except:
        paymentissue='NULL'
    try:
        if (issue != 0):
            paymentdate=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr[10]/td[2]').text
        else:
            paymentdate='NULL'
    except:
        paymentdate='NULL'
    try:
        paymentprince=0
        if(issue != 0):
            for x in range(1,issue+1):
                paymentprince=paymentprince+float(browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr['+str(9+issue)+']/td[3]').text)
        else:
            paymentprince='NULL'    
    except:
        paymentprince='NULL'
    try:
        hoster=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[3]/div[6]/div[1]/div/table/tr['+str(10+issue)+']/td[2]').text
    except:
        hoster='NULL'
    f = open('chinaland.csv', 'a+' ,encoding='utf-8-sig')
    f.truncate()
    fnames = ["region","EMnumber","PROJname","PROJlocat","area","landsources","landusage", \
            "landway","agelimit","landclass","landlevel","landprince","paymentissue", \
            "paymentdate","paymentprince","hoster"]
    writer = csv.DictWriter(f, fieldnames=fnames)  
    
    deal={}
    deal["region"]=region
    deal["EMnumber"]=EMnumber
    deal["PROJname"]=PROJname
    deal["PROJlocat"]=PROJname
    deal["area"]=area
    deal["landsources"]=landsources
    deal["landusage"]=landusage
    deal["landway"]=landway
    deal["agelimit"]=agelimit
    deal["landclass"]=landclass
    deal["landlevel"]=landlevel
    deal["landprince"]=landprince
    deal["paymentissue"]=paymentissue
    deal["paymentdate"]=paymentdate
    deal["paymentprince"]=paymentprince
    deal["hoster"]=hoster
    #??????????????????csv??????
    writer.writerow(deal)
    f.close()
    return
    
def getData(date_begin=None,date_end=None,zero=None):
    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = r'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe' # ??????????????????
    browser = Edge(options=options, executable_path=r'./msedgedriver') # ?????????????????????????????????

    browser.get('https://www.landchina.com/#/')#???chrome????????????????????????????????????
    input("input enter key to continue: ")
    f = open('chinaland.csv', 'w' ,encoding='utf-8-sig')
    f.truncate()
    fnames = ["region","EMnumber","PROJname","PROJlocat","area","landsources","landusage", \
            "landway","agelimit","landclass","landlevel","landprince","paymentissue", \
            "paymentdate","paymentprince","hoster"]
    writer = csv.DictWriter(f, fieldnames=fnames)  
    writer.writeheader()
    f.close()
    if(date_begin!=None or date_end!=None):
        setdate(browser,date_begin,date_end)
    if(zero!=None):
        setzero(browser,zero)
    enter(browser)

    itemsNum = re.findall('\d+', browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/div/div[1]').text)
    if(int(itemsNum[0])!=int(itemsNum[1])):
        print("????????????6000???----??????????????????")
    for n in range(floor(int(itemsNum[0])/10)):#???????????????????????????999//*[@id="appMain"]/div/div[5]/table/tr[3]
        index=3
        sleep(2)
        remain = int(itemsNum[0])-n*10
        if(remain>10):
            remain=10
        for m in range(remain):
            flag=1
            #name=browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/table/tr['+ str(index) +']').text.split('\n')
            while(flag):
                try:
                    browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/table/tr['+ str(index) +']').click()
                    flag=0
                except:
                    sleep(1)
                    flag=1
            handle = browser.window_handles # ?????????????????????
            #print (handle)
            browser.switch_to.window (handle[1]) # ???????????????????????????//*[@id="appMain"]/div/div[3]/div[3]
            getpage(browser)
            browser.close()
            browser.switch_to.window (handle[0])
            index = index + 1
            sleep(1)
        browser.find_element_by_xpath('//*[@id="appMain"]/div/div[5]/div/div[2]/button[2]').click()
    return


if __name__ == "__main__":
    #opt_date_start = input("??????????????????: (??????:2000-01-01,????????????????????????n/N)\n")
    #opt_date_end = input("??????????????????: (??????:2000-01-01,????????????????????????n/N)\n")
    #opt_zero = input("????????????: (??????????????????n/N)\n")
    #if(opt_date_start=="N" or opt_date_start=="n"):
    #    opt_date_start=None
    #if(opt_date_end=="N" or opt_date_end=="n"):
    #    opt_date_end=None
    #if(opt_zero=="N" or opt_zero=="n"):
    #    opt_zero=None
    getData()
    print("/****************??????******************/")
    input("input enter key to continue")