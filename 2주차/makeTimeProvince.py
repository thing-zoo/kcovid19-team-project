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

province = data['province']
pro_dic = {}    #{'province':[{cdate_dic}, {rdate_dic}, {ddate_dic}]}
total = {}      #{'province':[total_confirmed, total_released, total_deceased]}
for p in list(province):
    if p not in pro_dic.keys():
        pro_dic[p] = []
        total[p] = [0, 0, 0]

#print(pro_dic)

# Using Hashing
# get date from "K_COVID19.csv" and count
confirmed_date = data['confirmed_date']
released_date = data['released_date']
deceased_date = data['deceased_date']
for p in pro_dic.keys():
    cdate_dic = {}
    rdate_dic = {}
    ddate_dic = {}

    for i, date in enumerate(list(confirmed_date)):
        if province[i] != p:
            continue
        if date in cdate_dic.keys():
            cdate_dic[date] = cdate_dic[date] + 1
        else:
            cdate_dic[date] = 1
    
    for i, date in enumerate(list(released_date)):
        if province[i] != p:
            continue
        if date in rdate_dic.keys():
            rdate_dic[date] = rdate_dic[date] + 1
        else:
            rdate_dic[date] = 1

    for i, date in enumerate(list(deceased_date)):
        if province[i] != p:
            continue
        if date in ddate_dic.keys():
            ddate_dic[date]= ddate_dic[date]+1
        else:
            ddate_dic[date] = 1

    pro_dic[p].append(cdate_dic)
    pro_dic[p].append(rdate_dic)
    pro_dic[p].append(ddate_dic)

    # print(p)
    # print(pro_dic[p][1])
    # print(pro_dic[p][2])


# 중복된 case 제거를 위해 checking list & variable
date = []
with open("../data/addtional_Timeinfo.csv", 'r') as file:
    file_read = csv.reader(file)

    # index = column - 1
    col_list = { 
        'date' :0
    }

    for i,line in enumerate(file_read):

        #Skip first line
        if not i:                           
            continue

        d = line[col_list['date']]
        # checking duplicate case_id & checking case_id == "NULL"
        if (d in date) or (d == "NULL") :
            continue
        else:
            date.append(d)

        for p, dic in pro_dic.items():
            #make sql data & query
            sql_data = []
            sql_data.append(d)
            sql_data.append(p)
            # append "total number from confirmed_date" to sql_date list
            if d in dic[0].keys():
                total[p][0] = total[p][0] + dic[0][d]
            sql_data.append(total[p][0])
            # append "total number from released_date" to sql_date list
            if d in dic[1].keys():
                total[p][1] = total[p][1] + dic[1][d]
            sql_data.append(total[p][1])
            # append "total number from deceased_date" to sql_date list
            if d in dic[2].keys():
                total[p][2] = total[p][2] + dic[2][d]
            sql_data.append(total[p][2])

            #Make query & execute
            query = """INSERT INTO `timeProvince`(pdate, province, confirmed, released, deceased) VALUES (%s,%s,%s,%s,%s)"""
            sql_data = tuple(sql_data)
            #print(sql_data)
            #for debug
            try:
                cursor.execute(query, sql_data)
                print("[OK] Inserting [%s] to timeProvince"%(d))
            except (pymysql.Error, pymysql.Warning) as e :
                # print("[Error]  %s"%(pymysql.IntegrityError))
                if e.args[0] == 1062: continue
                print('[Error] %s | %s'%(d,e))
                break

conn.commit()
cursor.close()
