import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
balance INTEGER NOT NULL
)
''')
#cursor.execute('''ALTER TABLE Users ADD COLUMN balance INTEGER NOT NULL DEFAULT 0;''')

#cursor.execute("CREATE INDEX IF NOT EXISTS idx_email  ON Users (email)")


#for i in range(10):
    #cursor.execute("INSERT INTO Users(username,email,age,balance)VALUES(?,?,?,?)",(f"User{i+1}",f"{i+1}example@gmail.com",f"age{(i+1)*10}",f" 1000"))

#cursor.execute("UPDATE Users SET balance = ? WHERE id%2 <> ?",(500,0))
#cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?",(0,))


#cursor.execute("SELECT username, email,age,balance FROM Users WHERE age <> ?",(60,))

#users=cursor.fetchall()
#for user in users:
    #print(f"Имя:{user[0]}/ Почта:{user[1]}/Возраст:{user[2]}/Баланс{user[3]}")

#cursor.execute("DELETE FROM Users WHERE id =?" ,(6,))


cursor.execute("SELECT Sum (balance) FROM Users")
all_balance=cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total_users=cursor.fetchone()[0]
#print(total_users)
#print(all_balance)
print(all_balance/total_users)

connection.commit()
connection.close()