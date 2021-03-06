import random

from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
import pandas
from subscription.decorators import payment_required
from django.utils.decorators import method_decorator
from users.models import User
from exam.forms import ExamImportForm

from question.models import Answer
from .models import Exam
from elearning.models import ELearningUserSession, ELearning, ELearningSession

from question.models import Question, ExamUserSession, ExamUserAnswer
from presentations.models import Presentation
from question.serializers import ExamUserSessionSerializer
from django.contrib.auth.mixins import AccessMixin
import os
from config.common import *
from django.contrib.auth import authenticate

def about(request):
    return render(request, 'about.html')


def solutions(request):
    return render(request, 'solutions.html')


def contact(request):
    return render(request, 'contact.html')

def mission(request):
    return render(request, 'mission.html')

def references(request):
    return render(request, 'references.html')

def instructions(request):
    return render(request, 'instructions.html')

def careers(request):
    return render(request, 'careers.html')

def sitemapob(request):
    return render(request, 'sitemap.xml')


class OurBaseView(TemplateView):
    template_name = "exam/Solvency-2-e-learning.html"

def user_progress_result(users):
    """
    This method return the users progress list
    """

    elearning = list(ELearning.objects.all().values_list('name', flat=True))
    user_progress_report = {}
    user_progress_completed = {}

    for user in users:

        user_el = ELearningUserSession.objects.filter(user=user)
        elearning_progress = list(ELearning.objects.all().values_list('name', flat=True))
        elearning_progress_completed = list(ELearning.objects.all().values_list('name', flat=True))

        for el in user_el:
            elearning_name = el.elearning.name
            el_progress_value = el.user_progress

            if elearning_name in elearning_progress:
                index = elearning_progress.index(elearning_name)
                elearning_progress[index] = el_progress_value

            # elearning completed sessions
            if elearning_name in elearning_progress_completed:
                el_completed_session_number = el.active_session_number - 1
                total_el_session_number = ELearningSession.objects.filter(elearning__name=elearning_name).count()
                completed_progress = (el_completed_session_number / total_el_session_number) * 100
                elearning_progress_completed[index] = round(completed_progress)
        #     ~~~~~~~~~~~~~~~~~


        for el in elearning:
            if el in elearning_progress:
                index_el = elearning_progress.index(el)
                elearning_progress[index_el] = '-'

            # el completed session
            if el in elearning_progress_completed:
                index_el = elearning_progress_completed.index(el)
                elearning_progress_completed[index_el] = '-'
            #     ~~~~~~~~~~~~~~~~~~~~~~

        user_progress_report[user.email] = elearning_progress
        user_progress_completed[user.email] = elearning_progress_completed

    return user_progress_report,user_progress_completed


def random_color(number_of_colors):

    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return color


def team_progress_result(manager):
    """
    This method return the team progress list
    """

    elearning = list(ELearning.objects.all().values_list('name', flat=True))

    user_list = list(User.objects.filter(manager=manager).values_list('email', flat=True))
    all_user_progress_list = []
    color = random_color(len(elearning))
    el_count = 0
    all_user_progress_completed_list = []

    for el in elearning:
        el_value_list = list(User.objects.filter(manager=manager).values_list('email', flat=True))
        el_value_completed_list = list(User.objects.filter(manager=manager).values_list('email', flat=True))

        for user in user_list:
            user_el = ELearningUserSession.objects.filter(user__email=user,elearning__name=el)


            if user in el_value_list:
                    index = el_value_list.index(user)

                    if len(user_el) == 0:
                        el_value_list[index] = 0
                    else:
                        el_value_list[index] = user_el[0].user_progress

            if user in el_value_completed_list:
                    index = el_value_completed_list.index(user)
                    # elearning completed sessions
                    if len(user_el) == 0:
                        el_value_completed_list[index] = 0
                    else:
                        el_completed_session_number = user_el[0].active_session_number - 1
                        total_el_session_number = ELearningSession.objects.filter(
                            elearning__name=el).count()
                        completed_progress = (el_completed_session_number / total_el_session_number) * 100
                        el_value_completed_list[index] = round(completed_progress)
                    #     ~~~~~~~~~~~~~~~~~


        all_user_progress_list.append({"label":el,
                "backgroundColor": color[el_count],
                "borderColor": color[el_count],
                "data": el_value_list})

        all_user_progress_completed_list.append({"label":el,
                "backgroundColor": color[el_count],
                "borderColor": color[el_count],
                "data": el_value_completed_list})

        el_count = el_count + 1

    return all_user_progress_list,user_list,all_user_progress_completed_list




class UserProgressView(TemplateView):
    template_name = "user-progress.html"

    def get_context_data(self, **kwargs):

        context = super(UserProgressView, self).get_context_data()
        elearning = list(ELearning.objects.all().values_list('name', flat=True))
        user_progress_report,user_progress_completed = user_progress_result(users=User.objects.all())
        context['elearnings'] = elearning
        context['user_progress_report'] = user_progress_report

        return context




class ExamView(DetailView):
    model = Exam


class ExamUserSessionViewSet(viewsets.GenericViewSet):
    """ Viewset for managing movie objects with details from omdbapi.com.
        Results are saved in database for limiting external API requests.
    """
    queryset = ExamUserSession.objects.all()
    serializer_class = ExamUserSessionSerializer
    pk_url_kwarg = 'exam.pk'

    def get_object(self):
        return self.get_queryset().filter(exam__pk=self.kwargs['pk'], finished=None).first()

    def get_queryset(self):
        qs = super(ExamUserSessionViewSet, self).get_queryset()
        qs.filter(user=self.request.user, exam__exam_type=Exam.EXAM)
        return qs

    def retrieve(self, request, pk=None):
        """ GET: Get active exam user session """
        exam = get_object_or_404(Exam, pk=pk, exam_type=Exam.EXAM)
        eus = ExamUserSession.objects.filter(exam_id=pk, finished=None)
        exam_obj = Exam.objects.get(id=pk)

        if not eus.exists():
            response = {
                'state': 'init',
                'content': render_to_string('exam/includes/_exam_start.html', {'object': exam})
            }
            return Response(response)

        eus = eus.first()
        if not eus.finished and eus.no_time_left:
            eus.stop_test()
            response = {
                'state': 'no_time_left',
                'session': self.serializer_class(eus).data,
                'content': render_to_string('exam/includes/_exam_time_passed.html')
            }

        else:
            # Assign new question if not already assigned. Exclude already answered.
            if not eus.active_question:

                already_answered = list(ExamUserAnswer.objects.filter(session=eus) \
                                        .values_list('question', flat=True))

                questions = Question.objects.filter(exam=eus.exam).exclude(pk__in=already_answered)

                # If no questions left or questions limit reached - end exam
                if not questions or len(already_answered) >= eus.n_questions:
                    eus.stop_test()
                    response = {
                        'state': 'end',
                        'session': self.serializer_class(eus).data,
                        'content': render_to_string('exam/includes/_exam_end.html')
                    }
                    return Response(response)

                # Get random question
                question = random.choice(questions)
                eus.active_question = question
                eus.save()
            else:
                question = eus.active_question

            context = {
                'object': eus,
                'show_answers': exam_obj.show_answers,
                'question': question
            }
            response = {
                'state': 'question',
                'session': self.serializer_class(eus).data,
                'content': render_to_string('exam/includes/_question.html', context)
            }
        return Response(response)

    def partial_update(self, request, pk=None):
        """ PATCH: Start exam """
        exam = get_object_or_404(Exam, pk=pk)
        data = request.data
        nick_name = data.get('nick_name', None)

        eus, crt = ExamUserSession.objects.get_or_create(exam=exam, user=request.user, nick_name=nick_name,
                                                         finished=None)
        if crt:
            eus.start_test()
            response = {
                'state': 'start',
                'session': self.serializer_class(eus).data,
            }
            return Response(response)
        return Response(status=400)

    def update(self, request, pk=None):
        """ PUT: Answer sent by user """

        data = request.data
        eus = self.get_object()
        answer_id = int(data.get('answer', None))
        question_id = int(data.get('question', None))

        eua = ExamUserAnswer.objects.filter(session=eus, question_id=question_id, session__finished=None).first()

        # If already answered, finished or no time left - return error
        if eua or eus.finished or eus.no_time_left:
            return Response(status=400)

        eua = ExamUserAnswer.objects.create(
            session=eus,
            question_id=question_id,
            answer_id=answer_id,
            user_id=request.user.id
        )
        eus.active_question = None
        eus.save()
        if eua.answer.correct:
            response = {
                'correct': 'true',
                'content': render_to_string('exam/includes/_correct.html')
            }
        else:
            response = {
                'correct': 'false',
                'content': render_to_string('exam/includes/_false.html')
            }
        if eua.answer.question.explanation:
            response['explanation'] = eua.answer.question.explanation
        return Response(response)


@method_decorator(login_required, name='dispatch')
@method_decorator(payment_required, name='dispatch')
class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'exam/exam_list.html'

    def get_queryset(self):
        if self.request.user.is_demo:
            qs = super(ExamListView, self).get_queryset().filter(demo=True)
        else:
            qs = super(ExamListView, self).get_queryset()
        return qs

    def get_material_list(self):

        path = os.path.join(STATICFILES_DIRS[0], "materials")  # insert the path to your directory
        files = os.listdir(path)
        return files

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exams'] = self.get_queryset().filter(exam_type=Exam.EXAM)
        context['e_user_sessions'] = list(ELearningUserSession.objects.filter(user=self.request.user) \
                                          .values_list('elearning', flat=True))

        memory_force = ELearningUserSession.objects.filter(user=self.request.user) \
            .values_list('exam__name', 'memory_force')

        context['memory_force'] = dict(memory_force)

        context['material_files'] = self.get_material_list()

        # context['topic'] =  Presentation.objects.values_list('topic', flat=True).distinct()


        if self.request.user.is_demo:
            context['topic_dict'] = dict(Presentation.objects.filter(is_demo=True)\
                                         .values_list('topic', 'elearning').distinct())
            context['presentation_elearnings'] = Presentation.objects.filter(is_demo=True)\
                .values_list('elearning', flat=True).distinct()
        else:
            context['topic_dict'] = dict(Presentation.objects.values_list('topic', 'elearning').distinct())
            context['presentation_elearnings'] = Presentation.objects.values_list('elearning', flat=True).distinct()

        if self.request.user.is_demo:
            context['elearnings'] = ELearning.objects.filter(demo=True, exam_type="elearning")
        else:
            context['elearnings'] = ELearning.objects.filter(exam_type="elearning")
        # context['memory_force'] = ELearningUserSession.objects.filter(user=self.request.user)
        # context['elearnings_ns'] = self.get_queryset().filter(exam_type=Exam.ELEARNING_NS)

        elearning_progress = list(ELearning.objects.all().values_list('name', flat=True))
        user_progress_report,user_progress_completed_report = user_progress_result(users=User.objects.filter(id=self.request.user.id))
        context['elearnings_progress'] = elearning_progress
        context['user_progress_report'] = user_progress_report
        context['user_progress_completed_report'] = user_progress_completed_report
        all_user_dict,user_list,team_completed_list = team_progress_result(self.request.user.email)


        context['all_user_dict'] = all_user_dict
        context['user_label_list'] = user_list
        context['team_completed_list'] = team_completed_list

        return context


class ExamScoreReauthentication(TemplateView):
    template_name = 'exam/score_login.html'


class ExamScoresListView(LoginRequiredMixin, TemplateView):
    model = ExamUserSession
    template_name = 'exam/exam_score_list.html'

    def get(self, *args, **kwargs):
        return redirect("/exam/score-reauthentication/")

    def post(self, *args, **kwargs):

        email = self.request.user.email
        password = self.request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            context = {}
            context['object_list'] = self.model.objects.filter(finished__isnull=False,
                                                               user=self.request.user, exam__exam_type=Exam.EXAM)
            return render(self.request, 'exam/exam_score_list.html', context)
        else:
            return HttpResponse("Sorry,You don't have permissions to access this page.")


class ExamScoreView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        eus = get_object_or_404(ExamUserSession, pk=kwargs['pk'])
        response = render(request, 'exam/includes/_score.html', {
            'session': ExamUserSessionSerializer(eus).data,
            'score': eus.get_score,
            'questions': eus.n_questions,
            'correct': eus.count_correct_answers
        })
        return response


class AdminOrStaffLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is staff or admin"""

    # ---------------------------------------------------------------------------
    # dispatch
    # ---------------------------------------------------------------------------
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class ExamImportView(AdminOrStaffLoginRequiredMixin, FormView):
    """
    This class handle the import data of exam
    """

    form_class = ExamImportForm
    template_name = "exam/exam_import_form.html"

    def get_success_url(self):
        success_url = reverse_lazy('admin:exam_exam_changelist')
        return success_url

    def form_valid(self, form):
        csv_file = form.cleaned_data.get("csv_file")
        df = pandas.read_excel(csv_file)
        df.dropna(how="all", inplace=True)

        for i in range(len(df)):
            try:
                exam_name = df['quiz'][i]
                q_category = df['category'][i]
                q_subcategory = df['sub_category'][i]
                exam, crt = Exam.objects.get_or_create(name=exam_name, exam_type=Exam.EXAM)
                q_text = df['content'][i]
                q_explanation = df['explanation'][i]
                correct_answer_text = df['correct'][i]
                wrong_1 = df['answer1'][i]
                wrong_2 = df['answer2'][i]
                wrong_3 = df['answer3'][i]
                if q_text != "n" and correct_answer_text != "n" and str(q_text) != "nan" and q_text != " ":
                    q, crt = Question.objects.get_or_create(exam=exam, text=q_text)
                    if crt:
                        q.explanation = q_explanation
                        q.text = q_text
                        q.category = q_category
                        q.subcategory = q_subcategory
                        q.save()
                        Answer.objects.create(question=q, text=correct_answer_text, correct=True)
                        Answer.objects.create(question=q, text=wrong_1)
                        Answer.objects.create(question=q, text=wrong_2)
                        Answer.objects.create(question=q, text=wrong_3)
            except:
                print("Skip row")
        messages.info(self.request, "your exam data imported successfully.")
        return FormView.form_valid(self, form)

    def get_context_data(self, **kwargs):

        context = super(ExamImportView, self).get_context_data()
        context["opts"] = Exam._meta
        return context


class DownloadFileView(View):
    template_name = "exam/exam_list.html"

    def get(self, request, *args, **kwargs):
        # path = "assets/materials"
        path = os.path.join(STATICFILES_DIRS[0], "materials")
        file_path = os.path.join(path, kwargs.get('slug'))
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404


class PresentationSlideShow(TemplateView):

    template_name = 'elearning/includes/presentation_slide.html'

    def get_context_data(self, **kwargs):

        context = super(PresentationSlideShow, self).get_context_data()
        topic = self.request.GET.get('topic', None)
        elearning = self.request.GET.get('elearning', None)

        slides = Presentation.objects.filter(topic=topic, elearning=elearning).values_list('slide', flat=True)
        context["media"] = MEDIA_URL
        context["slides"] = slides
        context["seen_slide"] = 1
        context["previous_slide"] = 0
        context["total_slides"] = len(slides)

        return context
