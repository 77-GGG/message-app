import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('messages.db')
cursor = conn.cursor()

# 创建messages表
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# 提交事务
conn.commit()

# 关闭连接
conn.close()
