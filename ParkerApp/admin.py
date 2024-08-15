from django.contrib import admin
from .models import *

admin.site.register(register_table)
admin.site.register(contact_table)
admin.site.register(reservation)
admin.site.register(slots_table)
admin.site.register(subscribers_table)
admin.site.register(feedback_table)