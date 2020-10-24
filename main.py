from flask import Flask, render_template, request, url_for, redirect
import mmh3
import requests
import sys
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def method_name():
    if request.method=='POST':
       response = requests.get(request.form["url"])
       favicon = response.content.encode('base64')
       hash = mmh3.hash(favicon)
       shodan_url="https://www.shodan.io/search?query=http.favicon.hash:"+str(hash)
       return render_template("index.html", hash=str(hash),shodan_url=shodan_url,display="")
    return render_template("index.html",hash="",shodan_url=" ",display="none")

if __name__ == '__main__':
    app.run()
