import sqlite3

conn = sqlite3.connect("phonebook.sqlite3")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS persons")
cursor.execute("DROP TABLE IF EXISTS phone_records")
cursor.execute("DROP TABLE IF EXISTS phone_types")

cursor.execute("CREATE TABLE IF NOT EXISTS persons ( " +
               "   person_id  INT NOT NULL, " +
               "   first_name TEXT NOT NULL, " +
               "   last_name  TEXT NOT NULL, " +
               "   PRIMARY KEY (person_id) )")

cursor.execute("CREATE TABLE IF NOT EXISTS phone_types ( " +
               "    type_id INT NOT NULL, " +
               "    type_name TEXT NOT NULL, "+
               "    PRIMARY KEY (type_id) )")

cursor.execute("CREATE TABLE IF NOT EXISTS phone_records ( " +
               "    person_id INT NOT NULL, " +
               "    type_id INT NOT NULL, " +
               "    phone_number TEXT NOT NULL, " +
               "    PRIMARY KEY (person_id, type_id), " +
               "    FOREIGN KEY (person_id) REFERENCES persons (person_id), " +
               "    FOREIGN KEY (type_id) REFERENCES phone_types (type_id) )")

cursor.execute("CREATE INDEX IF NOT EXISTS fk_phre_pers_idx ON phone_records (person_id)")
cursor.execute("CREATE INDEX IF NOT EXISTS fk_phre_type_idx ON phone_records (type_id)")

conn.close()