# -*- coding: utf-8 -*- 
import pymysql
import csv
import pandas as pd
import sys

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
# get confirmed_date from "K_COVID19.csv" and count
confirmed_date = data['confirmed_date']
sex = data['sex']

cdate_dic_male = {}
cdate_dic_female = {}

i=0
for date in list(confirmed_date):
    if sex[i]=='male':
        if date in cdate_dic_male.keys():
            cdate_dic_male[date] = cdate_dic_male[date] + 1
        else:
            cdate_dic_male[date] = 1
    else:
        if date in cdate_dic_female.keys():
            cdate_dic_female[date] = cdate_dic_female[date] + 1
        else:
            cdate_dic_female[date] = 1
    i=i+1

deceased_date = data['deceased_date']
sex = data['sex']
ddate_dic_male = {}
ddate_dic_female = {}

i=0
for date in list(deceased_date):
    if sex[i]=='male':
        if date in ddate_dic_male.keys():
            ddate_dic_male[date] = ddate_dic_male[date] + 1
        else:
            ddate_dic_male[date] = 1
    else:
        if date in ddate_dic_female.keys():
            ddate_dic_female[date] = ddate_dic_female[date] + 1
        else:
            ddate_dic_female[date] = 1
    i=i+1

# cdate_dic_male = sorted(cdate_dic_male.items())
# cdate_dic_female = sorted(cdate_dic_female.items())
# ddate_dic_male = sorted(ddate_dic_male.items())
# ddate_dic_female = sorted(ddate_dic_female.items())

# ?-?
date=[]
total_confirmed_male = 0
total_deceased_male = 0
total_confirmed_female = 0
total_deceased_female = 0


with open("../data/addtional_Timeinfo.csv", 'r') as file:
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

        # checking duplicate case_id & checking case_id == "NULL"
        if (line[col_list['date']] in date) or (line[col_list['date']] == "NULL") :
            continue
        else:
            date.append(line[col_list['date']])

        #make sql data & query
        sql_data_male = []
        sql_data_female = []

        sql_data_male.append(line[col_list['date']])
        sql_data_female.append(line[col_list['date']])
        sql_data_male.append("male")
        sql_data_female.append("female")

         # append "total number from confirmed_date" to sql_date list
        if line[col_list['date']] in cdate_dic_male.keys():
            total_confirmed_male = total_confirmed_male + cdate_dic_male[line[col_list['date']]]
        sql_data_male.append(total_confirmed_male)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_male.keys():
            total_deceased_male = total_deceased_male + ddate_dic_male[line[col_list['date']]]
        sql_data_male.append(total_deceased_male)
        if line[col_list['date']] in cdate_dic_female.keys():
            total_confirmed_female = total_confirmed_female + cdate_dic_female[line[col_list['date']]]
        sql_data_female.append(total_confirmed_female)
        # append "total number from deceased_date" to sql_date list
        if line[col_list['date']] in ddate_dic_female.keys():
            total_deceased_female = total_deceased_female + ddate_dic_female[line[col_list['date']]]
        sql_data_female.append(total_deceased_female)
        #---------------------------------------------------------------------------------------------------

        #Make query & execute
        query = """INSERT INTO `TimeGender`(gdate, sex, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_male = tuple(sql_data_male)

        #for debug
        try:
            cursor.execute(query, sql_data_male)
            print("[OK] Inserting [%s] to timeGender"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

        query = """INSERT INTO `TimeGender`(gdate, sex, confirmed, deceased) VALUES (%s,%s,%s,%s)"""
        sql_data_female = tuple(sql_data_female)

        #for debug
        try:
            cursor.execute(query, sql_data_female)
            print("[OK] Inserting [%s] to timeGender"%(line[col_list['date']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['date']],e))
            break

conn.commit()
cursor.close()
