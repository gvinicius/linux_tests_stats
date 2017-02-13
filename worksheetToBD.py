import os
import xlrd
import py_bd


root = "/Users/jonatasfbastos/Dropbox/DOUTORADO_UFBA/Computacao/Evolution/Test Evolution/LTP Study/LTP Versions/TestScript/"

class Version:

	def __init__(self, name):
		self._name = name
		self._sub_systems = []

class SubSystem:

	def __init__(self, name):
		self._name = name
		self._test_cases = []	
	
	def	__str__(self):
		cabecalho = "----------------------------------"
		testcases = ""

		for i in range(0, len(self._test_cases)):
			testcases += str(self._test_cases[i]._name) + "\n"

		return 	str(cabecalho + "\n" + self._name + "\n" + cabecalho + "\n" + testcases)


class TestCase:

	def __init__(self, name):
		self._name = name

	def __str__(self):	
		return str(self._name)


def main():
	for path, subdirs, files in os.walk(root):    
	    for file in files:        
	        if file.endswith(".xlsx"):
	            workbook = xlrd.open_workbook(path + "/" + file)            
	            version = Version(file[0:12])            
                    # insert version
	            for i in range(0, workbook.nsheets - 1):
	            	sheet = workbook.sheet_by_index(i) 				
	            	subsystem = SubSystem(sheet.name)

                        # insert subsystem?
	            	version._sub_systems.append(subsystem)            	
	            	for row in range(0, sheet.nrows):
	            		test = TestCase(sheet.cell(row, 0).value)
	            		subsystem._test_cases.append(test)

                                # subsystems = py_db.DataBase.select_id_reverse(self, 'subsystems')?
                                # versions = py_db.DataBase.select_id_reverse(self, 'versions')?
	           		#print (subsystem)
	            #print ("################################")
	            #print (version._name)	         

if __name__ == "__main__":
	main()
            
