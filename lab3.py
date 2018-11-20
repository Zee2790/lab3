import os
import sys
import json
#from tasks import *
import fileinput
import sys

#import initprop
#from initprop import *
# input comes from STDIN (standard input)
from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')

@app.task
def reverse(string):
    return string[::-1]

@app.task
def mydata(words):
    
    #print 'han is:'
    #print words
    #if c == 1:
       #print 'Hello'  
    for word in words:
        #print word
        if word == 'hon':
           #print  'hi zee'
           global hon
           hon = hon+1
        if word == 'han':
           global han
           han = han+1
        if word == 'den':
           global den
           den = den+1
        if word == 'det':
           global det
           det = det+1
        if word == 'denna':
           global denna
           denna = denna+1
        if word == 'denne':
           global denne
           denne = denne+1
        if word == 'hen':
           global hen
           hen = hen+1
        if word == 'han' or  word == 'hon' or  word == 'den' or  word=='det' or  word=='denna' or word =='denne' or word =='hen':
           global count  
           count = count+1
           




   

def mydata1():
   folder = "/home/ubuntu/a3/data/"
   for file in os.listdir(folder):
    #print file
       filepath = os.path.join(folder, file)
       f = open(filepath, 'r')
       for line in f:
           try:
               data = json.loads(line)
               retweet = data["retweeted"]
               if retweet == 'false':
                  continue
               text = data["text"]
               words = line.split( )
               mydata(words)
                     
                         
           except:
        #print 'not JSON format'
               continue
        
   #print  "Count is: " 

#print  han     
def datadisplay():
    j["hen"] = hen
    j["hon"] = hon
    j["han"] = han
    j["den"] = den
    j["denna"] = denna
    j["denne"] = denne
    j["det"] = det
    j["total"] = count
    
    print  "Count is: " 
    print  j
    return j


j = {}
ans = "0"
count = 0
han = 44;
hen = 0;
hon = 0;
det = 0;
den = 0;
denna = 0;
denne = 0;
#words = None
#f = fileinput.input()

#mydata1()
#datadisplay()  