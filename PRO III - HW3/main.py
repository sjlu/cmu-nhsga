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
import sys
import JOD
from JOD import SPINNER_RADIUS,DRUMPAD_RADIUS
from tank import Tank
from collisions import *
from math import *

CAM_HEIGHT = 80

class World(DirectObject):
    def __init__(self):
        self.accept("space",self.findCam)
        camera.setPosHpr(0,0,CAM_HEIGHT, 0, -90, 0)
        base.disableMouse()
        
        #collisions
        createTraverser()
        self.cHandler = createHandler("Event")
        
        self.setupJOD()
        base.accept("escape",sys.exit)
        self.doLights()
        base.setBackgroundColor(0,0,0)
        self.makeTanks()
    
        self.arena = Actor("models/arena.egg")
        self.arena.reparentTo(render)
        self.arena.setScale(.02)
        self.arena.setPos(0, 0, 0)
        self.arena.setHpr(45, 0, 0)
        
        #init time
        self.secondsTime = 0
        self.minutesTime = 3
        
        self.titleRot = 0
        
        timeTitleString = str(self.minutesTime) + ":0" + str(self.secondsTime)
        
        self.timeTitle = OnscreenText(text=timeTitleString, style=1, fg=(0,0,1,1), pos=(0,0), scale = 0.1)
        
        f1 = Func(self.updateTime)
        
        w = Wait(1)
        
        self.s = Sequence(w, f1)
        self.s.loop() #time update rotation
        
        f2 = Func(self.updateTimeRot)
        
        w2 = Wait(0.03)
        
        s2 = Sequence(w2, f2)
        s2.loop()
        
    def updateTimeRot(self):
        self.titleRot += 0.5
        
    def updateTime(self):
        self.secondsTime -= 1
        
        if self.secondsTime < 0:
            self.secondsTime = 59
            self.minutesTime -= 1
        
        timeTitleString = str(self.minutesTime) + ":"
        
        if self.secondsTime < 10:
            timeTitleString = timeTitleString + "0"
            
        timeTitleString = timeTitleString + str(self.secondsTime)
        self.timeTitle.destroy()
        self.timeTitle = OnscreenText(text=timeTitleString, style=1, fg=(0,0,1,1), pos=(0,0), scale = 0.1)
        
        if self.minutesTime == 0 and self.secondsTime == 0:
            #insert game ended code here
            self.gameEnd()

    def makeTanks(self):
        self.tanks = [0,0,0,0]
        for y in range (4):
            rot = 0
            
            if y == 0:
                #tank on bottom right
                rot = -135
            elif y == 1:
                #tank on bottom left
                rot = 135
            elif y == 2:
                #tank on top left
                rot = 45
            elif y == 3:
                #tank on top right
                rot = -45
            
            nextTank = Tank(self.cHandler, y, rot)
            self.accept("JOD_SPIN_"+str(y), nextTank.spin)
            self.accept("JOD_HIT_"+str(y), nextTank.buttonHit)
            self.tanks[y]=nextTank
            
    
    def findCam(self):
        #Debug method
        print 'camera: ', camera.getPos(), camera.getHpr() 
        
    def pollJOD(self, task):
        self.jamodrum.poll()
        return Task.cont
    
    def setupJOD(self):
        self.jamodrum = JOD.JamoDrum()
        taskMgr.add(self.pollJOD, "JODPollTask")
        
        self.jamodrum.simulate(6.0)
   
    def doLights(self):
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .8, .7, .7, 1 ) )
        self.directionalLight.setDirection( Vec3( 0, 0, -2 ) )
        self.dl2 = DirectionalLight( "directionalLight" )
        self.dl2.setColor(Vec4(.7, .8,.7,1))
        self.dl2.setDirection(Vec3 (-50,3,2))
        self.dl3= DirectionalLight( "directionalLight" )
        self.dl3.setColor(Vec4(.7,.7,.8,1))
        self.dl3.setDirection(Vec3 (50, -3,-2))
        render.setLight(NodePath(self.directionalLight))
        render.setLight(NodePath(self.dl2))
        render.setLight(NodePath(self.dl3))
    def gameEnd(self):
        winningPlayer = 0
        for x in range(4):
            if( self.tanks[x].tankDamage < self.tanks[winningPlayer].tankDamage ):
                winningPlayer = x
        self.s.finish()
        imageObject = OnscreenImage(image = "models/tank-o-drum.jpg", pos = (0, 0, 0))
        OnscreenText(text="Player " + str(winningPlayer+1) + " is the Winner! "+str(self.tanks[winningPlayer].tankDamage) +"%", style=1, fg=(1,0,0,1), pos=(0,0), scale = .1)
        
        
w=World()
run()