from django.shortcuts import render
from django.utils.functional import cached_property
from myapp.blog.models import PyBlog, PyBlogDetail
from myapp.coding.models import PyCoding
import logging as log

from django.views import generic

class menuMixin(object):
    # @cached_property는 아래 매소드로 만든 메뉴 데이터를 실행할 때마다 db에서 가져오는 자원 낭비를 막기 위해 캐시하는 것으로 쓰인다.
    @cached_property
    def getMenuList(self):
        return {
            'blog_menu':PyBlog.objects.all(),
            'coding_menu':PyCoding.objects.all(),
            }
        
class customHandler404(generic.View):
    def get(self, request, *args, **kwargs):
        context = menuMixin().getMenuList
        return render(request, "errors/404.html", context)
    
def handler500(request):
    context = menuMixin().getMenuList
    response = render(request, "errors/500.html", context=context)
    response.status_code = 500
    return response

class TagMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(tags__icontains=q)
        return queryset
    
# naver cloud platform
import json
import requests
import time
import base64
import hashlib
import hmac
from django.http import HttpResponse

class NaverOutboundMailer(generic.TemplateView):
    def __init__(self):
        self.ncp_access_key = 'CSUAq1nV17VOVLNoa8Oc'
        self.ncp_secret_key = 'LDZFX2wsUlVDWskXmvWnlhHCu9EoiImHt88bTDYJ'
        self.ncp_mail_url = 'https://mail.apigw.ntruss.com/api/v1/mails'
        self.ncp_sig_url = '/api/v1/mails'
        
    def post(self, request, *args, **kwargs):
        return self.send(request.POST['mailBody'])
    
    def send(self, mailBody):
        self.timestamp = str(int(time.time() * 1000))
        result = 'N'
        if self.make_signature():
            try:
                data = """ {"templateSid": 7696,
                            "recipients": [{"address": "fpdjxpa37@gmail.com",
                            "name": "bumtaehyeon",
                            "type": "R",
                            "parameters": {"q": "%s"}],
                            "individual":true,
                            "advertising": false
                    }""" % str(mailBody)
                    
                headers = {"Content-Type":'application/json', "x-ncp-apigw-timestamp":self.timestamp, "x-ncp-iam-access-key":self.ncp_access_key, "x-ncp-apigw-signature-v2":self.signingKey}
                response = requests.post(self.ncp_mail_url, headers=headers, data=data.encode('utf-8'))
                rescode = response.status_code
                
                if(rescode==201):
                    result = json.loads(response.text)
            except Exception as e:
                print("mail send: ", e)
        return HttpResponse(json.dumps({"isSend":result}), content_type="application/json")
    
    def make_signature(self):
        try:
            secret_key = bytes(self.ncp_secret_key, 'UTF-8')
            method = "POST"
            message = method + " " + self.ncp_sig_url + "\n" + self.timestamp + "\n" + self.ncp_access_key
            message = bytes(message, 'UTF-8')
            self.signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
            return True
        except Exception as e:
            return False