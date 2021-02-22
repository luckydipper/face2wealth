from flask import Flask, render_template
#import codecs
application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
    #print(render_template("index.html"))
    return render_template("index.html")


#dynamic URL setting
# @application.route('/user/<user_name>/<int:user_id>')
# def user(user_name, user_id):
#     return f'Hello, {user_name}({user_id})!'

#in template(html), use python 
#{%if for%} or {{var}}

if __name__ == "__main__":
    port= int(9000)
    application.run(host="0.0.0.0", port=port, debug = True) #'local 0.0.0.0'