from flask import Flask, session, render_template, redirect, request, url_for, Blueprint
import pymysql
 
maria_host = 'localhost'
maria_port=3306
maria_user = 'root'
maria_password = '23691341' #비번 바꿔줘야 함
maria_db = 'WHS'

logindb = Blueprint("logindb", __name__)

@logindb.route("/login", methods=['GET', 'POST'])
def login_result():
    if request.method == 'POST':
        error = None

        db = pymysql.connect(host=maria_host, port=maria_port, user=maria_user, password=maria_password, db=maria_db, charset='utf8')

        id = request.form['id']
        pw = request.form['pw']

        cursor = db.cursor()

        sql = "SELECT id FROM login WHERE id = %s AND pw = %s"
        value = (id, pw)

        cursor.execute(sql, value)

        data = cursor.fetchone()
        db.commit()
        db.close()

        return redirect(url_for('list'))
    """
        if data:
            session['login_user'] = data[0]
            
        else:
            error = 'invalid input data detected !'
            return render_template("error.html", error=error)
        """
    return render_template("login.html")