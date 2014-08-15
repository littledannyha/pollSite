from django.contrib import admin
from polls.models import Poll, Choice
# Register your models here.

#changes the layout from fat entry boxes to skinny entry boxes
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#controls the feel of the polls admin page
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question']}),
        ('Date Information',{'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]
#    columns displayed in the polls view
    list_display = ('question','pub_date','was_published_recently')

#    adds a filter
    list_filter = ['pub_date']
#    adds a search field
    search_fields = ['question']
admin.site.register(Poll,PollAdmin)

