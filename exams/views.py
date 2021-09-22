from django.shortcuts import render
from .models import Exam
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result

# Create your views here.
class ExamListView(ListView):
    model = Exam 
    template_name = 'exams/main.html'

def exam_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exams/exam.html', {'obj': exam})

def exam_data_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    questions = []
    # fetch all question of an exam
    for q in exam.get_questions():
        answers = []
        # fetch all answer options of a particular question
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'duration': exam.duration,
    })

def save_exam_view(request, pk):
    if request.method == 'POST':
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        exam = Exam.objects.get(pk=pk)

        mark = 0
        multiplier = 100 / exam.total_assigned_marks
        ratio = exam.total_assigned_marks / exam.total_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            mark += ratio
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        percentage = mark * multiplier

        if mark >= exam.pass_mark:
            Result.objects.create(exam=exam, user=user, mark=mark, percentage=percentage, result_status='Pass')
            return JsonResponse({'passed': True, 'percentage': percentage, 'results': results})
        else:
            Result.objects.create(exam=exam, user=user, mark=mark, percentage=percentage, result_status='Fail')
            return JsonResponse({'passed': False, 'percentage': percentage, 'results': results})