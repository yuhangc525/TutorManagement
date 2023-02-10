import pymysql


class MysqlHelper:
    def __init__(self):
        self._conn = self.connect()
        self._cursor = self._conn.cursor()

    # 连接数据库
    def connect(self):
        try:
            conn = pymysql.connect(host="localhost",
                                   user="root",
                                   password="cyh",
                                   database="tutor")
            return conn
        except pymysql.Error as e:
            print("连接数据库失败" + str(e))

    # 查询所有家教信息
    def selectAll(self):
        sql = "select * from tutor_information order by number desc "
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
            return result
        except Exception as e:
            print("sql语句执行错误" + str(e))

    def updateOne(self):
        sql = "update tutor_information set "


if __name__ == '__main__':
    helper = MysqlHelper()
    helper.selectAll()
