from flask import Flask, session, render_template, redirect, request, url_for, Blueprint
import pymysql
 
maria_host = 'localhost'   
maria_port=3306
maria_user = 'root'
maria_password = '23691341' #비번 바꿔줘야 함
maria_db = 'WHS'

listdb = Blueprint("listdb", __name__)

@listdb.route("/list", methods=['GET', 'POST'])
def list_result():
    db = pymysql.connect(host=maria_host, port=maria_port, user=maria_user, password=maria_password, db=maria_db, charset='utf8')
    cursor = db.cursor()

    if request.method == 'POST':
        error = None

        sql = "SELECT * FROM board"
        value = (sql)
        cursor.execute(sql)
        data_list = cursor.fetchall()
        db.commit()

        print(data_list[0])

    else:  # GET request
        sql = "SELECT * FROM board"
        cursor.execute(sql)
        data_list = cursor.fetchall()

    db.close()

    return render_template("list.html", data_list=data_list)