""" This only drops the db. """
import py_db

def main():
    data_base = py_db.DataBase()
    data_base.drop()
    data_base.connect.close()

if __name__ == "__main__":
    main()

