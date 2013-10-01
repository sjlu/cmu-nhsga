import direct.directbase.DirectStart 
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task 
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import * 
from random import randint
from direct.gui.OnscreenText import *
from collisions import *

class World(DirectObject):
    def __init__ (self):
        #LOADING THE ENVIRONMENT
        self.environment = Actor("models/enviro.egg")
        self.environment.setScale(.3)
        self.environment.setPosHpr(0,0,0,0,0,0)
        self.environment.reparentTo(render)
        #self.environment.find("**/environment").getChild(0).node().setIntoCollideMask(BitMask32.allOn())
        
        #DISABLING THE MOUSE
        #base.disableMouse()
        
        taskMgr.add(self.checkcollision,"checkcollision")
        
        self.cTrav = CollisionTraverser()
        self.cHandler = CollisionHandlerQueue()
        
        self.cTrav.addCollider(self.subcnp, self.cHandler)
        
        #SETTING THE CAMERA PLACEMENT AND ANGLE
        base.camera.setPosHpr(-1000,-1000,1000,-86,-13,-6.1)
        base.camLens.setFar(1000000)
        
        #SETTING BACKGROUND COLOR
        base.setBackgroundColor(0,0,0)
    
        #LOADING ACTOR AND SETTING POSITION
        self.model = Actor("models/subMod.egg")
        self.model.loadAnims({"pop": "models/subAni.egg"})
        self.model.setScale(.1)
        self.model.setPosHpr(0,0,0,0,0,0)
        self.model.reparentTo(render)

        #SETTING THE COLLISION SPHERE
        self.subcsphere = CollisionSphere(0,0,0.5,0.4)     
        self.subcnode = CollisionNode('subcnode') 
        self.subcnode.addSolid(self.subcsphere)
        self.subbnode.setFromCollideMask(BitMask32.allOff())
        self.subcnode.setIntoCollideMask(BitMask32.bit(1))
        self.subcnp=self.ballmodel.attachNewNode(self.subcnode)
        self.subcnp.show()
    
        # create the 'carrot' object that will be used to easily move the controlled
        # object forward regardless of the objects current heading
        # use this code to 'see' the carrot 
        self.carrot = loader.loadModel( "models/ball.egg" )
        self.carrot.setScale(50)
        ## # use this code normally - don't want to see the carrot
        ## self.tankCarrot = render.attachNewNode( "tankCarrot" )
        # parent the carrot to the object so that it will alway stay with the object 
        self.carrot.reparentTo(self.model)
        # place the carrot a set distance away for the object equal to the distance that 
        # you want the object to move  
        self.carrot.setPos(50, 0, 0) 
        
        self.accept("q-repeat",self.moveModel)
        self.accept("a-repeat",self.turnModelH, [-10])
        self.accept("d-repeat",self.turnModelH, [10])
        self.accept("w-repeat",self.turnModelR, [-10])
        self.accept("s-repeat",self.turnModelR, [10])
        
        self.ringX = 0
        self.ringY = 0
        self.ringZ = 0
        
        self.ring = Actor("models/ring.egg")
        self.model.setPosHpr(self.ringX,self.ringY,self.ringZ,0,0,0)
        self.model.reparentTo(render)
        

    def moveModel(self):
        self.model.setPos(self.carrot.getPos(render))
        
    def turnModelH(self,angle):
        self.model.setH(self.model.getH() + angle)
        
    def turnModelR(self,angle):
        self.model.setR(self.model.getR() + angle)
        
    def collideWithWall( self, obj ):
        if( obj.getFromNode().getName() == self.colName ):
            self.model.setPos( self.model.getPos() - self.calculateVector() )
        
        
w = World()
run()
