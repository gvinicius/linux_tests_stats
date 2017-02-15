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
    db = py_db.DataBase()
    for path, subdirs, files in os.walk(root):    
        for file in files:        
            if file.endswith(".xlsx"):
                workbook = xlrd.open_workbook(path + "/" + file)
                version = Version(file[0:12])
                version_id = db.insert_common('versions', version._name)
                for i in range(0, workbook.nsheets - 1):
                    sheet = workbook.sheet_by_index(i)	
                    subsystem = Subsystem(sheet.name)
                    subsystem_id = db.insert_common('subsystems', subsystem._name)
                    version._subsystems.append(subsystem)
                    for row in range(0, sheet.nrows):
                        tc = Test_case(sheet.cell(row, 0).value)
                        subsystem._test_cases.append(tc)
                        # db.insert_test_case(description, subsystem_id, version_id, loc)
                        db.insert_test_case(tc._name, subsystem_id, version_id, 1)
                        #print (subsystem)
                #print ("################################")
                #print (version._name)	         
    db.connection.close()

if __name__ == "__main__":
	main()
            
