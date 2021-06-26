import json
import requests
import lxml.html
import lxml.etree
import sendgrid
import os
from sendgrid.helpers.mail import *

CompanyCollection=[]
with open('finalconfig.json','r') as f:
    config=json.load(f)
for company in config["Companies"]:    
    name,industry,accessurl,id,ratiourl=company.values()
    cooky={'_gcl_au':'1.1.186761279.1613983464','_ga':'GA1.2.678724411.1613983464','_gid':'GA1.2.1626534257.1617941896', 'csrftoken':'DTEWPQuHiDsqBNeqJyOpc7ZmhBeFXeUy5R8zz0Cv1ay5odqSzzjE41i7uwpiecKW', 'sessionid':'yrun45v0hbjau1eajwnhfw37angsdgls'}    
    data=requests.get(ratiourl,cookies=cooky)
    doc = lxml.html.fromstring(data.content)
    ratio=[]
    ratio=doc.xpath("//*[contains(@class, 'number')]/text()")    
    if(len(ratio)>5):        
        magicratio=str(ratio[5]).find(',')
        if(magicratio<0):
            if (float(ratio[5])>=2):
                CompanyCollection.append(name+" ==> "+ratio[5])
print(CompanyCollection)
#sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#from_email = Email("kallepalliraviteja@gmail.com")
#to_email = To("kallepalliraviteja@gmail.com")
#subject = "magicration > 2"
#content = Content("text/plain", json.dumps(CompanyCollection))
#mail = Mail(from_email, to_email, subject, content)
#response = sg.client.mail.send.post(request_body=mail.get())
#old
#'_gcl_au'='1.1.186761279.1613983464'; '_ga'='GA1.2.678724411.1613983464';'_gid'='GA1.2.1626534257.1617941896'; 'csrftoken'='DTEWPQuHiDsqBNeqJyOpc7ZmhBeFXeUy5R8zz0Cv1ay5odqSzzjE41i7uwpiecKW'; 'sessionid'='yrun45v0hbjau1eajwnhfw37angsdgls'
#new
#'csrftoken'='SQbUm8ZqGtP9JoANN7QlhMKreWFMwfK3IrQG2Y7BCA7tQvYfm6CRYJcFBGVuQF4k','_gcl_au'='1.1.186761279.1613983464','_ga'='GA1.2.678724411.1613983464','_gid'='GA1.2.679438925.1615025394','sessionid'='2mul0orlr1a2l289hqgqrknzw5r8svxd'
