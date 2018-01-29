from requests import request, Session
from getpass import getpass
import time
web_url = 'http://localhost/cobauntukpython/'
uri_request = {
    'home':'?p=home',
    'login':'?p=login',
    'logout':'?p=logout',
    'download':'?p=download&file=',
    'upload':'?p=upload'
}
data_form={
    'username':'joko',
    'password':'',
    'login':''
}
data_form['password'] = getpass('Input your password : ')
open_sess = Session()

def login(form):
    resp = open_sess.post(web_url+uri_request['login'],data=form)
    if resp.status_code==200:
        return True, resp

    return False, resp

login_r, resp = login(data_form)
if login_r==True:
    print resp.status_code
    print 'request headers'
    print open_sess.headers
    print 'content'
    print resp.content
    print 'response header'
    print resp.headers

    resp = open_sess.post(web_url+uri_request['download']+'01.csv')
    print 'request header when download'
    print open_sess.headers
    print 'downloading file....'
    print resp.status_code
    print 'view download response header'
    print resp.headers
    with open('ambil--'+str(time.time())+'.csv','wb') as file:
        file.write(resp.content)

    data_upload = {'a':'aa','b':'bb','c':'cc'}
    multipart = [
        ('file[]',('up1.csv',open('up1.csv','rb'),'text/csv')),
        ('file[]',('up2.csv',open('up2.csv','rb'),'text/csv'))
    ]
    resp = open_sess.post(web_url+uri_request['upload'],files=multipart,data=data_upload)
    print resp.status_code
    print resp.content

