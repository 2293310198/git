#coding:utf-8
import MySQLdb
import os,sys,time


sgkint=32



def crea_table(sgkint):
    db=MySQLdb.connect(host='localhost',user='root',passwd='root',db='sgksite',charset="utf8") 
    cursor=db.cursor()
    try:
        #创建索引的语句
        #print "CREATE TABLE sgk_"+str(sgkint)+" (`id` bigint(10) NOT NULL AUTO_INCREMENT,`email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,PRIMARY KEY (`id`) USING BTREE,INDEX `email`(`email`) USING BTREE) ENGINE = MyISAM AUTO_INCREMENT = 0 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;SET FOREIGN_KEY_CHECKS = 1"
        cursor.execute ("CREATE TABLE sgk_"+str(sgkint)+" (`id` bigint(10) NOT NULL AUTO_INCREMENT,`email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,PRIMARY KEY (`id`) USING BTREE,INDEX `email`(`email`) USING BTREE) ENGINE = MyISAM AUTO_INCREMENT = 0 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;SET FOREIGN_KEY_CHECKS = 1")
        print u"创建表成功"
    except Exception, e:
            print e
    
    cursor.close()
    db.close()


f = []
for root,dirs,files in  os.walk('D:\BreachCompilation\data'):
    for name in files:
        if 'symbols' not in name:
            x= os.path.join(root,name)
            f.append(x)
            





def file_readlines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def datas(sgkint,email,password):
    try:
        #print "INSERT INTO sgk_%s (email,password) VALUES ( '%s','%s')" % (str(sgkint),email,password)
        cursor.execute("INSERT INTO sgk_%s (email,password) VALUES ( '%s','%s')" % (str(sgkint),email,password))
    except Exception, e:
        print e
        


def chuli_data(li):
    x_array=[]
    li = li.strip('\n')
    try:
        if ':' in li:
            x_array=li.split(":")
                
        elif ';' in li:
            x_array=li.split(";")   
    except:
        print u"没有找到分割字符"
    
    return x_array




conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='sgksite',charset="utf8") 
cursor=conn.cursor()


#计算器


crea_table(sgkint)

count_f = len(f)
ii=1

for ff in f:
    lines = file_readlines(ff)
    count_line = len(lines)

    for li in lines:
        
        x_array=chuli_data(li)
        if x_array:
            email=MySQLdb.escape_string(x_array[0])
            password=MySQLdb.escape_string(x_array[1])
        
        
        print ff+" "+str(count_f)+" "+str(count_line)+" "+str(ii)+' '+str(sgkint)
        try:
            #print "INSERT INTO sgk_%s (email,password) VALUES ( '%s','%s')" % (str(sgkint),email,password)
            cursor.execute("INSERT INTO sgk_%s (email,password) VALUES ( '%s','%s')" % (str(sgkint),email,password))
          
        except Exception, e:
            print e
        #if cursor.lastrowid >=1000000:
        ii=ii+1

        if ii >30000000:
            sgkint=sgkint+1
           
            crea_table(sgkint)
            time.sleep(5)
            ii=1
        count_line=count_line-1
    count_f=count_f-1
