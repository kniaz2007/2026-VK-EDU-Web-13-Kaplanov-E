from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from questions.models import Question, Tag, Answer, QuestionLike, AnswerLike
from faker import Faker
from random import *
User = get_user_model() 
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("ratio", nargs="?", type=int, default=100)
    def handle(self, *args, **options):
        ratio = options['ratio']
        user_to_create=[]
        question_to_create = []
        tag_to_create = []
        answer_to_create = []
        questionlike_to_create = []
        answerlike_to_create = []
        batch_size = 50000
        fake = Faker('ru_RU')
        for i in range(ratio):
            user = User(
                username=f"{fake.user_name()}_{randint(1,100000)}",
                email=fake.email(),
                password = "qwerty123"
            )
            user_to_create.append(user)
            if ((i!=0) and (i % batch_size == 0)):
                User.objects.bulk_create(user_to_create, batch_size=1000)
                user_to_create.clear()
        if len(user_to_create) != 0:
            User.objects.bulk_create(user_to_create, batch_size=1000)

        user = list(User.objects.all())

        for i in range(ratio*10):
            question = Question(
                title=f"{fake.word()} {fake.word()} ?",
                author=user[randint(0, len(user)-1)],
                text = fake.text(max_nb_chars=1000)
            )
            question_to_create.append(question)
            if ((i!=0) and (i % batch_size == 0)):
                Question.objects.bulk_create(question_to_create, batch_size=1000)
                question_to_create.clear()
        if len(question_to_create) != 0:
            Question.objects.bulk_create(question_to_create, batch_size=1000)

        for i in range(ratio):
            tag = Tag(
                name=f"{fake.word()}"
            )
            tag_to_create.append(tag)
            if ((i!=0) and (i % batch_size == 0)):
                Tag.objects.bulk_create(tag_to_create, batch_size=1000)
                tag_to_create.clear()
        if len(tag_to_create) != 0:
            Tag.objects.bulk_create(tag_to_create, batch_size=1000)

        all_tags = list(Tag.objects.all())
        all_question = list(Question.objects.all())
        for t in all_tags:
            random_question = sample(all_question, randint(1, 3))
            t.questions.add(*random_question) 

        for i in range(ratio*100):
            answer = Answer(
                title=f"{fake.word()} {fake.word()} ",
                author=user[randint(0, len(user)-1)],
                text = fake.text(max_nb_chars=1000),
                question=all_question[randint(0, len(all_question)-1)]
            )
            answer_to_create.append(answer)
            if ((i!=0) and (i % batch_size == 0)):
                Answer.objects.bulk_create(answer_to_create, batch_size=1000)
                answer_to_create.clear()
        if len(answer_to_create) != 0:
            Answer.objects.bulk_create(answer_to_create, batch_size=1000)

        for i in range(ratio*100):
            questionlike = QuestionLike(
                user=user[randint(0, len(user)-1)],
                question=all_question[randint(0, len(all_question)-1)]
            )
            questionlike_to_create.append(questionlike)
            if ((i!=0) and (i % batch_size == 0)):
                QuestionLike.objects.bulk_create(questionlike_to_create, batch_size=1000,ignore_conflicts=True)
                questionlike_to_create.clear()
        if len(questionlike_to_create) != 0:
            QuestionLike.objects.bulk_create(questionlike_to_create, batch_size=1000,ignore_conflicts=True)

        all_answer = list(Answer.objects.all())
        for i in range(ratio*100):
            answerlike = AnswerLike(
                user=user[randint(0, len(user)-1)],
                answer=all_answer[randint(0, len(all_answer)-1)]
            )
            answerlike_to_create.append(answerlike)
            if ((i!=0) and (i % batch_size == 0)):
                AnswerLike.objects.bulk_create(answerlike_to_create, batch_size=1000,ignore_conflicts=True)
                answerlike_to_create.clear()
        if len(answerlike_to_create) != 0:
            AnswerLike.objects.bulk_create(answerlike_to_create, batch_size=1000,ignore_conflicts=True)

