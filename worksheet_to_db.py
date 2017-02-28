""" This module extracts linux test evolution's data from worksheets to a db.  """
import os
import xlrd
import py_db

""" Relative path to linux tests data """
root = "../evolution/"

class Version:
    def __init__(self, name):
        self._name = name
        self._subsystems = []

class Subsystem:
    def __init__(self, name):
        self._name = name
        self._test_cases = []	
    def __str__(self):
        header = "----------------------------------"
        test_cases = ""
        for i in range(0, len(self._test_cases)):
            test_cases += str(self._test_cases[i]._name) + "\n"
        return 	str(header + "\n" + self._name + "\n" + header + "\n" + test_cases)

class Test_case:
    def __init__(self, name):
        self._name = name
    def __str__(self):	
        return str(self._name)

""" Method the implements the conversion """
def main():
    data_base = py_db.DataBase()
    for path, subdirs, files in os.walk(root):    
        for file in files:        
            if file.endswith(".xlsx"):
                workbook = xlrd.open_workbook(path + "/" + file)
                version = Version(file[0:12])
                version_id = data_base.insert_common('versions', version._name)
                for i in range(0, workbook.nsheets - 1):
                    sheet = workbook.sheet_by_index(i)	
                    subsystem = Subsystem(sheet.name)
                    subsystem_id = data_base.insert_common('subsystems', subsystem._name)
                    version._subsystems.append(subsystem)
                    for row in range(0, sheet.nrows):
                        test_case = Test_case(sheet.cell(row, 0).value)
                        test_case_id = data_base.insert_common('test_cases', test_case._name)
                        subsystem._test_cases.append(test_case)
                        data_base.insert_test_case_subsystem_version(test_case_id, subsystem_id, version_id, 1)
    data_base.connect.close()

if __name__ == "__main__":
    main()        
