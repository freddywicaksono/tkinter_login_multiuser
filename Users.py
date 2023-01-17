from db import DBConnection as mydb
import hashlib

class Users:

   def Login(self, username, password):
       a=str(username)
       pwd = hashlib.md5(password.encode("utf-8")).hexdigest()
       b=a.strip()
       self.conn = mydb()
       sql="SELECT * FROM users WHERE username='" + b + "' and password='" + pwd + "'"
       self.result = self.conn.findOne(sql)
       val = []
       if(self.result!=None):
           self.__username = self.result[1]
           self.__password = self.result[2]
           self.__rolename = self.result[3]
           self.affected = self.conn.cursor.rowcount
           val.append('True')
           val.append(self.__rolename)
       else:
           self.__username = ''
           self.__password = ''
           self.__rolename = ''
           self.affected = 0
           val.append('')
           val.append('')
       self.conn.disconnect
       return val
   