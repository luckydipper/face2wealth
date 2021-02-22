from flask import Blueprint, render_template, url_for
# from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return "hello world"

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# urlfor로 question으로 블루프린트 등록된 이름을 찾음. _list로 된 함수명, 
# question_view도 bp의 일환이니, 여기서 question이란 bq이름 찾아서 redirect

# @bp.route('/')
# def index():#sql asc ascending, desc descending
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)
# @bp.route('/detail/<int:question_id>/')#매핑 규칙
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)#get(question_id)
#     return render_template('question/question_detail.html', question=question)