from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # Reservas
    path('reservas/', views.ReservaListView.as_view(), name='reserva_list'),
    path('reservas/nuevo/', views.ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/eliminar/', views.ReservaDeleteView.as_view(), name='reserva_delete'),
]
