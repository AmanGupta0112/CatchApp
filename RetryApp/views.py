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
from .comment_analysis import Sentiment_Analysis as csa
from .twitters_App import Sentiment_Analysis as tsa
from .rec import Recommend
from django.contrib.auth.decorators import login_required

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

class TreApp(generic.TemplateView):
    template_name = 'RetryApp/tre_app.html'
    def get_context_data(self,*args,**kwargs):
        context = super(TreApp,self).get_context_data(*args, **kwargs)
        context['Tre_app'] = AppDetails().Trending()
        return context

class NewSoft(generic.TemplateView):
    template_name = 'RetryApp/newsoft.html'
    def get_context_data(self,*args,**kwargs):
        context = super(NewSoft,self).get_context_data(*args, **kwargs)
        context['New_soft'] = SoftwareDetails().NewRelease()
        return context

class TreSoft(generic.TemplateView):
    template_name = 'RetryApp/tresw.html'
    def get_context_data(self,*args,**kwargs):
        context = super(TreSoft,self).get_context_data(*args, **kwargs)
        context['Tre_soft'] = SoftwareDetails().Trending()
        return context

class NewWeb(generic.TemplateView):
    template_name = 'RetryApp/newweb.html'

def searchview(request):
    option = request.GET.get('dropdown')

    if option == 'Application':
        ans = request.GET.get('search-box')
        # import pdb; pdb.set_trace()
        app_info,app_detail = AppDetails().searchapp(ans)
        try:
            sa_ls = tsa.Analysis(str(ans))
            rating = round(app_info['score'],2)
        except:
            rating = ""
            sa_ls = ''
        return render(request,
                      'RetryApp/searched_app.html',
                      {
                      'app_info':app_info,
                      'appdetail':app_detail,
                      "rating":rating,
                      "sa_ls":sa_ls,
                      })

    elif option == 'Software':
        ans = request.GET.get('search-box')
        logo,download,detail,disc =  SoftwareDetails().searchedsoftware(ans)
        try:
            sa_ls = tsa.Analysis(ans)
        except:
            sa_ls = ""
        data = {
        "Title":detail[1],
        "Size":detail[3],
        "Requirements":detail[5],
        "Language":detail[7][:34],
        "Available_languages":detail[9],
        "Price":detail[11]
        }
        return render(request,
                     'RetryApp/searched_soft.html',
                     {
                     'logo':logo,
                     "download":download,
                     'detail':data,
                     'disc':disc[0],
                     "sa_ls":sa_ls,
                     })

    elif option == 'WebSites':
        ans = request.GET.get('search-box')

        url,field_name,g_ranks_val,c_ranks_val,disc,Traffic_val,search_tra,p_search_tra,backlinks,logo = WebsiteDetails().searchedwebsite(ans)
        try:
            sa_ls = tsa.Analysis(ans)
        except Exception as e:
            sa_ls = ""
            print(e)
        return render(request,
                     'RetryApp/searched_web.html',
                     {
                     "field_name":url,
                     'disc':disc,
                     "title" : ans + ".com",
                     "g_ranks_val":g_ranks_val,
                     "c_ranks_val":c_ranks_val,
                     "Traffic_val":Traffic_val,
                     "search_tra":search_tra,
                     "p_search_tra":p_search_tra,
                     "backlinks":backlinks,
                     "logo":logo,
                     "sa_ls":sa_ls,
                     })
    else:
        return HttpResponse("Select the option first")


@login_required
def RecommendationView(request):
    request_post=request
    app_data , sw_dict = Recommend(request_post)
    context = {
    "app_data" : app_data,
    "sw_data" : sw_dict
    }
    return render(request,'RetryApp/reccomend.html',context)
