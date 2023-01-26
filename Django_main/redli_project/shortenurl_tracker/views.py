from pickle import OBJ
from socket import MsgFlag
from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib
import pyshorteners
from .models import data,s_data
import json
# Create your views here.

def home(request):
    return render(request,"home.html")

def help(request):
    return render(request, "help.html")

def track(request):
    if request.method=='POST':
        url=request.POST['user_url']
        resp=requests.get(url)
        class IPQS:
            key = 'JAEvaHs7q9yYVhuWRL3tm7sLc1iqRRNq'
            def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
                url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
                x = requests.get(url, params = vars)
                #print(x.text)
                return (json.loads(x.text))
        URL = url
        strictness = 0
        additional_params = {
            'strictness' : strictness
        }
        ipqs = IPQS()
        result = ipqs.malicious_url_scanner_api(URL, additional_params)
        safe = result['unsafe']
        if result['unsafe']==False:
            safe = "Clean URL - SAFE"
        else:
            safe = "This is not safe site"
        domain = str(result['domain'])
        ip_address = str(result['ip_address'])
        spamming = result['spamming']
        if result['spamming']==False:
            spamming = "No SPAM Issues detected"
        else:
            spamming = "Spamming"
        malware = result['malware']
        if result['malware']==False:
            malware = "No Malware Issues detected"
        else:
            malware = "Malware Issues detected"
        phish = result['phishing']
        if result['phishing']==False:
            phish = "No Phishing Issues detected"
        else:
            phish = "Phishing Issues"
        server = result['server']
        redirect_url = resp.history
        obj=data()
        obj.entered_url=url
        obj.end_url=resp.url
        obj.safe=safe
        obj.domain=domain
        obj.ip_address=ip_address
        obj.spamming=spamming
        obj.Malware=malware
        obj.Phishing=phish
        obj.Server=server
        obj.save()
        if resp.history:
            msg="Yes the url is redirected"
            blw_msg="Here the following redirected chain......."
            return render(request, "track.html", {"redirection":redirect_url, "end_url":resp, "message":msg,
            "lower_msg":blw_msg, "safer":safe, "domain":domain, "ip":ip_address, "spam":spamming, "mal":malware,
            "phish":phish, "server":server})
        else:
            nmsg="URL is not Redirected"
            return render(request,"not.html", {"negative":nmsg, "safer":safe, "domain":domain, "ip":ip_address,
            "spam":spamming, "mal":malware, "phish":phish, "server":server})

def shome(request):
    return render(request, "url_shorten.html")

def shorten(request):
    if request.method=='POST':
        user_url = request.POST['long_url']
        shortener=pyshorteners.Shortener(api_key="60c2647daf13836b963d3672c2a1909fda6c897b")
        shortened_url=shortener.bitly.short(user_url)
        obj1=s_data()
        obj1.original=user_url
        obj1.shorted=shortened_url
        obj1.save()
        return render(request, "result.html", {"tiny_url":shortened_url, "Original":user_url})
