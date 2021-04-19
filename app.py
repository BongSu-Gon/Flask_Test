from flask import Flask , render_template 
from data import Articles
#reder_template html과 만나면 해당 템플릿으로 변환시켜 줌.

app = Flask(__name__)

app.debug = True

@app.route('/data', methods = ['GET']) #데커레이터  경로 라우팅, 방식(지금은 리스트)
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

@app.route('/articles')
def articles():
    articles = Articles()
    print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

if __name__ == '__main__': ## 처음 서버 띄우는 곳, 초기 실행
    app.run()