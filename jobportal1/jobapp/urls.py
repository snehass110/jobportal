from django.urls import path
from . views import *
urlpatterns=[path('',home),
             # path('logpage/',login1),
             path('register/',regis),
             path('success/',success),
             path('send/',send_mail_regis),
             path('error/',error),
             path('log/',login),
             path('verify/<auth_token>',verify),
             path('log2/',login2),
             path('register2/',regis2),
             path('addjob/<int:id>',addjob),
             path('list_company/',list_company),
             path('sendmail/<int:id>/',sendmail),
             path('update/<int:id>',update),
             path('openings/<int:id>',openings),
             path('viewmore/<int:id>',viewmore),
             path('apply/<int:id>/<int:ids>', apply),
             path('view_applicant/<int:id>',view_applicant),
             path('applied_job/<int:id>',applied_jobs)
             ]
