import mysql.connector
#zad 3.1
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="haslo123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE  `hasla` (\
    `id` int(10) NOT NULL auto_increment,\
    `tresc` varchar(255),\
    `kategoria` varchar(255),\
    PRIMARY KEY( `id` ),\
    UNIQUE(tresc)\
);")

mycursor.execute.execute("CREATE TABLE `zawodnicy` (\
    `id` INT NOT NULL AUTO_INCREMENT,\
    `imie` VARCHAR NOT NULL,\
    `nazwisko` VARCHAR NOT NULL,\
    `numer` INT,\
    PRIMARY KEY (`id`)\
);")

#zad 3.2

sql = "INSERT INTO hasla (tesc, kategoria) VALUES (%s, %s)"

val = {
    ("kucharz", "zawody"),
    ("Rekin", "zwierzeta")
}

mycursor.executemany(sql, val)

mydb.commit()