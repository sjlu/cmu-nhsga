from direct.actor.Actor import Actor
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.interval.LerpInterval import LerpPosInterval
from pandac.PandaModules import *
from direct.interval.FunctionInterval import Func
from direct.interval.MetaInterval import Sequence, Parallel
from direct.interval.FunctionInterval import Wait
from direct.task.Task import *
from pandac.PandaModules import DirectionalLight
from direct.interval.ActorInterval import ActorInterval 
from random import randint
from pandac.PandaModules import Shader
import picker 
import math

class world(DirectObject):
    def __init__ (self):
        
        
    #row = int(hit.getName()[-3])
    #col = int(hit.getName()[-2])
    #type= int(hit.getName()[-1])
        self.lights()
        self.dList=[]
        self.pick=picker.Picker()
        base.accept("objectPicked",self.somethingPicked)
        self.onePick=-1
        self.twoPick=-1
        self.checkNumber=0
        self.board=Actor("resources/Board.egg")
        self.board.reparentTo(render)
        self.board.setScale(.22)
        self.board.setPos(-1.5,16.7,0)
        self.otherGrid=[]
        
        self.xGrid=[]
        base.disableMouse()
        base.camera.setPosHpr(-8.79932, -4.50985, 91.962,-26.7942, -76.1442, -28.9128)
        
        base.setBackgroundColor(0,0,0)
        self.accept("space",self.findCam)
       
        for i in range(8):
            col=[]
            for y in range(8):
                col.append(1)
            self.otherGrid.append(col)
       
                
        for i in range(8):
            col=[]
            for y in range(8):
                col.append(0)
            self.xGrid.append(col)
            
        for x in range(8):
            for y in range(8):
                self.makeAJewel(x,y,randint(0,5))
        #self.checkMatches2()
        #self.deleteThings()
        
        taskMgr.add(self.checkMatches, "checkMatches")
        taskMgr.add(self.deleteThings2, "deleteThings2")
        
    def checkMatches(self, task):
        for x in range(8):
            for y in range(8):
                yVar = y+1
                #print "here1"
                #print str(x)+ str(y) + self.xGrid[x][y].getName()[-1]
                while(yVar<8 and int(self.xGrid[x][y].getName()[-1]) == int(self.xGrid[x][yVar].getName()[-1])):
                    yVar+=1
                    #print yVar
                    #print "here"
                if((yVar-y)>=3):
                     while(yVar>y):
                        yVar-=1
                        self.otherGrid[x][yVar] = 0
                        print "something needs deleting"
                        print self.otherGrid
                        
                yVar = 0
                
        for x in range(8):
            for y in range(8):
                yVar = y+1
                #print "here1"
                #print str(x)+ str(y) + self.xGrid[x][y].getName()[-1]
                while(yVar<8 and int(self.xGrid[y][x].getName()[-1]) == int(self.xGrid[yVar][x].getName()[-1])):
                    yVar+=1
                    #print yVar
                    #print "here"
                if((yVar-y)>=3):
                     while(yVar>y):
                        yVar-=1
                        self.otherGrid[yVar][x] = 0
                        print "something needs deleting"
                        print self.otherGrid
                        
                yVar = 0
        return Task.cont
   # def dropDown(self, task):
    #write stuff here    
                
    def deleteThings(self):
        #print "I work"
        for x in range(8):
            for y in range(8):
                if(self.otherGrid[x][y] == 0):
                   self.otherGrid[x][y] = 1
                   self.xGrid[x][y].delete()
                   self.makeAJewel(x,y,randint(0,5))
        return Task.cont
    
    def deleteThings2(self, task):
        
        for x in range(8):
            for y in range(8):
                if(self.otherGrid[x][y] == 0):
                   self.xGrid[x][y].delete()
                   print "I'm running"
                   self.makeAJewel(x,y,randint(0,5))
                   self.otherGrid[x][y] = 1
        return Task.cont
        
    def makeAJewel(self,x,y,type):
        temp=Actor("resources/Jewel"+str(type))
        temp.setPos(Vec3(x*4,y*4,0))
        temp.setScale(.1)
        temp.setHpr(0,0,0)
        temp.setName("jewel"+str(x)+str(y)+str(type))
        temp.reparentTo(render)
        self.xGrid[x][y]=temp
        self.pick.makePickable(self.xGrid[x][y])
        
        
    def areTouching(self):
        #if abs(self.onePick[1]-self.twoPick[1])==1 and abs(self.onePick[2]-self.twoPick[2])!=1 or abs(self.onePick[2]-self.twoPick[2])==1 and abs(self.onePick[1]-self.twoPick[1])!=1:
       
        if self.onePick[0]==self.twoPick[0] and self.onePick[1]==self.twoPick[1]:
            return 0
        if abs(self.onePick[0]-self.twoPick[0])==1:
            print abs(self.onePick[0]-self.twoPick[0])
            if (self.onePick[1]==self.twoPick[1]):
                
                return 1
        elif abs(self.onePick[1]-self.twoPick[1])==1:
            print abs(self.onePick[1]-self.twoPick[1])
            if(self.onePick[0]==self.twoPick[0]):
                
                return 1
            
    
    def somethingPicked(self):
    
        hit = self.pick.getPickedObj()
        print hit
        
        if hit!= None:
            row = int(hit.getName()[-3])
            col = int(hit.getName()[-2])
            type= int(hit.getName()[-1])
            if self.onePick == -1:
                self.onePick=(row,col,type)
            else:
                self.twoPick=(row,col,type)
                if self.areTouching():
                    self.switchJ(self.onePick,self.twoPick)
                self.onePick=-1
                self.twoPick=-1
        else:
            self.onePick=-1
            self.twoPick=-1

    def switchJ (self,onePick,twoPick):
        oX=onePick[0]
        oY=onePick[1]
        tX=twoPick[0]
        tY=twoPick[1]
        print "from"
        print self.xGrid[oX][oY]
        print self.xGrid[tX][tY]
    
        oL=LerpPosInterval(self.xGrid[oX][oY],.2,Vec3(tX*4,4*tY,0),Vec3(oX*4,4*oY,0))
        tL=LerpPosInterval(self.xGrid[tX][tY],.2,Vec3(oX*4,4*oY,0),Vec3(tX*4,4*tY,0))
        
        print "moving"
        print self.xGrid[oX][oY]
        print self.xGrid[tX][tY]
        f1=Func(self.xGrid[oX][oY].delete)
        f2=Func(self.xGrid[tX][tY].delete)
        f3=Func(self.makeAJewel,oX,oY,twoPick[2])
        f4=Func(self.makeAJewel,tX,tY,onePick[2])
        
        s=Sequence(Parallel(oL,tL),f1,f2,f3,f4)
        s.start()
        
       
    def findCam(self):
        print 'camera: ', camera.getPos(), camera.getHpr() 
    def lights(self):
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .8, .7, .7, .1 ) )
        self.directionalLight.setDirection( Vec3( -1, -1, -2 ) )
        self.dl2 = DirectionalLight( "directionalLight" )
        self.dl2.setColor(Vec4(.7, .8,.7,1))
        self.dl2.setDirection(Vec3 (-3,3,2))
        self.dl3= DirectionalLight( "directionalLight" )
        self.dl3.setColor(Vec4(.7,.7,.8,1))
        self.dl3.setDirection(Vec3 (1, -3,0))
        render.setLight(NodePath(self.directionalLight))
        render.setLight(NodePath(self.dl2))
        render.setLight(NodePath(self.dl3))
        
w=world()
run()