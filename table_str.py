#!/usr/bin/python

import psycopg2
import random
import time

# 随机生成时间戳
def str_timestamp(start,end):
    start_year = (start,1,1,0,0,0,0,0,0)
    end_year = (end,1,1,0,0,0,0,0,0)
    random_int = random.randint(time.mktime(start_year),time.mktime(end_year))
    timestamp = time.strftime("%Y%m%d%H%M%S",time.localtime(random_int))
    return timestamp
    
#创建可变长度字符串函数
def str_len(nu_len):
    char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ''.join(random.sample(char_list,nu_len))
    return string

#创建可变长度数字
def int_len(start,end):
    num = random.randint(start,end)
    return num

#创建多位可选字符串数组
def list_str():
    list_char = ['A001','A002','A003','A004','A005','A006']
    string = random.choice(list_char)
    return string

#创建多位可选字符串数组
def list_s(list_char):
#    list_char = ['A001','A002','A003','A004','A005','A006']
    string = random.choice(list_char)
    return string
    
#创建指定字符串
string_str = 'A0281'

#定义变量
n = 0
#输出时间


#创建pg数据库连接
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
cur = conn.cursor()
print("成功连接PG")

#加载SQL
SQL = 'INSERT INTO TMP_T0182_TBSPAMT0_H_TMP (CST_ACCNO ,DEP_LGL_FRZ_AMT ,ITRT_BSN_FRZ_AMT ,ORD_BSN_FRZ_AMT ,LGL_ST_FRZ_CNT) VALUES(%s,%s,%s,%s,%s);'
print('加载SQL，准备造数。。。')

for i in range(10000):
    date_dt = str_timestamp(1980,2020)
    list_char = ['028004','028003']
    list_c = ['009017','009017']
    #定义数据库字段数据
    T1 = '62' + str(int_len(1000000000,9999999999))
    T2 = int_len(0,99999)
    T3 = int_len(0,99999)
    T4 = int_len(0,99999)
    T5 = int_len(0,99)

    #待插入数据
    VA = (T1 ,T2 ,T3 ,T4 ,T5)

    #执行SQL
    cur.execute(SQL,VA)
    
    if(i//100 > n):
        n = i//100
        print(n)
        
conn.commit()
conn.close()    
print("插入成功")







