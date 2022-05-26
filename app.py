# Flasuからflaskをインポート
import glob
import time
import random
from flask import Flask, render_template
# app
app = Flask(__name__)

# helloworld app葉ルーティング,関数
@app.route("/") 
def helloworld(): 
    return "HelloWorld"
# ひきすう
@app.route("/<name>")
def greet(name):
    return name +"さん、こんにちは！"

@app.route("/template")
def template():
    return render_template("index.html")

# テンプレートと変数
@app.route("/temp")
def temp():
    py_name = "わお"
    return render_template("index.html", name = py_name)

@app.route("/weather")
def weather():
    py_weather = "はれ"
    return render_template("weather.html", weather=py_weather)



# __name__というのは自動的に定義される変数で、現在のファイル名（モジュール）が入る
if __name__ == "__main__":
    # flaskがもっているアプリを実行します
    app.run(debug=True)