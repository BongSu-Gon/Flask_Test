from passlib.hash import sha256_crypt
from flask import Flask , render_template , request, redirect
from data import Articles
import pymysql 

#reder_template html과 만나면 해당 템플릿으로 변환시켜 줌.

app = Flask(__name__)

app.debug = True

db = pymysql.connect( #접속환경 설정; 키값 설정 후, 새로운 인스턴스(db) 생성
    host='localhost',
    port = 3306,
    user = 'root',
    password = '1234',
    db = 'busan'
)



  #get과 post차이점
  #get 검색 창, 일련의 형태, post방식은 get과 달리 검색 창에 안뜸


@app.route('/', methods = ['GET']) #데커레이터  경로 라우팅, 방식(지금은 리스트)
def hello_world():
    # return "hello world"
    return render_template("index.html",data = "kim")
    # 첫번째 인자 html경로, 두번째는 전달할 데이터
@app.route('/index')
def index():
    return render_template("index.html", hello ="bongsu")
@app.route('/about')
def about():
    return render_template("about.html", hello ="bongsu")

# @app.route('/articles')
# def articles():
#     sql = 'SELECT * FROM topic;'
#     cursor.execute(sql)
#     topics = cursor.fetchall()
#     print(topics)
#     articles = Articles()
#     print(articles[0]['title'])
#     return render_template("articles.html", articles = articles)
@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles()
    # print(topics[0])
    return render_template("articles.html", articles = topics)


@app.route('/article/<int:id>')
#플라스크 파이썬에서 <>안에 매개 변수명으로 사용.
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id ={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods = ["GET","POST"])
def add_articles():
    cursor = db.cursor()
    if request.method =="POST":
        author = request.form['author']
        title = request.form['title']
        description = request.form['description']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, description, author]
        print(description)

        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        return redirect("/articles")
        # return "<h1>글쓰기</h1>"
    else :
        return render_template("add_articles.html")

@app.route('/delete/<int:par_id>', methods = ['POST'])
def delete(par_id):
    cursor = db.cursor()
    # sql = 'DELETE FROM topic WHERE id = %s;'
    # id = [par_id]
    # cursor.execute(sql, id)

    sql = 'DELETE FROM topic WHERE id = {};'.format(par_id)
    cursor.execute(sql)
    db.commit()

    return redirect("/articles")


@app.route('/<int:par_id2>/edit/', methods = ["GET","POST"])

def edit(par_id2):
    cursor = db.cursor()
    if  request.method =="POST":
        # request.form['title','description','author']
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        print(author)
        sql = 'UPDATE topic SET title = %s, body = %s ,author = %s WHERE id = {};'.format(par_id2)
        
        input_data = [title, desc, author]
        cursor.execute(sql, input_data)
        db.commit()
        print(request.form['title'])
        return redirect("/articles")
        
    else :
        sql = "SELECT * FROM topic WHERE id = {};".format(par_id2)
        cursor.execute(sql)
        topic = cursor.fetchone()
        # print(topic[1])
        return render_template("edit_articles.html", article = topic)

@app.route('/register' , methods = ['GET', 'POST'])
def register():
  cursor = db.cursor()
  if request.method == "POST":
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    userpw = sha256_crypt.encrypt(request.form['userpw'])#암호화 
    sql = "INSERT INTO users (name, email , username, password) VALUES (%s,%s,%s,%s)"
    input_data = [name ,email , username ,userpw  ]
    cursor.execute(sql ,input_data)
    db.commit()
    return redirect('/articles')

  else:

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
  cursor = db.cursor()
  if request.method == "POST":
    username = request.form['username']
    userpw_1 = request.form['userpw']
    sql = 'SELECT password FROM users WHERE email = %s;'
    input_data = [usersname]
    cursor.execute(sql, input_data)
    userpw = cursor.fetchone()
    print(userpw[0])
    if sha256_crypt.verify(userpw_1, userpw[0]):
      return "SUCCESS"
    else:
      return userpw[0]
     
if __name__ == '__main__': ## 처음 서버 띄우는 곳, 초기 실행
    app.run()

    