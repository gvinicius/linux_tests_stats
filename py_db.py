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
        self.connect.execute('CREATE TABLE `subsystems`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `description` VARCHAR(15) NOT NULL ) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def create_versions(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `versions`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `description` VARCHAR(15) NOT NULL ) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def create_test_case(self):
        self.use_db()
        self.connect.execute('CREATE TABLE `test_cases`(`id` INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, `subsystem_id` INTEGER(11) NOT NULL, `version_id` INTEGER(11) NOT NULL, `description` VARCHAR(15) NOT NULL, CONSTRAINT `fk_1` FOREIGN KEY (`subsystem_id`) REFERENCES subsystems (`id`),  CONSTRAINT `fk_2` FOREIGN KEY (`version_id`) REFERENCES versions (`id`)) ENGINE=InnoDB COLLATE=utf8_unicode_ci;')
    def select_id_reverse(self, table_name):
        self.use_db()
        return self.connect.execute('SELECT `id`, `description` FROM {0};'.format(table_name))
    def insert_common(self, table_name, description):
        self.use_db()
        self.connect.execute('INSERT INTO {0} VALUES (`{1}`);'.format(table_name, description))
    def insert_common(self, description, subsystem_id, version_id):
        self.use_db()
        self.connect.execute('INSERT INTO `test_cases` VALUES (`{0}`, `{1}`,`{2}`);'.format(description, subsystem_id, version_id))
