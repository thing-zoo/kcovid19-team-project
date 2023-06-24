# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import sys
import getpass 
import pymysql
import csv
import math

#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='cathy77', 
                        password='mjwaw4025', 
                        db='K_COVID19', 
                        charset='utf8')

# Connection 으로부터 Cursor 생성
cursor = conn.cursor()
dup=[]
Hospital=[]
Hospital_capacity={}

#nearhospital구하는함수
def near_hospital(region):
    dis={ } #{ 'hid' : [dis, capacity, now] }
    
    for H in Hospital:
        distance = math.sqrt(pow((float(region[3])-float(H[4])), 2)+pow((float(region[4])-float(H[5])),2))
        dis[H[0]] = distance
    
    dis = sorted(dis.items(), key=lambda x :x[1])
    
    return dis
    
Hospital_id = []

with open("../data/Hospital.csv",encoding='UTF-8') as file:
    file_read=csv.reader(file)

    col_list = {
        'Hospital_id' : 0,
        'Hospital_name' : 1,
        'Hospital_province' : 2,
        'Hospital_city' : 3,
        'Hospital_latitude' : 4,
        'Hospital_longitude' : 5,
        'capacity' : 6,
        'now' : 7
    }

    for i,line in enumerate(file_read):

        #skip first line
        if not i:
            continue

        #checking duplicate case_id & chechking case_id == "NULL"
        if (line[col_list['Hospital_id']]in Hospital_id) or (line[col_list['Hospital_id']]=="NULL") :
            continue
        else:
            Hospital_id.append(line[col_list['Hospital_id']])

        #make sql data &query
        sql_data = []

        for idx in col_list.values() :
            if line[idx] == "NULL" :
                line[idx] = None
            else:
                line[idx] = line[idx].strip()

            sql_data.append(line[idx])
        query="""INSERT INTO `hospital`(hid,hname,hprovince,hcity,hlatitude,hlongitude,capacity,now) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_data=tuple(sql_data)

        #for debug
        try:
            cursor.execute(query,sql_data)
            print("[OK] Inserting [%s] to hospital"%(line[col_list['Hospital_id']]))
        except (pymysql.Error,pymysql.Warning) as e :
            if e.args[0] == 1062 : continue
            print('[Error] %s | %s'%(line[col_list['Hospital_id']],e))
            break
    conn.commit()

with open("../data/Hospital.csv",encoding='UTF-8') as file:
    file_read=csv.reader(file)

    col_list = {
        'Hospital_id' : 0,
        'Hospital_name' : 1,
        'Hospital_province' : 2,
        'Hospital_city' : 3,
        'Hospital_latitude' : 4,
        'Hospital_longitude' : 5,
        'capacity' : 6,
        'now' : 7
    }

    for i,line in enumerate(file_read):
        #skip first line
        if not i:
            continue
        #checking duplicate case_id & chechking case_id == "NULL"
        if (line[col_list['Hospital_id']]in dup) or (line[col_list['Hospital_id']]=="NULL") :
            continue
        else:
            dup.append(line[col_list['Hospital_id']])
            Hospital_capacity[line[col_list['Hospital_id']]]=[int(line[col_list['capacity']]), int(line[col_list['now']])]

        Hospital.append(line)


# 중복된 case 제거를 위해 checking list
dup = []
with open("../data/Region.csv",encoding='UTF-8') as file:
    file_read=csv.reader(file)

    rcol_list = {
        'code' : 0,
        'province' : 1,#이친구랑
        'city' : 2,#이친구를 통해 비교
        'latitude' : 3,
        'logitude' : 4,
    }

    hdis = {}
    for i,line in enumerate(file_read):
        #skip first line
        if not i:
            continue
        #checking duplicate case_id & chechking case_id == "NULL"
        if (line[rcol_list['code']]in dup) or (line[rcol_list['code']]=="NULL") :
            continue
        else:
            dup.append(line[rcol_list['code']])
        
        key = (line[rcol_list['province']], line[rcol_list['city']])
        hdis[key] = near_hospital(line)

    #patientinfo 가져오기
    query="""select patient_id, province, city from patientinfo"""
    cursor.execute(query)
    rows = cursor.fetchall() #row에 다 저장되어있음! row는 튜플
    patient_hos={}

    for pid, pp, pc in rows:
        passing=0
        if pc==None or pc=='etc':
            pc=pp
        for k, near in hdis.items():
            if k[0] != pp or k[1] != pc:
                continue
            for key, h in near:#near은 dict
                passing=1
                if Hospital_capacity[key][0]<=Hospital_capacity[key][1] :
                    continue
                patient_hos[pid]=key
                Hospital_capacity[key][1]=Hospital_capacity[key][1]+1
                break
        if(passing==0) : patient_hos[pid]=None
    
    # print(len(patient_hos))
    # query="""select patient_id from patientinfo"""
    # cursor.execute(query)
    # rows = cursor.fetchall() #row에 다 저장되어있음! row는 튜플
    # i=0

    for pid, data in patient_hos.items():
        query="""UPDATE `patientinfo` SET hospital_id=(%s) WHERE patient_id=(%s)"""
        # query="""UPDATE TABLE SET hospital_id (%s) where patient_id = (%s) """
        sql_data=(data, pid)
        # i=i+1
        try:
            cursor.execute(query,sql_data)
            print("[OK] Inserting to patient")
        except (pymysql.Error,pymysql.Warning) as e :
            if e.args[0] == 1062 : continue
            print('[Error] %s'%(e))
            break

    for hid, now_cap in Hospital_capacity.items():
        query="""UPDATE `hospital` SET now=(%s) WHERE hid=(%s)"""
        sql_data=(now_cap[1], hid)
        try:
            cursor.execute(query,sql_data)
            print("[OK] Inserting to hospital")
        except (pymysql.Error,pymysql.Warning) as e :
            if e.args[0] == 1062 : continue
            print('[Error] %s'%(e))
            break
    

    conn.commit()
    cursor.close()