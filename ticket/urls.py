from django.urls import path
from  .views import TicketListView,TicketCreateView,TicketEditView,TicketDeleteView


urlpatterns = [
    path('' , TicketListView.as_view() , name="home"),
    path('create/' , TicketCreateView.as_view() , name="create"),
    path('edit/<int:id>/' , TicketEditView.as_view() , name="edit"),
    path('delete/<int:id>/' , TicketDeleteView.as_view() , name="delete")

]