from django.urls import path, include
from . import views
from .views import HomeView, DashboardView, CreateBlogView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('profile/', DashboardView.as_view(), name='profile'),
    path('create/', CreateBlogView.as_view(success_url="/"), name='create_blog'),
    path('search/', views.search, name='search'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='post-delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='post-update'),
    # path('search/', BlogFilterView.as_view(filterset_class=BlogFilter,
    #                                      template_name='index.html'), name='searcher'),

]