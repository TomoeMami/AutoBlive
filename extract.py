# -*- coding: utf-8 -*-
import re
import datetime
import pandas as pd
import os
import numpy as np

def getYesterday(dayb): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=dayb) 
    yesterday=today-oneday  
    return yesterday


if __name__ == '__main__':
    uid = ['12235923','11588230','13946381','14222920','14917277','3822389','21302477','21304638','21130785','14578426','14893','337374','14275133','21302352','21144047','1321846','14892076','13576775','6241497','21133979','14052636','21224291','21195793','21219990','10209381','21129632','21107534','21132965','14327465','7962050','21302479','947447','6080883','4895312','21317030','3889934','15142311','4634167','21131813','6632844','4664126','12770821','11575621','704808','21302469','180784','3827429','9680769','11261960','4078398','13744134','11110277','21320551','21320281','8725120','262755','3657657','160683','7688266','6586670','278936','12492310','2610619','21318294','13289738','40529','21327595','21357592','284685','14110147','21288388','919919','895206','21300316','15065340']
    # 
    yesterday = str(getYesterday(1))
    cleanday = str(getYesterday(3))
    #yesterday = "2019-04-22"
    resultdir = "C:/Users/Administrator/Documents/blive/"
    with open(resultdir+"comments.csv","a",encoding='utf_8_sig') as f:
        f.write(yesterday+',') 
    with open(resultdir+"income.csv","a",encoding='utf_8_sig') as f:
        f.write(yesterday+',') 
    for k in range(len(uid)):
    # k=1
    # k=0
        result = ""
        times = ""
        value = ""
        dhhtimes = ""
        dhhprice = ""
        filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/'+yesterday
        cleandir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/'+cleanday
        os.remove(cleandir+"/total")
        length = len([name for name in os.listdir(filedir) if os.path.isfile(os.path.join(filedir, name))])
        for i in range(length):
            with open(filedir+"/bundle"+str(i),"r",encoding='utf_8') as f:
                    raw = f.read()
            os.remove(filedir+"/bundle"+str(i))
            with open(filedir+"/total","a",encoding='utf-8') as f:
                f.write(raw)
        with open(filedir+"/total","a",encoding='utf-8') as f:
            f.write("\"type\":\"online\",\"total\":1}")
        with open(filedir+"/total","r",encoding='utf-8') as f:
            raw = f.read()
        # 以下为正则提取
        rawcomment = re.findall(r"\"type\":\"online\",\"total\":\d{2,10}.*?\"type\":\"online\",\"total\":1}",raw)
        raw1 = re.findall(r"(\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\".{1,40}\",)",str(rawcomment))
        raw2 = re.sub(r"\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\"","",str(raw1))
        raw1 = re.sub(r"\'\,\s\'","",str(raw2))   
        raw2 = re.sub(r"\",\'\]","",str(raw1))
        raw1 = re.sub(r"\['","",str(raw2))
        result = re.sub(r"\"","",str(raw1))
        price1 = re.findall(r"\"coinType\":\"gold\",\"name\":\".{1,10}\",\"count\":\d*,\"price\":\d*",raw)
        price2 = re.sub(r"\"coinType\":\"gold\",\"name\":\".{1,10}\",\"count\":","",str(price1))
        rawtimes = re.findall(r"\'\d+,",price2)
        temp1times = re.findall(r"\d+",str(rawtimes))
        temp2times = re.sub(r"\'","",str(temp1times))
        temp1times = re.sub(r"\s","",str(temp2times))
        temp2times = re.sub(r"\[","",str(temp1times))
        times = re.sub(r"\]","",str(temp2times))
        rawvalue = re.findall(r"\:\d+\'",price2)
        temp1value = re.findall(r"\d+",str(rawvalue))
        temp2value = re.sub(r"\'","",str(temp1value))
        temp1value = re.sub(r"\s","",str(temp2value))
        temp2value = re.sub(r"\[","",str(temp1value))
        value = re.sub(r"\]","",str(temp2value))
        rawdhh = re.findall(r"\"level\":\d,\"count\":\d",raw)
        dhhprice1 = re.findall(r"\d,",str(rawdhh))
        dhhprice2 = re.sub(r",\'","",str(dhhprice1))
        dhhprice1 = re.sub(r"\'","",str(dhhprice2))
        dhhprice2 = re.sub(r"\s","",str(dhhprice1))
        dhhprice1 = re.sub(r"\[","",str(dhhprice2))
        dhhprice2 = re.sub(r"\]","",str(dhhprice1))
        dhhprice1 = re.sub(r"1","a",str(dhhprice2))
        dhhprice1 = re.sub(r"3","198",str(dhhprice2))
        dhhprice2 = re.sub(r"2","1998",str(dhhprice1))
        dhhprice = re.sub(r"a","19998",str(dhhprice2))
        dhhtimes1 = re.findall(r"\d\'",str(rawdhh))
        dhhtimes2 = re.sub(r"\"","",str(dhhtimes1))
        dhhtimes1 = re.sub(r"\'","",str(dhhtimes2))
        dhhtimes2 = re.sub(r"\s","",str(dhhtimes1))
        dhhtimes1 = re.sub(r"\[","",str(dhhtimes2))
        dhhtimes = re.sub(r"\]","",str(dhhtimes1))
        if result:
            print(str(uid[k])+" OK")
        else:   
            print(str(uid[k])+" FAIL") 
        #以下为提取信息处理
        raw3 = result.split(",")
        nameresult = pd.Series(raw3)
        namenum = nameresult.drop_duplicates().count()
        times1 = times.split(",")
        timeresult = pd.Series(times1)
        timeresult = pd.to_numeric(timeresult)
        value1 = value.split(",")
        valueresult = pd.Series(value1)
        valueresult = pd.to_numeric(valueresult)
        times2 = dhhtimes.split(",")
        timeresult2 = pd.Series(times2)
        timeresult2 = pd.to_numeric(timeresult2)
        value2 = dhhprice.split(",")
        valueresult2 = pd.Series(value2)
        valueresult2 = pd.to_numeric(valueresult2)
        money = np.sum(valueresult * timeresult) / 1000 + np.sum(valueresult2 * timeresult2)# 打赏
        with open(resultdir+"comments.csv","a",encoding='utf_8_sig') as f:
            f.write(str(namenum))
            if(k<(len(uid)-1)):
                f.write(',')
            else:
                f.write("\n")
        with open(resultdir+"income.csv","a",encoding='utf_8_sig') as f:
            f.write(str('%0.3f' % (money))+',')
            if(k<(len(uid)-1)):
                f.write(',')            
            else:
                f.write("\n") 