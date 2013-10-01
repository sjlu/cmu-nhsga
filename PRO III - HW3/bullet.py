import direct.directbase.DirectStart 
from pandac.PandaModules import *
from pandac.PandaModules import TextNode
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.interval.MetaInterval import *
from direct.interval.LerpInterval import *
from direct.interval.FunctionInterval import Func
from direct.actor.Actor import Actor
from pandac.PandaModules import NodePath
from direct.gui.DirectGui import *
from direct.task import Task
from math import *
from collisions import *
from direct.showbase.Messenger import Messenger

BULLET_SPEED = 0.1

class Bullet(DirectObject):
    def __init__(self, loc, xDir, yDir, ownerId, handle):        
        self.cHandler = handle
        self.model = Actor("models/bullet2.egg")
        self.model.reparentTo(render)
        self.model.setScale(.01)
        self.model.setHpr(0, 0, 0)
        self.model.setPos(loc)
        
        self.dX = xDir * BULLET_SPEED
        self.dY = yDir * BULLET_SPEED
        
        #collisions
        node = createColSphere( self.model, "tankSphere"+str(ownerId), 10 )
        
        #bugggg
        node.show()
        
        setColMask( self.model, 16 )
        TrevAddCol( node, self.cHandler )
        addPattern( self.cHandler, "bulletSphere"+str(ownerId)+"-into-arena" )
        addPattern( self.cHandler, "bulletSphere"+str(ownerId)+"-into-tankSphere" )
        self.accept( "bulletSphere"+str(ownerId)+"-into-arena", self.collideWithWall )
        self.accept( "bulletSphere"+str(ownerId)+"-into-tankSphere", self.collideWithTank )
        
        self.colName =  "bulletSphere"+str(ownerId)
        
        self.stopTask = 0
        
        #taskMgr.add(self.moveBullet, "MoveBullet")
        
        f1 = Func(self.moveBullet)
        
        w = Wait(0.01)
        
        self.sequence = Sequence(w, f1)
        self.sequence.loop()
        
    def collideWithWall( self, obj ):
        if obj.getFromNode().getName()[-1] == self.colName[-1] and obj.getFromNode().getName()[-2] == self.colName[-2]:
            #print "wall collided"
            self.model.delete()
            self.stopTask = 1
        #print obj.getFromNode().getName()
    
    def collideWithTank( self, obj ):
        if obj.getFromNode().getName()[-1] == self.colName[-1] and obj.getFromNode().getName()[-2] == self.colName[-2]:
            self.model.delete()
            self.stopTask = 1
            
            #make sure the name doesn't start with "Box..." but rather "tanksphere..."
            if obj.getIntoNode().getName()[0] != 'B':
                messenger.send("bullet"+obj.getIntoNode().getName()[-1])
            
            
    def moveBullet(self):
        if( self.stopTask == 1 ):
            self.sequence.finish()
            return 0
        
        pos = self.model.getPos()
        
        posX = pos[0] + self.dX
        posY = pos[1] + self.dY
        
        self.model.setPos(posX, posY, pos[2])