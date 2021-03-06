# from django.contrib import admin
# from .models import *
# import pandas
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
# from import_export.results import Result
# from question.models import Question, Answer
#
# from import_export.results import RowResult
#
# class ExamResource(resources.ModelResource):
#     class Meta:
#         model = Exam
#         skip_unchanged = True
#         report_skipped = True
#         raise_errors = True
#         use_transactions = True
#         exclude = ""
#         clean_model_instances = True
#
#     def before_import_row(self, row, **kwargs):
#         # Add code here
#         exam_name = row['quiz']
#         q_category = row['category']
#         q_subcategory = row['sub_category']
#         q_text = row['content']
#         q_explanation = row['explanation']
#         correct_answer_text = row['correct']
#         wrong_1 = row['answer1']
#         wrong_2 = row['answer2']
#         wrong_3 = row['answer3']
#         exam, crt = Exam.objects.get_or_create(name=exam_name, exam_type=Exam.EXAM)
#         q, crt = Question.objects.get_or_create(exam=exam, text=q_text)
#         if crt:
#             q.explanation = q_explanation
#             q.text = q_text
#             q.category = q_category
#             q.subcategory = q_subcategory
#             q.save()
#             Answer.objects.create(question=q, text=correct_answer_text, correct=True)
#             Answer.objects.create(question=q, text=wrong_1)
#             Answer.objects.create(question=q, text=wrong_2)
#             Answer.objects.create(question=q, text=wrong_3)
#
#         return Result()
#
# # def import_data(self, dataset, dry_run=False, raise_errors=False, *args, **kwargs):
# # 	print("import data")
# # for row in dataset:
# # 	exam_name = row[0]
# # 	q_category = row[1]
# # 	q_subcategory = row[2]
# # 	# skip n
# # 	q_text = row[4]
# # 	q_explanation = row[5]
# # 	correct_answer_text = row[6]
# # 	wrong_1 = row[7]
# # 	wrong_2 = row[8]
# # 	wrong_3 = row[9]
# # 	exam, crt = Exam.objects.get_or_create(name=exam_name, exam_type=Exam.EXAM)
# # 	q, crt = Question.objects.get_or_create(exam=exam, text=q_text)
# # 	if crt:
# # 		q.explanation = q_explanation
# # 		q.text = q_text
# # 		q.category = q_category
# # 		q.subcategory = q_subcategory
# # 		q.save()
# # 		Answer.objects.create(question=q, text=correct_answer_text, correct=True)
# # 		Answer.objects.create(question=q, text=wrong_1)
# # 		Answer.objects.create(question=q, text=wrong_2)
# # 		Answer.objects.create(question=q, text=wrong_3)
#
# # return Result()
#
#
# class ExamAdmin(ImportExportModelAdmin):
#     resource_class = ExamResource
#
#
# admin.site.register(Exam, ExamAdmin)
#
#
# # e-learning import/export resource
# class ExamImportExportResource(resources.ModelResource):
#     class Meta:
#         model = ImportExportExam
#         skip_unchanged = True
#         report_skipped = True
#         raise_errors = False
#         # skip_unchanged = True
#         # report_skipped = True
#         # raise_errors = True
#         # use_transactions = True
#         # exclude = ""
#         # clean_model_instances = True
#
#     def import_row(self, row, instance_loader, **kwargs):
#         # overriding import_row to ignore errors and skip rows that fail to import
#         # without failing the entire import
#         print(row, "start")
#         import_result = super(ExamImportExportResource, self).import_row(row, instance_loader, **kwargs)
#         if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
#             # Copy the values to display in the preview report
#             import_result.diff = [row[val] for val in row]
#             # Add a column with the error message
#             import_result.diff.append('Errors: {}'.format([err.error for err in import_result.errors]))
#             # clear errors and mark the record to skip
#             import_result.errors = []
#             import_result.import_type = RowResult.IMPORT_TYPE_SKIP
#
#         return import_result
#
#
#
#     # def before_import_row(self, row, **kwargs):
#     #     print("#"*20)
#     #     print(row)
#     #     print("#"*20)
#     #     print("before import row start", row['id'])
#     #     exam_name = row['quiz']
#     #     q_category = row['category']
#     #     q_subcategory = row['sub_category']
#     #     exam, crt = Exam.objects.get_or_create(name=exam_name, exam_type=Exam.EXAM)
#     #     q_text = row['content']
#     #     q_explanation = row['explanation']
#     #     correct_answer_text = row['correct']
#     #     wrong_1 = row['answer1']
#     #     wrong_2 = row['answer2']
#     #     wrong_3 = row['answer3']
#     #     q, crt = Question.objects.get_or_create(exam=exam, text=q_text)
#     #     if crt:
#     #         q.explanation = q_explanation
#     #         q.text = q_text
#     #         q.category = q_category
#     #         q.subcategory = q_subcategory
#     #         q.save()
#     #         Answer.objects.create(question=q, text=correct_answer_text, correct=True)
#     #         Answer.objects.create(question=q, text=wrong_1)
#     #         Answer.objects.create(question=q, text=wrong_2)
#     #         Answer.objects.create(question=q, text=wrong_3)
#     #
#     #     print("before import row end")
#     #
#     #     return Result()
#
# # def delete_instance(self, instance, using_transactions=True, dry_run=False):
# # 	print(instance)
# # 	print("I'm at delete instance")
# # 	pass
#
#     # def before_import(self, dataset, result, using_transactions, dry_run = False, **kwargs):
#     #     print("before import"*20)
#     #     print("+"*20)
#     #     print(dataset)
#     #     print("+" * 20)
#     #     pass
#
# # for row in dataset:
# # 	exam_name = row[1]
# # 	q_category = row[2]
# # 	q_subcategory = row[3]
# # 	figure = row[4]
# # 	exam, crt = Exam.objects.get_or_create(name=exam_name, exam_type=Exam.EXAM)
# # 	q_text = row[5]
# # 	q_explanation = row[6]
# # 	correct_answer_text = row[7]
# # 	wrong_1 = row[8]
# # 	wrong_2 = row[9]
# # 	wrong_3 = row[10]
# # 	q, crt = Question.objects.get_or_create(exam=exam, text=q_text)
# # 	if crt:
# # 		q.explanation = q_explanation
# # 		q.text = q_text
# # 		q.category = q_category
# # 		q.subcategory = q_subcategory
# # 		q.save()
# # 		Answer.objects.create(question=q, text=correct_answer_text, correct=True)
# # 		Answer.objects.create(question=q, text=wrong_1)
# # 		Answer.objects.create(question=q, text=wrong_2)
# # 		Answer.objects.create(question=q, text=wrong_3)
#
# # return Result()
#
#
# class ExamImportExportAdmin(ImportExportModelAdmin):
#     resource_class = ExamImportExportResource
#
#     def save_model(self, request, obj, form, change):
#         print("save_model" * 20)
#         if change:
#             old_object = self.model.objects.get(id=obj.id)
#             old_elearning = Exam.objects.filter(name=old_object.quiz)[0]
#             old_elearning.name = obj.quiz
#             old_elearning.save()
#             ###Slide and Question can't be switched each other, but just figure's name is able to be updated.###
#             question, created = Question.objects.get_or_create(exam=old_elearning, text=old_object.content)
#             question.text = obj.content
#             question.explanation = obj.explanation
#             question.category = obj.category
#             question.sub_category = obj.sub_category
#             question.save()
#
#             correct_answer, created = Answer.objects.get_or_create(question=question, text=old_object.correct)
#             correct_answer.text = obj.correct
#             correct_answer.save()
#             answer1, created = Answer.objects.get_or_create(question=question, text=old_object.answer1)
#             answer1.text = obj.answer1
#             answer1.save()
#             answer2, created = Answer.objects.get_or_create(question=question, text=old_object.answer2)
#             answer2.text = obj.answer2
#             answer2.save()
#             answer3, created = Answer.objects.get_or_create(question=question, text=old_object.answer3)
#             answer3.text = obj.answer3
#             answer3.save()
#         else:
#             elearning, crt = Exam.objects.get_or_create(name=obj.quiz, exam_type=Exam.ELEARNING)
#             question, created = Question.objects.get_or_create(exam=elearning, text=obj.content)
#             question.text = obj.content
#             question.explanation = obj.explanation
#             question.category = obj.category
#             question.sub_category = obj.sub_category
#             question.save()
#
#             correct_answer, created = Answer.objects.get_or_create(question=question, text=obj.correct)
#             correct_answer.save()
#             answer1, created = Answer.objects.get_or_create(question=question, text=obj.answer1)
#             answer1.save()
#             answer2, created = Answer.objects.get_or_create(question=question, text=obj.answer2)
#             answer2.save()
#             answer3, created = Answer.objects.get_or_create(question=question, text=obj.answer3)
#             answer3.save()
#         obj.user = request.user
#         super().save_model(request, obj, form, change)
#
#
# admin.site.register(ImportExportExam, ExamImportExportAdmin)
