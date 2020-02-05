class fractal(object):
 def__init__(self,start,regler,commando,length,depth):
  self.start=start
  self.regler=regler
  self.commando=commando
  self.length=length
  self.depth=depth

 def tegn(self,right):
  for i in right
   if type(i)==list:
    self.tegn(i)
   else:
    cmd=self.commando[i]
    cmd.udf(t,self.length)

 def read():
  commando={}
  r=rule()
  filex = open(filx)
  for line in filex:
   line = line.strip()
   if 'start' in line:
    start=right[1:]
   elif 'length' in line:
    length=int(right[1])
   elif 'rule' in line:
    r.rule1(right[1],right[3:])
   elif 'depth' in line:
    depth=int(right[1])
   elif 'cmd' in line:
    cmd=command(right[1],right[3:])
    commando[right[1]]=cmd
  return fractal(start,r,commando,length,depth)
