import MySQLdb
import sqlalchemy as sqa

class Init_db:
    def __init__(self):
        self.engine = sqa.create_engine("mysql://root:ldd01@localhost/", echo=True)


