from FractalWorld import *
import sys

world = FractalWorld(width=800,height=800,delay=0)
t = Fractal(draw=True)

if sys.argv[1]=='tree.fdl':
  pu(t)
  lt(t,90)
  bk(t,200)
  pd(t)

class rule(object):
 def __init__(self):
  self.rule={}

 def rule1(self,left,right):
  self.rule[left]=right

 def udv(self,lista,depth):
  if depth<=0:
   return lista
  liste=[]
  for i in lista:
   if i not in self.rule:
    liste.append(i)
   else:
    liste.append(self.udv(self.rule.get(i),depth-1))
  return liste

class command(object):
 def __init__(self,cmd,a):
  self.cmd=cmd
  self.a=a

 def udf(self,turtle,length):
  if self.cmd=="fd":
   fd(turtle,length[0])
  if self.cmd=="bk":
   bk(turtle,length[0])
  if self.cmd=="lt":
   lt(turtle,int(self.a[0]))
  if self.cmd=="rt":
   rt(turtle,int(self.a[0]))
  if self.cmd=="scale":
   length[0]=length[0]*float(self.a[0])

class fractal(object):
 def __init__(self,start,regler,commando,length,depth):
  self.start=start
  self.regler=regler
  self.commando=commando
  self.length=[length]
  self.depth=depth

 def tegn(self,lista):
  for i in lista:
   if type(i)==list:
    self.tegn(i)
   else:
    cmd=self.commando.get(i)
    cmd.udf(t,self.length)

def read():
  commando={}
  r=rule()
  filex = open(sys.argv[1])
  for line in filex:
   line=line.strip()
   lista=line.split(' ')
   if 'start' in line:
    start=lista[1:]
   elif 'length' in line:
    length=int(lista[1])
   elif 'rule' in line:
    r.rule1(lista[1],lista[3:])
   elif 'depth' in line:
    depth=int(lista[1])
   elif 'cmd' in line:
    cmd=command(lista[2],lista[3:])
    commando[lista[1]]=cmd
  return fractal(start,r,commando,length,depth)

frac=read()

a=frac.regler.udv(frac.start,frac.depth)
frac.tegn(a)

wait_for_user()
