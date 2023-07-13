from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    re_enter_password = request.form.get('re_enter_password')
    birth_date = request.form.get('birth_date')

    # SQLite3 bog'lamini yaratish
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Ma'lumotlarni bazaga yozish
    cursor.execute("INSERT INTO users (username, email, password, birth_date) VALUES (?, ?, ?, ?)",
                   (username, email, password, birth_date))
    
    # O'zgarishlarni saqlash
    connection.commit()
    
    # Bog'lam ruyxatlarini yopish
    connection.close()
    
    return 'Ro\'yxatdan o\'tganingiz uchun rahmat!'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # SQLite3 bog'lamini yaratish
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Foydalanuvchini bazada qidirish
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    
    # Bog'lam ruyxatlarini yopish
    connection.close()
    
    if result:
        return 'Kirishingiz uchun rahmat!'
    else:
        return 'Kirishdagi ma\'lumotlar xato!'

if __name__ == '__main__':
    app.run(debug=True)
