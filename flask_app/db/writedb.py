from flask import Flask, session, render_template, redirect, request, url_for, Blueprint
import pymysql
from datetime import datetime
 
maria_host = 'localhost'
maria_port=3306
maria_user = 'root'
maria_password = '23691341' #비번 바꿔줘야 함
maria_db = 'WHS'

writedb = Blueprint("writedb", __name__)

@writedb.route("/write", methods=['GET','POST'])
def write():
    if request.method == 'POST':
        print(1111111)
        error = None

        db = pymysql.connect(host=maria_host, port=maria_port, user=maria_user, password=maria_password, db=maria_db, charset='utf8')

        title = request.form['title']
        author = request.form['author']
        pw = request.form['pw']
        contents = request.form['contents']

        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM board")
        num = cursor.fetchall()
        num = num[0]
        num = int(num[0])
        db.commit()
        cursor = db.cursor()

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO board VALUES(%s, %s,%s,%s,%s,%s,%s )"
        value = (str(num+1),title,author,date,'0', contents, pw)

        cursor.execute(sql, value)

        data = cursor.fetchone()
        db.commit()
        db.close()
        
        file = request.files['file']
        file.save(file.filename)

        return redirect(url_for('list'))
    
    
    return render_template("write.html")