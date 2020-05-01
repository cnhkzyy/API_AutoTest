import pymysql
from common.read_cfg import *


class ReadMysql:

    def __init__(self):

        #数据库连接
        try:
            self.conn = pymysql.Connect(host=host, user=user, password=password, db=db, port=port, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise e


    #查找所有数据
    def select_all_data(self, select_sql):
        self.cursor.execute(select_sql)
        all_data = self.cursor.fetchall()
        return all_data


    #获取一条数据
    def select_one_data(self, select_sql):
        self.cursor.execute(select_sql)
        one_data = self.cursor.fetchone()
        return one_data


    #更新数据
    def update_data(self, update_sql):
        try:
            self.cursor.execute(update_sql)
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            return False


    #关闭数据库连接
    def close_db(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    ReadMysql().select_one_data("select * from member where MobilePhone=13113745100 and LeaveAmount=200;")


