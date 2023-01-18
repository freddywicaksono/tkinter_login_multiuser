from db import DBConnection as mydb
import hashlib

class Users:
    def __init__(self):
       self.__username = None
       self.__password = None
       self.__rolename = None
       self.conn = None
       self.affected = None
       self.result = None
    
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


    @property
    def rolename(self):
        return self.__rolename

    @rolename.setter
    def rolename(self, value):
        self.__rolename = value
        
    def Login(self):
        a=str(self.__username)
        pwd = hashlib.md5(self.__password.encode("utf-8")).hexdigest()
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
   