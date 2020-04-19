from django.contrib import admin
from . import models

admin.site.register(models.AttendanceRecord) # ,AttendanceRecordAdmin
admin.site.register(models.Prof)


# For reordering apperance in the admin panel - fields
# also adds search facility and filtering options on the right
# list_display shows the entire Model/table in the view with all the columns in the list given

# class AttendanceRecordAdmin(admin.ModelAdmin):
# 	fields = ['dateTime','courseID','studentID']
#	search_fields = ['studentID']
# 	list_filter = ['courseID']
#	list_display = ['dateTime','courseID','studentID'] 