""" This contains the custom methods to treat the db.  """
import MySQLdb
import sqlalchemy as sqa

class DataBase:
    def __init__(self):
        self.engine = sqa.create_engine("mysql://root:ldd01@localhost/", echo=True)
        self.connect = self.engine.connect()
    def create_schema(self):
        self.connect.execute("CREATE SCHEMA `linux_tests`;")
    def use_db(self):
        self.connect.execute("USE `linux_tests`;")
    def create_subsystems(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `subsystems`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `description` VARCHAR(15) NOT NULL UNIQUE ) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def create_versions(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `versions`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `description` VARCHAR(15) NOT NULL UNIQUE) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def create_test_cases(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `test_cases`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `description` VARCHAR(15) NOT NULL UNIQUE) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def create_test_case_subsystem_versions(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `test_case_subsystem_versions`(`subsystem_id` INTEGER(11) NOT NULL, `version_id` INTEGER(11) NOT NULL, `test_case_id` INTEGER(11) NOT NULL, `lines_of_code` INTEGER(4) NOT NULL, PRIMARY KEY (`subsystem_id`, `version_id`, `test_case_id`), CONSTRAINT `fk_1` FOREIGN KEY (`subsystem_id`) REFERENCES subsystems (`id`),  CONSTRAINT `fk_2` FOREIGN KEY (`version_id`) REFERENCES versions (`id`),  CONSTRAINT `fk_3` FOREIGN KEY (`test_case_id`) REFERENCES test_cases (`id`)) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def insert_common(self, table_name, description):
        id = 0
        self.use_db()
        result =  self.connect.execute('select COALESCE((SELECT `id` FROM {0} WHERE `description` LIKE "{1}"),0) AS `id` ;'.format(table_name, description))
        if result.fetchone()['id'] == 0:
            self.connect.execute('INSERT INTO {0} (`description`) VALUES ("{1}");'.format(table_name, description))
            result = self.connect.execute('select LAST_INSERT_ID() AS `id`;')
        #for row in result:
        #    id = row['id']
        return result.fetchone()['id']
    def insert_test_case_subsystem_version(self, test_case_id, subsystem_id, version_id, loc):
        self.use_db()
        self.connect.execute('INSERT INTO `test_case_subsystem_versions` (`test_case_id`, `subsystem_id`, `version_id`, `lines_of_code`) VALUES ("{0}", "{1}", "{2}", "{3}");'.format(test_case_id, subsystem_id, version_id, loc))
    def drop(self):
        self.connect.execute("DROP DATABASE `linux_tests`;")

