import MarksheetBean
from MarksheetBean import *

import pymysql


class MarksheetDao():

    def nextPk(self):
        r = 0
        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "select max(roll_No) from marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for d in result:
            r = d[0]
        return r + 1


    def add(self,mb):
        pk = MarksheetDao.nextPk(mb)

        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "insert into marksheet values (%s, %s, %s, %s, %s)"
            data = (pk, mb.getName(), mb.getPhysics(), mb.getChemistry(), mb.getMaths() )
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()

    def update(self,mb):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "update marksheet set name = %s , physics= %s, chemistry = %s , maths = %s   where roll_no= %s"
            data = ( mb.getName(), mb.getPhysics(), mb.getChemistry(), mb.getMaths() ,mb.getRollNo())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()

    def delete(self,mb):
        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "delete from marksheet where roll_no = %s "
            data = ( mb.getRollNo())
            cursor.execute(sql, args=data)
            connection.commit()
        connection.close()

    def getRollNo(self, mb):

        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = " select * from marksheet where roll_no = %s "
            data = (mb.getRollNo())

            cursor.execute(sql, args=data)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for d in result:
            print(d[0], "\t", d[1], "\t", d[2], "\t", d[3], "\t", d[4])

    def getMeritList(self):

        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "select roll_no , name, physics, chemistry, maths, (physics+chemistry+maths) as total from marksheet where physics>=33 and chemistry>=33 and maths>=33 " \
                  "order by total desc limit 5 "

            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
        connection.close()
        for d in result:
            print(d[0], "\t", d[1], "\t", d[2], "\t", d[3], "\t", d[4],  "\t", d[5])


    def search(self):
        result = ""
        connection = pymysql.connect(host="localhost", user="root", password="root", db="vikash")
        with connection.cursor() as cursor:
            sql = "select * from marksheet  "

            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for d in result:
            print(d[0], "\t", d[1], "\t", d[2], "\t", d[3], "\t", d[4])


