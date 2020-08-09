from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,FeedBackForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactModel,FeedBackModel,SearchModel
from django.views import generic
from django.core.mail import send_mail
import os
from .searched import AppDetails,SoftwareDetails,WebsiteDetails

# Create your views here.
class ContactUsView(generic.FormView):
    form_class = ContactForm
    model= ContactModel
    success_url = reverse_lazy('home')
    template_name = 'RetryApp/contactus.html'

    def form_valid(self, form):
        subject=form.cleaned_data.get('name')
        message=form.cleaned_data.get('query')
        from_email=form.cleaned_data.get('email')
        contact_no = form.cleaned_data.get('contact_no')

        send_mail(
            subject,
            (message +
            "     Email:- " +from_email+
            "     Mobile no:- " +contact_no),
            from_email,
            ["aman.gupta.vns.0112@gmail.com"],
        )

        return super(ContactUsView, self).form_valid(form)

class FeedbackView(generic.FormView):
    form_class = FeedBackForm
    model= FeedBackModel
    success_url = reverse_lazy('home')
    template_name = 'RetryApp/feedback.html'
    def form_valid(self, form):
        subject=form.cleaned_data.get('subject')
        message=form.cleaned_data.get('feedback')
        from_email=form.cleaned_data.get('email')
        name = form.cleaned_data.get('name')

        send_mail(
            ("Feedback:- " +subject),
            (message +
            "     Email:- " + from_email+
            "     Name :- " + name ),
            from_email,
            ["aman.gupta.vns.0112@gmail.com"],
        )

        return super(FeedbackView, self).form_valid(form)

class NewApp(generic.TemplateView):
    template_name = 'RetryApp/newapp.html'
    def get_context_data(self,*args,**kwargs):
        context = super(NewApp,self).get_context_data(*args, **kwargs)
        context['New_apps'] = AppDetails().NewRelease()
        return context

class NewSoft(generic.TemplateView):
    template_name = 'RetryApp/newsoft.html'

class NewWeb(generic.TemplateView):
    template_name = 'RetryApp/newweb.html'

def searchview(request):

    option = request.GET.get('dropdown')

    if option == 'Application':
        ans = request.GET.get('search-box')
        app_info,app_detail = AppDetails().searchapp(ans)
        rating = round(app_info['score'],2)
        return render(request,'RetryApp/searched_app.html',{'app_info':app_info,'appdetail':app_detail,"rating":rating})

    elif option == 'Software':
        ans = request.GET.get('search-box')
        logo,download,detail,disc =  SoftwareDetails().searchedsoftware(ans)
        data = {
        "Title":detail[1],
        "Size":detail[3],
        "Requirements":detail[5],
        "Language":detail[7],
        "Available_languages":detail[9],
        "Price":detail[11]
        }
        return render(request,'RetryApp/searched_soft.html',{'logo':logo,"download":download,'detail':data,'disc':disc[0]})

    elif option == 'WebSites':
        ans = request.GET.get('search-box')
        field_name,ranks_val,desc,Traffic_val,country_traf,country_traf_val,audiance_interest,img_logo = WebsiteDetails().searchedwebsite(ans)
        return render(request,'RetryApp/searched_web.html',
        {"field_name":field_name,
        "title" : ans+".com",
        "ranks_val":ranks_val,
        "desc":desc,
        "Traffic_val":Traffic_val,
        "country_traf":country_traf,
        "country_traf_val":country_traf_val,
        "audiance_interest":audiance_interest,
        "img_logo":img_logo})
    else:
        return HttpResponse("Select the option first")
