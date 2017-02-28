import py_db

def main():
    data_base = py_db.DataBase()
    data_base.create_schema()
    data_base.create_subsystems()
    data_base.create_versions()
    data_base.create_test_cases()
    data_base.create_test_case_subsystem_versions()
    data_base.connect.close()

if __name__ == "__main__":
    main()
