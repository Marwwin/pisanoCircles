#%%

## THIS CELL COUNTS THE PISANO PERIODS

import time 
import numpy as np
import os

def fib(n):
  res = [0,1]
  return fibHelper(n,2, res)

def fibHelper(n,i,res):
  if len(res) == n:
    return res
  else:
    res.append(res[i-1]+res[i-2])
    i += 1
    return fibHelper(n,i,res)

def getPisano(modulo):
  fibb = np.array(fib(5000))
  modulatedFibb = fibb%modulo
  series = findPeriod(modulatedFibb)
  return series

def findPeriod(fList):
  for f in range(len(fList)):
    valueToTest = "".join(list(map(str,fList[0:f+1])))
    against = "".join(list(map(str,fList[f+1:(f+1)*2])))
    against2 = "".join(list(map(str,fList[(f+1)*2:(f+1)*3])))
    
    if valueToTest == against and valueToTest == against2:
      #print(valueToTest[10:20])
      #print(len(valueToTest), len( "".join(list(map(str,fList[0:f+1])))))
      #print(len(against),len("".join(list(map(str,fList[f+1:(f+1)*2])))))
      #print(len(against2),len("".join(list(map(str,fList[(f+1)*2:(f+1)*3])))))
      return fList[0:f+1]

sys.setrecursionlimit(10000)

startT = time.time()

pisanoPeriods = {}
for i in range(1,251):
  period = getPisano(i)
  pisanoPeriods.update({i:period})

print("Runtime:",time.time() - startT)

#%%

## GET THE TURTLE READY FOR ACTION

import turtle

s = turtle.getscreen()
s.setup(startx=20,starty=20)
t = turtle.Turtle()
#%%

def getCircleData(period):
  return len(pisanoPeriods[period])

def getAllPoints(p):
  points = []
  for i in range(p):
    t.circle(50,360/p)
    points.append(t.pos())
  return points

def drawPisano(mod):
  currentPeriod = pisanoPeriods[mod]
  points = getAllPoints(mod)
  for i in range(len(currentPeriod)):
    t.goto(points[currentPeriod[i]])
#drawPisano(8)

t.clear()
t.speed(0)
cn = 0
yValue = 400
for i in range(60,100):
  t.pu()
  xValue = -400+(115*(cn%8))
  if cn %8 == 0:
    yValue -= 115
  t.setpos(xValue,yValue)
  t.pd()
  drawPisano(i)
  cn += 1

#t.circle(100,360/5)
#t.pos()

#%%

s.exitonclick()


