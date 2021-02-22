#Flask_WTF

#SECRET_KEY는 CSRF(cross-site request forgery)라는 웹 사이트 취약점 공격을 방지하는
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
#글자 수에 제한이 있는 ‘제목’은 StringField를 사용하고, 글자 수에 제한이 없는 ‘내용’은 TextAreaField를 사용했다
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
#datarequired가 실패시 나오는 문장 

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])