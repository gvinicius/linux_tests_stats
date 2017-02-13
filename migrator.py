import py_db

def main():
    db = py_db.DataBase()
    db.create_schema()
    db.create_subsystems()
    db.create_versions()
    db.create_test_cases()

if __name__ == "__main__":
	main()
