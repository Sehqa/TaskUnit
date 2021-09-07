import sqlite3

class Db(object):

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
