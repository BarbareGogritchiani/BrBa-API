import json
import requests
import sqlite3

name = input("enter the characters name: ")
url = f'https://www.breakingbadapi.com/api/characters?name={name}'
r = requests.get(url)
print(r)

if r.status_code == 200:
    print("Connection Status was OK")
else:
    print("There Was An Error")

r2  = json.loads(r.text)
result = json.dumps(r2, indent=4)


with open('walter.json', 'w') as file:
    file.write(result)

print(r.content)
print(r.headers)

conn = sqlite3.connect("breaking_bad.sqlite")
cursor = conn.cursor()

#ცხრილის შექმნა , რომელშიც იქნებიან პერსონაჟები , ასევე მოიძებნება მათი დაბადების თარიღი
#მსახიობი , ვინც განასახიერებს მას და ნიქნეიმი

cursor.execute('''CREATE TABLE IF NOT EXISTS characters 
                    (char_id INTEGER ,
                    name VARCHAR(50),
                    birthday VARCHAR(50),
                    portrayed VARCHAR(50),
                    nickname VARCHAR(50));''')

cursor.execute('INSERT INTO characters (char_id, name, birthday, portrayed, nickname)'
               ' VALUES(?,?,?,?,?)',
               (r2[0]['char_id'],r2[0]['name'],r2[0]['birthday'],r2[0]['portrayed'],r2[0]['nickname'])
               )
conn.commit()

conn.close()