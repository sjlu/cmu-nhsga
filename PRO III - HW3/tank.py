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
from bullet import *
import sys
from pandac.PandaModules import TransparencyAttrib

TANK_SPEED_MOD = 30
TANK_HEIGHT = 2

class Tank(DirectObject):    
    def __init__(self, cHandler, tankId, rot):
        
        self.isKilled = 1
        self.isExploding = 0
        
        #collisions
        self.handler = cHandler
        
        self.bulletNum = 0
        self.tankId = tankId
        self.rot = rot
        
        self.model = Actor("models/tank"+str(self.tankId)+".egg")
        self.model.setScale(.01)
        
        #self.spawnTank()
        
        if tankId == 0:
            self.damageXPos = cos(radians(-45))
            self.damageYPos = sin(radians(-45))
        elif tankId == 1:
            self.damageXPos = cos(radians(-135))
            self.damageYPos = sin(radians(-135))
        elif tankId == 2:
            self.damageXPos = cos(radians(135))
            self.damageYPos = sin(radians(135))
        elif tankId == 3:
            self.damageXPos = cos(radians(45))
            self.damageYPos = sin(radians(45))
            
        self.tankDamageTextRot = 0
        
        self.tankDamage = 0
        self.tankDamageText = OnscreenText(text="Damage: "+str(self.tankDamage)+" %", style=1, fg=(1,1,1,1), pos=(self.damageXPos,self.damageYPos), scale = .07)
        self.tankDamageText.setHpr(0, 0, self.tankDamageTextRot)
        
        self.texHolder = []
        
        for i in range(1,18):
            self.texHolder.append(loader.loadTexture("explosion/frame"+str(i)+".tif"))
    def spawnTank(self):
        self.model = Actor("models/tank"+str(self.tankId)+".egg")
        self.model.reparentTo(render)
        self.model.setScale(.01)
        
        #collisions
        node = createColSphere( self.model, "tankSphere"+str(self.tankId), 160)
        node.setName( "tankSphere%d" % self.tankId )
        #node.show()
        setColMask( self.model, 16 )
        TrevAddCol( node, self.handler )
        addPattern( self.handler, "tankSphere"+str(self.tankId)+"-into-arena" )
        addPattern( self.handler, "tankSphere"+str(self.tankId)+"-again-arena", "Again" )
       
        self.accept( "tankSphere"+str(self.tankId)+"-into-arena", self.collideWithWall )
        self.accept( "tankSphere"+str(self.tankId)+"-again-arena", self.collideWithWall )
        self.colName =  "tankSphere"+str(self.tankId)
        base.accept( "bullet"+self.colName[-1], self.collideWithBullet )
        
        degrees = 0
        
        if self.tankId == 0:
            degrees = -45
        elif self.tankId == 1:
            degrees = -135
        elif self.tankId == 2:
            degrees = 135
        elif self.tankId == 3:
            degrees = 45
        
        x = cos(radians(degrees)) * 15
        y = sin(radians(degrees)) * 15
                
        self.model.setPos(x, y, TANK_HEIGHT)
        self.model.setHpr(self.rot, 0, 0)
        
        self.isKilled = 0
        
        f1 = Func(self.moveTank)
        
        w = Wait(0.01)
        
        self.moveTankSequence = Sequence(w, f1)
        self.moveTankSequence.loop()
        
    def killTank(self):
        self.moveTankSequence.finish()
        
        if self.isExploding == 1:
            return 0
        
        self.isExploding = 1
        
        self.model.setTransparency(TransparencyAttrib.MAlpha)
        
        self.seconds = 1
        self.frame = 0
            
        taskMgr.add(self.animateExplosion,"explosionAnimation")
        
        self.tankDamage += 10
        self.tankDamageText.destroy()
        self.tankDamageText = OnscreenText(text="Damage: "+str(self.tankDamage)+" %", style=1, fg=(1,1,1,1), pos=(self.damageXPos,self.damageYPos), scale = .07)
        self.tankDamageText.setHpr(0, 0, self.tankDamageTextRot)
        
    def animateExplosion(self, task):
        if self.seconds < task.time:
            if self.frame>16:
                if self.seconds >= 1:
                    self.model.delete()
                    self.isKilled = 1
                    self.isExploding = 0
                    
                    return 0
                self.frame=0
            self.model.setTexture(self.texHolder[self.frame],1)
            self.seconds+=.05
            self.frame+=1
            
        return task.cont
    
    def collideWithBullet(self):
        if self.isKilled == 0:
            self.killTank()

    
    def moveTank(self):
        self.oldPos = self.model.getPos() 
        newPos = self.model.getPos() + self.calculateVector()
                  
        self.model.setPos( newPos )
            
    #if angle > 0, it's 'right'
    #if angle < 0, it's 'left'
    def spin( self, angle ):
        self.turn( angle )
        
    def buttonHit( self, force=1 ):
        if self.isExploding == 1:
            return 0
        
        self.shoot( )
        
    def shoot( self ):
        
        #spawn the tank if it's dead
        if self.isKilled == 1:
            self.spawnTank()
            return 0
        
        #otherwise, shoot a bullet
            
        pos = self.model.getPos()
        xDir = cos(radians(self.model.getHpr()[0] - 90))
        yDir = sin(radians(self.model.getHpr()[0] - 90))
        
        colId = self.colName[-1]
        
        #make the bullet start out farther away from the tank
        xPos = pos[0] + (xDir * 3)
        yPos = pos[1] + (yDir * 3)
        
        #assign a new and different identification (bulletId) for the new bullet we create
        #if we assign similiar identifications, then multiple amount of bullets can get the
        #same collision events, and we don't want that to occur.
        newBullet = Bullet(Vec3(xPos, yPos, pos[2]), xDir, yDir, str(self.bulletNum)+str(colId), self.handler)
        #newBullet = Bullet(pos, xDir, yDir, colId, self.handler)
        self.bulletNum += 1
        
        if self.bulletNum == 10:
            self.bulletNum = 0
        
    def turn( self, angle ):
        if self.isKilled == 1 or self.isExploding == 1:
            return 0
        
        #angle = -angle 
        self.model.setHpr( (self.model.getHpr()[0] + angle), 0, 0 )
    
    def calculateVector(self):
        xCoord = cos(radians(self.model.getHpr()[0]-90))
        yCoord = sin(radians(self.model.getHpr()[0]-90))
        return (Vec3( xCoord, yCoord, 0 )/TANK_SPEED_MOD)
    
    def collideWithWall( self, obj ):
        if( obj.getFromNode().getName() == self.colName ):
            self.model.setPos( self.model.getPos() - self.calculateVector() )

    
    