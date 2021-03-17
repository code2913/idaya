from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
    path('',views.HomepageView.as_view(),name="hompage"),  
    path('kitchen',views.Kitchen.as_view(),name="kitchen"),  
    path('bedroom',views.Bedroom.as_view(),name="bedroom"),  
    path('office',views.Office.as_view(),name="office"),
    path('funiture',views.Furniture.as_view(),name="furniture"),  
    path('door-and-window',views.Door.as_view(),name="door"),  
    path('decoration',views.Decoration.as_view(),name="decoration"),  
    path('contact-us',views.Contact.as_view(),name="contact"),  

]
