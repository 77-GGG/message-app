from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# 数据库连接函数
def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn

# 首页，显示留言板
@app.route('/')
def index():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages').fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

# 添加留言
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        content = request.form['content']
        if content:
            conn = get_db_connection()
            conn.execute('INSERT INTO messages (content) VALUES (?)', (content,))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
