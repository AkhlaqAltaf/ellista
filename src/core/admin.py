from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
    site_header = 'Ellista International Reality'
    site_title = 'Ellista International Admin Dashboard'
    index_title = 'Welcome to Ellista Admin Panel'
admin_site = MyAdminSite(name='myadmin')

