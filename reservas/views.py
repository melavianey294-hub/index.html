from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Reserva

# Cliente Views
class ClienteListView(ListView):
    model = Cliente
    template_name = 'reservas/cliente_list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'reservas/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'reservas/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'reservas/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


# Reserva Views
class ReservaListView(ListView):
    model = Reserva
    template_name = 'reservas/reserva_list.html'

class ReservaCreateView(CreateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/reserva_confirm_delete.html'
    success_url = reverse_lazy('reserva_list')
