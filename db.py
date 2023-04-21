import pymysql

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host='127.0.0.1',user='rey',password='rey',database='flask_react_mysql',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as e:
        print(e)
    return conn
