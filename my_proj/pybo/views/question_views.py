from flask import Blueprint, render_template, request, url_for
from datetime import datetime
from werkzeug.utils import redirect

from pybo.models import Question
from ..form import QuestionForm, AnswerForm

from .. import db


bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)
    # return render_template('question/question_detail.html', question=question) 


#GET 방식 요청이므로 그대로 질문 등록 화면을 보여 주고,
#<저장하기>는 POST 방식 요청이므로 데이터베이스에 질문 1건을 저장한 다음 질문 목록 화면으로 이동한다.
@bp.route('/create/',methods=['POST','GET'])
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form= form)
