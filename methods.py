import requests
import datetime
import time


import timestring
import requests
from datetime import timedelta
import sqlite3

class Met(object):
    # headers,params,body,
    # Метод для htpp get
    def _gethttp(urls, paramss, headerss):
        r = requests.get(url=urls, params=paramss, headers=headerss)
        return r
    #метод для post
    def _posthttp(urls, paramss, headerss, bodys):
        r = requests.post(url=urls, params=paramss, headers=headerss, data=bodys)
        return r

    # Метод для проверки вхождения даты в интервал
    @staticmethod
    def _ininterval(date1, date2, date3):
        a=timestring.Date(date1).date
        b=timestring.Date(date2).date
        c=timestring.Date(date3).date
        return (a<c<b)

    # Метод для вычисления разницы между текущей и заданной датой
    def _datedifference(date):
        a = timestring.Date(date).date
        nowdate = datetime.datetime.now()
        if (a < nowdate):
            return (nowdate - a)
        elif (a > nowdate):
            return (a - nowdate)

    #метод для сравнения двух дат
    def _comparsdate(date1, date2):
        date1 = timestring.Date(date1).date
        date2 = timestring.Date(date2).date
        if (date1 > date2):
            return (str(date1) + '>' + str(date2))
        elif (date1 < date2):
            return (str(date2) + '>' + str(date1))
        elif (date1 == date2):
            return (str(date1) + '=' + str(date2))

    #Метод для сравнения списков
    def _compars_mass(a,b):
        for i in range(0, len(a)):
            if (a[i]!=b[i]):
                 return(a[i],b[i])



    def once(func):
        def wrapper(*args):
            with open(args[0], 'w') as ang:
                ang.write(str(func(*args)))
            result = func(*args)
            return result

        return wrapper

    @once
    def _logger(filename, url, level):
        rss = requests.get(url)
        if (level == 1):
            return (url, rss.text)
        elif (level == 2):
            return (url, rss.status_code)
        elif (level == 3):
            currenttime = datetime.datetime.now().time()
            return (url, rss.status_code, currenttime, rss.text)

    def _dictfrombd (none):
        dict1 = {}
        keylist = []
        resultlist = []
        dictlist = []
        conn = sqlite3.connect('mydb.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INT PRIMARY KEY,
           fname TEXT,
           lname TEXT,
           gender TEXT);
        """)
        conn.commit()
      #  cur.execute("""INSERT INTO users(userid, fname, lname, gender)
      #    VALUES('00021', 'Alex4', 'Smith4', 'male4');""")
     #   conn.commit()
        cur.execute("SELECT * FROM users;")
        colnames = cur.description
        for i in range(0, len(colnames)):
            keylist.append(colnames[i][0])

        for i in range(0, len(keylist)):
            for row in cur.execute('SELECT * FROM users;'):
                resultlist.append(row[i])
            dict1[keylist[i]] = resultlist
            dictlist.append(dict1)
            dict1 = {}
            resultlist = []
        return (dictlist)

    def testfunc(dd):
        return True

    def mainfunc(testfun, timeout, period):
        tim = timeout
        shet = 0
        for i in range(0, timeout):
            if (testfun):
                return ('Success')
                exit(0)
            elif (tim <= 0):
                return ('timeout')
                exit(0)
            else:
                shet = shet + 5
                tim = tim - period
                if (testfun):
                    return (print('Функция ' + 'вызывалась в течении ' + str(shet) + ' секунд'))
                else:
                    time.sleep(5)