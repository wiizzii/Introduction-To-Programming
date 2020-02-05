from FractalWorld import *
from itertools import chain
import sys
 
world  = FractalWorld(height=1000, width=1000, delay=0)
Jesper = Fractal(draw =False)




if sys.argv[1] == 'tree.fdl':
  pu(Jesper)#Pennen tages op
  lt(Jesper, 90)#Skildpadden vender 90 grader, for en god udgangsposition
  bk(Jesper,200)
  pd(Jesper)#pennen tages ned saa der kan tegnes
else:
#startposition
  pu(Jesper)
  fd(Jesper,-450)
  lt(Jesper,90)
  fd(Jesper,250)
  rt(Jesper,90)
  pd(Jesper)
class Regel(object):
  """Bruger en given regel til det matcherende element i listen 
     Attributes: single lhs letter and a list of letters on the rhs."""
 
  def __init__(self, start = [], regler = {}):
    self.start = start
    self.regler = regler
 
  def app_regel(self, start, dybde):
    if dybde <= 0:
      return list(chain.from_iterable(start))
    else:
      new_list = []
      for i in start:
        if i not in self.regler:
          new_list.append(i)
        else:
          new_list.append(self.app_regel(self.regler[i], dybde-1))
      return list(chain.from_iterable(new_list))
    
class Kommando(object):
  """Udforer kommandoer
     Attributes: command string (fd, lt, rt, scale), list of arguments"""
 
  def __init__(self, start = [], laengde = [], map = {}):
    self.start = start
    self.laengde = laengde
    self.map = map
 
  def udfor(self, start, map):
    self.laengde = eval(self.laengde[0])
    for i in self.start:
      if self.map[i][0] == "fd":
        fd(Jesper, self.laengde)
      elif self.map[i][0] == "bk":
        fd(Jesper, -self.laengde)
      elif self.map[i][0] == "lt":
        lt(Jesper, eval(self.map[i][1][0]))
      elif self.map[i][0] == "rt":
        rt(Jesper, eval(self.map[i][1][0]))
      elif self.map[i][0] == "nop":
        rt(Jesper, 360)
      elif self.map[i][0] == "scale":
        x = eval(self.map[i][1][0])
        self.laengde = x*self.laengde
      
     
     

 
class Fraktal(FractalWorld):
  """Laeser .fdl filen og udforer alle kommandoerne for det givne stadie 
     Attributes: start state(list) represented by a list, list of rules, map from single letter to commands, length, depth"""
 
  def __init__(self):
    self.start = []
    self.regler ={}
    self.map = {}
    self.laengde = []
    self.dybde = []
    

  def oversat(self,fil):
    
    fin = open(fil)
    for line in fin:
      line = line.strip()
      if 'start' in line:
        self.start = line.split()[1:]
      elif 'length' in line:
        self.laengde = line.split()[1:]
      elif 'depth' in line:
        self.dybde = line.split()[1:]
      elif 'rule' in line:
        self.regler[line.split()[1:2][0]] = line.split()[3:]
      elif 'cmd' in line:
        if line.split()[2:3] == ['fd'] or line.split()[2:3] == ['bk']:
          bogstav, cmds, argu = line.split()[1:2], line.split()[2:3], self.laengde
        else:
          bogstav, cmds, argu = line.split()[1:2], line.split()[2:3], line.split()[3:4]
        self.map[bogstav[0]] = [cmds[0], argu]
        
    fin.close()

  def tegn(self):
    self.oversat(sys.argv[1])#Aabner dokumentet
    Kommando(Regel(self.start,self.regler).app_regel(self.start,eval(self.dybde[0])), self.laengde, self.map).udfor(Regel(self.start,self.regler).app_regel(self.start,eval(self.dybde[0])),self.map)
    wait_for_user()
  
 
Fraktal().tegn()
