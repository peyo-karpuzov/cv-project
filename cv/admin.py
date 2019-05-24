from django.contrib import admin
from .models import ApplicantUser, MotivationLetter, CVGeneral, CVWorkPlaces, CVEducation, CVLanguages

admin.site.register(ApplicantUser)
admin.site.register(MotivationLetter)
admin.site.register(CVGeneral)
admin.site.register(CVWorkPlaces)
admin.site.register(CVEducation)
admin.site.register(CVLanguages)