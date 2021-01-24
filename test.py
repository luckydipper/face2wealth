from flask import Flask
import codecs
application = Flask(__name__)

# with open("index.html",'r') as html:
#     data = codecs.open(html)
#     print(data.read)


f=codecs.open("index.html", 'r')
html = f.read()


@application.route("/")
def hello():
    return html

if __name__ == "__main__":
    application.run(host='0.0.0.0')