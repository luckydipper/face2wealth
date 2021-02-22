#__init__.py는 패키지를 만드는데 사용됨. 패키지를 import하면 자동으로 실행
from flask import Flask ,render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os
import config #config가 인식이 안 되네 ^^.

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']= 'development' #Flask-WTF으로 form을 만드는데 CSRF 보안.
    BASE_DIR = os.path.dirname(__file__)
    SQLAlCHEMY_TRACK_MODIFICATIONS = False
    SQLAlCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLAlCHEMY_DATABASE_URI
    from . import models
    

    #ORM
    db.init_app(app)
    
    
    migrate.init_app(app, db)

    
    #import models, #현재 패키지에서 가져와야하므로?
    #.을 찍어야함.
    #blue print
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    return app

# @app.route('/', methods=['GET'])
# def index():
#     return "hello world"
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=9000,debug=True)
