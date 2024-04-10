from django.contrib import admin
from userformdata.models import MovieBooking

class MovieBookingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'name', 'email', 'quantity', 'date', 'time']
    search_fields = ['movie', 'name', 'email']
    list_filter = ['movie', 'date']

admin.site.register(MovieBooking, MovieBookingAdmin)

