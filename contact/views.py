import json
# import requests
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from .forms import CreateContactForm
from .models import ContactUs
# from Experience import settings


def contact(request):
    # site_key_captcha = settings.GOOGLE_RECAPTCHA_SITE_KEY
    # secret_key_captcha = settings.GOOGLE_RECAPTCHA_SECRET_KEY
    # if request.user.is_authenticated:
    #     email = get_user(request).email
    # else:
    #     email = None
    contact_form = CreateContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            fullname = contact_form.cleaned_data.get('fullname')
            email = contact_form.cleaned_data.get('email')
            call = contact_form.cleaned_data.get('call')
            subject = contact_form.cleaned_data.get('subject')
            text = contact_form.cleaned_data.get('text')

            # captcha_token = request.POST.get("g-recaptcha-response")
            # cap_url = "https://www.google.com/recaptcha/api/siteverify"
            # cap_secret = secret_key_captcha
            # cap_data = {"secret": cap_secret, "response": captcha_token}
            # cap_server_response = requests.post(url=cap_url, data=cap_data)
            # cap_json = json.loads(cap_server_response.text)
            # if cap_json['success'] == False:
            #     messages.error(request, "تیک من ربات نیستم را علامت بزنید", extra_tags='contact_message_error')
            # else:
            ContactUs.objects.create(fullname=fullname,call=call, email=email, subject=subject, text=text, is_read=False)
            contact_form = CreateContactForm()
        else:
            contact_form = CreateContactForm()

    context = {
        # 'site_key_captcha': site_key_captcha,
        'contact_form': contact_form,
    }

    return render(request, 'contact.html', context)
