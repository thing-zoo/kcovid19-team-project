# -*- coding: utf-8 -*- 
import pymysql
import csv
import pandas as pd

#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='cathy77', 
                        password='mjwaw4025', 
                        db='K_COVID19', 
                        charset='utf8')
# Connection 으로부터 Cursor 생성
cursor = conn.cursor()

data = pd.read_csv('../data/K_COVID19.csv')

# Using Hashing
# get age from "K_COVID19.csv" and count
confirmed_date = data['confirmed_date']
age = data['age']

cdate_dic_0s = {}
cdate_dic_10s = {}
cdate_dic_20s = {}
cdate_dic_30s = {}
cdate_dic_40s = {}
cdate_dic_50s = {}
cdate_dic_60s = {}
cdate_dic_70s = {}
cdate_dic_80s = {}
cdate_dic_90s = {}
cdate_dic_100s = {}

i=0
for date in list(confirmed_date):
    if age[i]=='0s':
        if date in cdate_dic_0s.keys():
            cdate_dic_0s[date] = cdate_dic_0s[date] + 1
        else:
            cdate_dic_0s[date] = 1
    elif age[i]=='10s':
        if date in cdate_dic_10s.keys():
            cdate_dic_10s[date] = cdate_dic_10s[date] + 1
        else:
            cdate_dic_10s[date] = 1
    elif age[i]=='20s':
        if date in cdate_dic_20s.keys():
            cdate_dic_20s[date] = cdate_dic_20s[date] + 1
        else:
            cdate_dic_20s[date] = 1
    elif age[i]=='30s':
        if date in cdate_dic_30s.keys():
            cdate_dic_30s[date] = cdate_dic_30s[date] + 1
        else:
            cdate_dic_30s[date] = 1
    elif age[i]=='40s':
        if date in cdate_dic_40s.keys():
            cdate_dic_40s[date] = cdate_dic_40s[date] + 1
        else:
            cdate_dic_40s[date] = 1
    elif age[i]=='50s':
        if date in cdate_dic_50s.keys():
            cdate_dic_50s[date] = cdate_dic_50s[date] + 1
        else:
            cdate_dic_50s[date] = 1
    elif age[i]=='60s':
        if date in cdate_dic_60s.keys():
            cdate_dic_60s[date] = cdate_dic_60s[date] + 1
        else:
            cdate_dic_60s[date] = 1
    elif age[i]=='70s':
        if date in cdate_dic_70s.keys():
            cdate_dic_70s[date] = cdate_dic_70s[date] + 1
        else:
            cdate_dic_70s[date] = 1
    elif age[i]=='80s':
        if date in cdate_dic_80s.keys():
            cdate_dic_80s[date] = cdate_dic_80s[date] + 1
        else:
            cdate_dic_80s[date] = 1
    elif age[i]=='90s':
        if date in cdate_dic_90s.keys():
            cdate_dic_90s[date] = cdate_dic_90s[date] + 1
        else:
            cdate_dic_90s[date] = 1
    elif age[i]=='100s':
        if date in cdate_dic_100s.keys():
            cdate_dic_100s[date] = cdate_dic_100s[date] + 1
        else:
            cdate_dic_100s[date] = 1
    i=i+1

deceased_date = data['deceased_date']
age = data['age']

ddate_dic_0s = {}
ddate_dic_10s = {}
ddate_dic_20s = {}
ddate_dic_30s = {}
ddate_dic_40s = {}
ddate_dic_50s = {}
ddate_dic_60s = {}
ddate_dic_70s = {}
ddate_dic_80s = {}
ddate_dic_90s = {}
ddate_dic_100s = {}

i=0
for date in list(deceased_date):
    if age[i]=='0s':
        if date in ddate_dic_0s.keys():
            ddate_dic_0s[date] = ddate_dic_0s[date] + 1
        else:
            ddate_dic_0s[date] = 1
    elif age[i]=='10s':
        if date in ddate_dic_10s.keys():
            ddate_dic_10s[date] = ddate_dic_10s[date] + 1
        else:
            ddate_dic_10s[date] = 1
    elif age[i]=='20s':
        if date in ddate_dic_20s.keys():
            ddate_dic_20s[date] = ddate_dic_20s[date] + 1
        else:
            ddate_dic_20s[date] = 1
    elif age[i]=='30s':
        if date in ddate_dic_30s.keys():
            ddate_dic_30s[date] = ddate_dic_30s[date] + 1
        else:
            ddate_dic_30s[date] = 1
    elif age[i]=='40s':
        if date in ddate_dic_40s.keys():
            ddate_dic_40s[date] = ddate_dic_40s[date] + 1
        else:
            ddate_dic_40s[date] = 1
    elif age[i]=='50s':
        if date in ddate_dic_50s.keys():
            ddate_dic_50s[date] = ddate_dic_50s[date] + 1
        else:
            ddate_dic_50s[date] = 1
    elif age[i]=='60s':
        if date in ddate_dic_60s.keys():
            ddate_dic_60s[date] = ddate_dic_60s[date] + 1
        else:
            ddate_dic_60s[date] = 1
    elif age[i]=='70s':
        if date in ddate_dic_70s.keys():
            ddate_dic_70s[date] = ddate_dic_70s[date] + 1
        else:
            ddate_dic_70s[date] = 1
    elif age[i]=='80s':
        if date in ddate_dic_80s.keys():
            ddate_dic_80s[date] = ddate_dic_80s[date] + 1
        else:
            ddate_dic_80s[date] = 1
    elif age[i]=='90s':
        if date in ddate_dic_90s.keys():
            ddate_dic_90s[date] = ddate_dic_90s[date] + 1
        else:
            ddate_dic_90s[date] = 1
    elif age[i]=='100s':
        if date in ddate_dic_100s.keys():
            ddate_dic_100s[date] = ddate_dic_100s[date] + 1
        else:
            ddate_dic_100s[date] = 1
    i=i+1

date=[]
total_confirmed_0s = 0
total_deceased_0s = 0

total_confirmed_10s = 0
total_deceased_10s = 0

total_confirmed_20s = 0
total_deceased_20s = 0

total_confirmed_30s = 0
total_deceased_30s = 0

total_confirmed_40s = 0
total_deceased_40s = 0

total_confirmed_50s = 0
total_deceased_50s = 0

total_confirmed_60s = 0
total_deceased_60s = 0

total_confirmed_70s = 0
total_deceased_70s = 0

total_confirmed_80s = 0
total_deceased_80s = 0

total_confirmed_90s = 0
total_deceased_90s = 0

total_confirmed_100s = 0
total_deceased_100s = 0

with open('../data/addtional_Timeinfo.csv', 'r') as file:
    file_read = csv.reader(file)

    # Use column 1(date), 2(test), 3(negative)
    # index = column - 1
    col_list = { 
        'date' :0,
        }

    for i,line in enumerate(file_read):

        #Skip first line
        if not i:                           
            continue

        # checking duplicate date & checking date == "NULL"
        if (line[col_list['date']] in date) or (line[col_list['date']] == "NULL") :
            continue
        else:
            date.append(line[col_list['date']])
       
        #make sql data & query
        sql_data_0s = []
        sql_data_10s = []
        sql_data_20s = []
        sql_data_30s = []
        sql_data_40s = []
        sql_data_50s = []
        sql_data_60s = []
        sql_data_70s = []
        sql_data_80s = []
        sql_data_90s = []
        sql_data_100s = []

        sql_data_0s.append(line[col_list['date']])
        sql_data_10s.append(line[col_list['date']])
        sql_data_20s.append(line[col_list['date']])
        sql_data_30s.append(line[col_list['date']])
        sql_data_40s.append(line[col_list['date']])
        sql_data_50s.append(line[col_list['date']])
        sql_data_60s.append(line[col_list['date']])
        sql_data_70s.append(line[col_list['date']])
        sql_data_80s.append(line[col_list['date']])
        sql_data_90s.append(line[col_list['date']])
        sql_data_100s.append(line[col_list['date']])

        sql_data_0s.append("0s")
        sql_data_10s.append("10s")
        sql_data_20s.append("20s")
        sql_data_30s.append("30s")
        sql_data_40s.append("40s")
        sql_data_50s.append("50s")
        sql_data_60s.append("60s")
        sql_data_70s.append("70s")
        sql_data_80s.append("80s")
        sql_data_90s.append("90s")
        sql_data_100s.append("100s")

        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_0s.keys():
            total_confirmed_0s = total_confirmed_0s + cdate_dic_0s[line[col_list['date']]]
        sql_data_0s.append(total_confirmed_0s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_0s.keys():
            total_deceased_0s = total_deceased_0s + ddate_dic_0s[line[col_list['date']]]
        sql_data_0s.append(total_deceased_0s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_10s.keys():
            total_confirmed_10s = total_confirmed_10s + cdate_dic_10s[line[col_list['date']]]
        sql_data_10s.append(total_confirmed_10s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_10s.keys():
            total_deceased_10s = total_deceased_10s + ddate_dic_10s[line[col_list['date']]]
        sql_data_10s.append(total_deceased_10s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_20s.keys():
            total_confirmed_20s = total_confirmed_20s + cdate_dic_20s[line[col_list['date']]]
        sql_data_20s.append(total_confirmed_20s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_20s.keys():
            total_deceased_20s = total_deceased_20s + ddate_dic_20s[line[col_list['date']]]
        sql_data_20s.append(total_deceased_20s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_30s.keys():
            total_confirmed_30s = total_confirmed_30s + cdate_dic_30s[line[col_list['date']]]
        sql_data_30s.append(total_confirmed_30s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_30s.keys():
            total_deceased_30s = total_deceased_30s + ddate_dic_30s[line[col_list['date']]]
        sql_data_30s.append(total_deceased_30s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_40s.keys():
            total_confirmed_40s = total_confirmed_40s + cdate_dic_40s[line[col_list['date']]]
        sql_data_40s.append(total_confirmed_40s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_40s.keys():
            total_deceased_40s = total_deceased_40s + ddate_dic_40s[line[col_list['date']]]
        sql_data_40s.append(total_deceased_40s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_50s.keys():
            total_confirmed_50s = total_confirmed_50s + cdate_dic_50s[line[col_list['date']]]
        sql_data_50s.append(total_confirmed_50s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_50s.keys():
            total_deceased_50s = total_deceased_50s + ddate_dic_50s[line[col_list['date']]]
        sql_data_50s.append(total_deceased_50s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_60s.keys():
            total_confirmed_60s = total_confirmed_60s + cdate_dic_60s[line[col_list['date']]]
        sql_data_60s.append(total_confirmed_60s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_60s.keys():
            total_deceased_60s = total_deceased_60s + ddate_dic_60s[line[col_list['date']]]
        sql_data_60s.append(total_deceased_60s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_70s.keys():
            total_confirmed_70s = total_confirmed_70s + cdate_dic_70s[line[col_list['date']]]
        sql_data_70s.append(total_confirmed_70s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_70s.keys():
            total_deceased_70s = total_deceased_70s + ddate_dic_70s[line[col_list['date']]]
        sql_data_70s.append(total_deceased_70s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_80s.keys():
            total_confirmed_80s = total_confirmed_80s + cdate_dic_80s[line[col_list['date']]]
        sql_data_80s.append(total_confirmed_80s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_80s.keys():
            total_deceased_80s = total_deceased_80s + ddate_dic_80s[line[col_list['date']]]
        sql_data_80s.append(total_deceased_80s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_90s.keys():
            total_confirmed_90s = total_confirmed_90s + cdate_dic_90s[line[col_list['date']]]
        sql_data_90s.append(total_confirmed_90s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_90s.keys():
            total_deceased_90s = total_deceased_90s + ddate_dic_90s[line[col_list['date']]]
        sql_data_90s.append(total_deceased_90s)
        # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_100s.keys():
            total_confirmed_100s = total_confirmed_100s + cdate_dic_100s[line[col_list['date']]]
        sql_data_100s.append(total_confirmed_100s)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_100s.keys():
            total_deceased_100s = total_deceased_100s + ddate_dic_100s[line[col_list['date']]]
        sql_data_100s.append(total_deceased_100s)

         #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_0s = tuple(sql_data_0s)

        #for debug
        try:
            cursor.execute(query, sql_data_0s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_10s = tuple(sql_data_10s)

        #for debug
        try:
            cursor.execute(query, sql_data_10s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_20s = tuple(sql_data_20s)

        #for debug
        try:
            cursor.execute(query, sql_data_20s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_30s = tuple(sql_data_30s)

        #for debug
        try:
            cursor.execute(query, sql_data_30s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_40s = tuple(sql_data_40s)

        #for debug
        try:
            cursor.execute(query, sql_data_40s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_50s = tuple(sql_data_50s)

        #for debug
        try:
            cursor.execute(query, sql_data_50s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_60s = tuple(sql_data_60s)

        #for debug
        try:
            cursor.execute(query, sql_data_60s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_70s = tuple(sql_data_70s)

        #for debug
        try:
            cursor.execute(query, sql_data_70s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_80s = tuple(sql_data_80s)

        #for debug
        try:
            cursor.execute(query, sql_data_80s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_90s = tuple(sql_data_90s)

        #for debug
        try:
            cursor.execute(query, sql_data_90s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

                #Make query & execute
        query = """INSERT INTO `TimeAge`(adate, age, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_100s = tuple(sql_data_100s)

        #for debug
        try:
            cursor.execute(query, sql_data_100s)
            print("[OK] Inserting [%s] to timeAge"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

        
conn.commit()
cursor.close()