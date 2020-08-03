from django.db import models

# Create your models here.
class Question(models.Model):
    # id = models.IntegerField()
    # 자동으로 생성되는 id는 PK, 1씩 자동증가(autoincrement)
    question_text = models.CharField('투표질문 제목', max_length=200)
    pub_date = models.DateTimeField('투표 날짜')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # PK가 id이기 때문에 FK 뒤에 자동으로 _id가 붙음
    choice_text = models.CharField('투표 선택지', max_length=30)
    votes = models.IntegerField('투표수', default=0)

    def __str__(self):
        return self.choice_text