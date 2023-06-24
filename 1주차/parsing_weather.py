# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import sys
import getpass 
import pymysql
import csv

#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='cathy77', 
                        password='mjwaw4025', 
                        db='K_COVID19', 
                        charset='utf8')

# Connection 으로부터 Cursor 생성
cursor = conn.cursor()

# 중복된 case 제거를 위해 checking list
keyData=[]
with open("../data/K_COVID19.csv", 'r') as file:
    file_read = csv.reader(file)

    col_list = { 
        'region_code' :23,
        'province' :4,
        'confirmed_date' : 10,
        'avg_temp' : 14,
        'min_temp' : 15,
        'max_temp' :16,
        }

    for i,line in enumerate(file_read):

        #Skip first line
        if not i:                           
            continue

        # checking duplicate region_code & checking region_code == "NULL"
        if (line[col_list['confirmed_date']] == "NULL") or (line[col_list['region_code']] == "NULL"):
            continue
        if ([line[col_list['confirmed_date']], line[col_list['region_code']]] in keyData):
            continue
        else:
            data=[]
            data.append(line[col_list['confirmed_date']])
            data.append( line[col_list['region_code']])
            keyData.append(data)

        #make sql data & query
        sql_data = []
        #print(line)
        #"NULL" -> None (String -> null)
        #print(col_list.values())
        for idx in col_list.values() :
            if line[idx] == "NULL" :
                line[idx] = None
            else:
                line[idx] = line[idx].strip()

            sql_data.append(line[idx])
        #print(sql_data)
        query = """INSERT INTO `WEATHER`(region_code, province, wdate, avg_temp, min_temp, max_temp) VALUES (%s,%s,%s,%s,%s,%s)"""
        sql_data = tuple(sql_data)
        #print(sql_data)
        #for debug
        try:
            cursor.execute(query, sql_data)
            print("[OK] Inserting [%s] to Weather"%(data))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['region_code']],e))
            break

conn.commit()
cursor.close()

print(len(keyData))