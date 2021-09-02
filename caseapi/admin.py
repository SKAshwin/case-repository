from django.contrib import admin
from .models import CaseMeta, USCircuitCaseMeta, Tag, JudgeRuling, Judges, USJudge

# Register your models here.
admin.site.register(CaseMeta)
admin.site.register(USCircuitCaseMeta)
admin.site.register(Judges)
admin.site.register(USJudge)
admin.site.register(JudgeRuling)
admin.site.register(Tag)
