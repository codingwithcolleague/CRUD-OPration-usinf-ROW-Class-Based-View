from django.shortcuts import redirect, render
from django.views import View
from . models import Metro
from . forms import MetroForm,MetroModelForm

# Create your views here.

class TicketListView(View):
    def get(self,request):
        queryset = Metro.objects.all()
        return render(request,"ticket/home.html" , { "query" : queryset} )
    

class TicketCreateView(View):
    def get(self,request):
        form = MetroForm()
        return render(request,"ticket/create.html" , { "form" : form } )
    
    def post(self,request):
        form = MetroForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            mobile = form.cleaned_data.get('mobile')
            startplace = form.cleaned_data.get('startplace')
            endplace = form.cleaned_data.get('endplace')
            status = form.cleaned_data.get('status')
            Metro.objects.create(name=name,mobile=mobile,startplace=startplace,endplace=endplace,status=status)
            return redirect('/ticket')
        return render(request,"ticket/create.html" , { "form" : form } )
    
class TicketEditView(View):
    def get(self,request,id):
        id = self.kwargs.get('id')
        obj = Metro.objects.get(id=id)
        print("obj",obj)
        form = MetroModelForm(instance=obj)
        return render(request,"ticket/create.html" , { "form" : form } ) 
    
    def post(self,request,id):
        id = self.kwargs.get('id')
        obj = Metro.objects.get(id=id)
        form = MetroModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/ticket')
        return render(request,"ticket/create.html" , { "form" : form } ) 
    
class TicketDeleteView(View):
    def get(self,request,id):
        id = self.kwargs.get('id')
        obj = Metro.objects.get(id=id)
        obj.delete()
        return redirect('/ticket')
