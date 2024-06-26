import pymysql

from lib.settings import MYSQL_HOST, MYSQL_DB, MYSQL_PASSWORD, MYSQL_USERNAME


class Connection:
    def __init__(self):
        self.con = pymysql.connect(
            host=MYSQL_HOST,
            port=3306,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB,
            autocommit=True,  # 결과 DB 반영 (Insert or update)
            charset='utf8mb4',  # 한글처리 (charset = 'utf8')
            cursorclass=pymysql.cursors.DictCursor  # DB조회시 컬럼명을 동시에 보여줌
        )
        self.cur = self.con.cursor()

    def select_one(self, sql, args=None):
        self.cur.execute(sql, args)
        result = self.cur.fetchone()
        self.cur.close()
        self.con.close()
        return result

    def select_all(self, sql, args=None):
        self.cur.execute(sql, args)
        result = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return result

    def save_one(self, sql, args=None):
        result = self.cur.execute(sql, args)
        self.cur.close()
        self.con.close()
        return result

    def save_all(self, sql, args=None):
        result = self.cur.executemany(sql, args)
        self.cur.close()
        self.con.close()
        return result