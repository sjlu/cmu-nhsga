# Author: Shao Zhang and Phil Saltzman
# Last Updated: 3/20/2005
#
# This tutorial is intended as a initial panda scripting lesson going over
# display initialization, loading models, placing objects, and the scene graph.
#
# Step 1: DirectStart contains the main Panda3D modules. Importing it
# initializes Panda and creates the window. The run() command causes the
# real-time simulation to begin

import direct.directbase.DirectStart
from direct.actor.Actor import Actor
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

class ball(DirectObject):
    def __init__ (self,balls):
        #taskMgr.doMethodLater(self,5,self.makeBall,"Ball")
     #   Makes the balls!
        self.ballmodel=Actor("resources/EnemyModel.egg")
        self.ballmodel.loadAnims({"bounce": "resources/banimation.egg"})
        if randint(0,1):
            self.ballmodel.setPos(1,0,10)
        else:
            self.ballmodel.setPos(0,1,10)
        self.ballmodel.reparentTo(render)
        t=1
        self.balllist=balls
        self.balllist.append(self)
        self.destroy=0
        self.dead=0
        self.initmove()
        self.ballcsphere = CollisionSphere(0,0,0.5,0.4)     
        self.ballcnode = CollisionNode('ballcnode') 
        self.ballcnode.addSolid(self.ballcsphere)
        self.ballcnode.setFromCollideMask(BitMask32.allOff())
        self.ballcnode.setIntoCollideMask(BitMask32.bit(1))
        self.ballcnp=self.ballmodel.attachNewNode(self.ballcnode)
        self.ballcnp.show()
        #### 
        # Lighting
        ####
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .8, .7, .7, 1 ) )
        self.directionalLight.setDirection( Vec3( -1, -1, -2 ) )
        self.dl2 = DirectionalLight( "directionalLight" )
        self.dl2.setColor(Vec4(.7, .8,.7,1))
        self.dl2.setDirection(Vec3 (-3,3,2))
        self.dl3= DirectionalLight( "directionalLight" )
        self.dl3.setColor(Vec4(.7,.7,.8,1))
        self.dl3.setDirection(Vec3 (1, -3,0))
        self.ballmodel.setLight(NodePath(self.dl2))
        self.ballmodel.setLight(NodePath(self.dl3))
        self.ballmodel.setLight(NodePath(self.directionalLight))

        
        
    def initmove (self):
        w=Wait(1)
        oldx=self.ballmodel.getX()
        oldy=self.ballmodel.getY()
        if randint(0,1):
            newx=1+oldx
            newy=oldy
        else:
            newy=1+oldy
            newx=oldx
        oldPos=Point3(oldx,oldy,8-oldx-oldy)
        newPos=Point3(newx,newy,8-newx-newy)
        self.destroy+=1
        action=self.ballmodel.actorInterval("bounce")
        i = LerpPosInterval(self.ballmodel,.5,newPos,oldPos)
        fI= Func(self.doneMoving)
        s=Sequence(w,Parallel(action,i),fI)
        s.start()
        
        
        
    def doneMoving (self):
        if self.destroy > 5:
            self.ballmodel.detachNode()
            self.balllist.remove(self)
        else:
            self.initmove()
        
        

class world(DirectObject):
    def __init__ (self):
        cube=loader.loadModel("resources/blue.egg")
        cube.reparentTo(render)
        self.balls=[]
        self.numCount=0
        self.nextMotion=0
        self.cubes=[]
        self.nextcreate=5
        
        #### 
        # Lighting
        ####
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .8, .7, .7, 1 ) )
        self.directionalLight.setDirection( Vec3( -1, -1, -2 ) )
        self.dl2 = DirectionalLight( "directionalLight" )
        self.dl2.setColor(Vec4(.7, .8,.7,1))
        self.dl2.setDirection(Vec3 (-3,3,2))
        self.dl3= DirectionalLight( "directionalLight" )
        self.dl3.setColor(Vec4(.7,.7,.8,1))
        self.dl3.setDirection(Vec3 (1, -3,0))
        
        
        
        for x in range(7):
            row=[]
            for y in range(7):
                row.append(0)
            self.cubes.append(row)
        for x in range(7):
            for y in range(7):
                if(x+y<7):
                    cube=loader.loadModel("resources/blue.egg")
                    cube.setPos(x,y,7-x-y)
                    cube.reparentTo(render)
                    print cube.getName()
                    self.cubes[x][y]=cube
        print "hi"
        base.disableMouse()
        base.camera.setPos(15,15,15)
        base.camera.lookAt(3,3,6)
        self.qbert=Actor("resources/qbert.egg")
        self.qbert.loadAnims({"hop": "resources/qmation.egg"})
        self.qbert.reparentTo(render)
        self.qbert.setPos(0,0,8)
        self.qbert.setH(180)
        self.qbert.setLight(NodePath(self.dl2))
        self.qbert.setLight(NodePath(self.dl3))
        self.qbert.setLight(NodePath(self.directionalLight))
        self.qbertsphere = CollisionSphere(0,0,0.5,0.3)     
        self.qbertcnode = CollisionNode('qbertcnode') 
        self.qbertcnode.addSolid(self.qbertsphere)
        self.qbertcnode.setFromCollideMask(BitMask32.bit(1))
        self.qbertcnode.setIntoCollideMask(BitMask32.allOff())
        #NodePath(self.qbertcnode).reparentTo(self.qbert)
        #self.qbertcnode.reparentTo(self.qbert)
        self.qbertcnp=self.qbert.attachNewNode(self.qbertcnode)
        self.qbertcnp.show()
        self.inMotion=0
        self.accept("arrow_up",self.initMove,[-1,0,270])
        self.accept("arrow_down",self.initMove,[1,0,90])
        self.accept("arrow_right",self.initMove,[0,1,180])
        self.accept("arrow_left",self.initMove,[0,-1,0])
        taskMgr.add(self.makeBalls,"makeBalls")
        taskMgr.add(self.checkcollision,"checkcollision")
        
        self.cTrav = CollisionTraverser()
        self.cHandler = CollisionHandlerQueue()
        
        self.cTrav.addCollider(self.qbertcnp, self.cHandler)
        
    def checkcollision (self,task):
        self.cTrav.traverse(render)
        if self.cHandler.getNumEntries()>0:
            self.cHandler.clearEntries()
            print "I am dead."
        return Task.cont
            
        
    def makeBalls (self,task):
        t=task.time
        if t>=self.nextcreate:
            self.nextcreate+=5
            ball(self.balls)
        return Task.cont
        
    def initMove (self,x,y,hed):
        if self.inMotion:
            self.nextMotion=[x,y,hed]
            return
        # print "Hi there"
        action=self.qbert.actorInterval("hop")
        fI=Func(self.doneMoving)
        oldx=self.qbert.getX()
        oldy=self.qbert.getY()
        newx=x+oldx
        newy=y+oldy
        oldPos=Point3(oldx,oldy,8-oldx-oldy)
        newPos=Point3(newx,newy,8-newx-newy)
        
        i = LerpPosInterval(self.qbert,.5,newPos,oldPos)
        self.inMotion=1
        self.qbert.setH(hed)
        s=Sequence(Parallel(action,i),fI)
        s.start()
        
        
    def doneMoving (self):
        self.inMotion=0
        oldPos=self.qbert.getPos()
       
        
        if self.qbert.getX()<0 or self.qbert.getY()<0 or self.qbert.getZ()<2:
           print "AHHH"
           w=Wait(.5)
           i=LerpPosInterval(self.qbert,2,Point3(oldPos[0],oldPos[1],oldPos[2]-100),oldPos)
           s=Sequence(w,i)
           s.start()
        else:
            print "atleast getting here"
            
            x=int(self.qbert.getX())
            y=int(self.qbert.getY())
            print self.numCount , self.cubes[x][y].getName()
            if self.cubes[x][y].getName() =="blue.egg":
                self.numCount +=1
                print self.numCount
            self.cubes[x][y].detachNode()  
            self.cubes[x][y]=loader.loadModel("resources/Yellow")
            self.cubes[x][y].setPos(x,y,7-x-y)
            self.cubes[x][y].reparentTo(render)
        if self.nextMotion!=0:
            self.initMove(self.nextMotion[0],self.nextMotion[1],self.nextMotion[2])
            self.nextMotion=0
        if self.numCount==28:
            print "PARTY!"

w=world()
run()


