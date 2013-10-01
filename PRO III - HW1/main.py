import direct.directbase.DirectStart 
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task 
## from direct.actor import Actor 
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import * 
import picker 
from random import randint
from direct.gui.OnscreenText import *

class World(DirectObject):
    def __init__ (self):
        
        self.title = OnscreenText(text="Project 1: WackACreature",
                                  style=1, fg=(1,1,1,1), pos=(0,.95), scale = .07)
        
        #  Variables
        self.holes = [0] * 9
        self.jumpHeight=20
        self.moveTime=2
        self.nextPop=2
        self.oneCount=0.0
        self.tenCount=0.0
        
        #Set the camera in a fixed position
        base.disableMouse()
        base.camera.setPosHpr(-0.785, -180.458, 120.247, 0, -30.29, 0)
        base.camLens.setFar(10000)
        base.setBackgroundColor( .1, .1, .1 )
        self.accept( "space", self.findCam )  # comment out later
        
        self.DirectionalLight = DirectionalLight("DirectionalLight")
        self.DirectionalLight.setColor( Vec4(.7,.7,.7,1) )
        self.DirectionalLight.setDirection( Vec3(-48.6484, 0.262534, -30.0068) )
        
        #Load the counter models there 
        self.oneSpin = Actor("models/spinner_model.egg")
        self.oneSpin.loadAnims({"spin": "models/spinner_ani.egg"})
        self.oneSpin.reparentTo(render)
        self.oneSpin.setScale(.2)
        self.oneSpin.setPosHpr(3,90,25,-3,-10,0)
        #theactor.pose("name_of_animation",frame)
        self.oneSpin.pose("spin",self.oneCount)
        
        self.tenSpin = Actor("models/spinner_model.egg")
        self.tenSpin.loadAnims({"spin": "models/spinner_ani.egg"})
        self.tenSpin.reparentTo(render)
        self.tenSpin.setScale(.2)
        self.tenSpin.setPosHpr(-3,90,25,-3,-10,0)
        
        #Load the environment model 
        self.environ = Actor("models/enviro.egg") 
        self.environ.reparentTo(render)
        self.environ.setScale(.2)
        
        #Load the score title model
        self.score = Actor("models/score.egg")
        self.score.reparentTo(render)
        self.score.setScale(.1)
        self.score.setPosHpr(0,110,30,0,45,0)
        
        #Load the Sounds 
        self.popSound=base.loadSfx("sound/pop.mp3")
        self.popSound.setVolume(.9)
        self.popSound.setLoopCount(1)
        
        self.thudSound=base.loadSfx("sound/thud2.mp3")
        self.thudSound.setVolume(.9)
        self.thudSound.setLoopCount(1)
        
        # Load and master a creature (Actor)
        self.creature = Actor("models/creature.egg")
        self.creature.loadAnims({"pop": "models/creature_ani.egg"})
        self.creature.setScale(.3)
        self.creature.setPosHpr(0,0,0,90,0,0)
        self.creature.reparentTo(render)
        
        
         #########################
        #Don't touch section
        
        for i in range(9):
            self.holes[i] = self.environ.controlJoint(None, 'modelRoot', 'Bone0' + str(i+1))
            print self.holes[i].getPos(render)
            
       
        #End don't touch section
        #########################
        
        
        
        #put the creature into a hole
        self.chooseAHole()
        
        #Lighting
        # Using the first light create and design more interesting lighting
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .9, .6, .6, 1 ) )
        self.directionalLight.setDirection( Vec3( 30, 30, -10 ) )
    
        #Apply the Lights
        render.setLight(NodePath(self.directionalLight))
        self.oneSpin.setLight(NodePath(self.directionalLight))
        
        #Setup collisions
        
        #############################
        #Don't touch section
        
        # setup the picker for mouse clicks on objects
        self.pick = picker.Picker()
        # assign the creature as an object that can be picked by the mouse
        self.pick.makePickable(self.creature)
        # define an event handler for when buttons are picked
        self.accept("objectPicked", self.somethingPicked )
        
        #End don't touch section
        #############################
        
    
        # assign keyboard events for debugging
        
        self.accept( "q", self.popUp )  # for testing the popUp
        self.accept( "w", self.chooseAHole )  # for testing the random hole
        
        #Start a task to move the creature around
        taskMgr.add(self.creatureTasks,"creatureTasks")
        
        
        
        
################################################################

    def creatureTasks(self,task):
        #Use this task for anything that needs to be done every frame
        #I used it to check for creature pops.
        if (task.time > self.moveTime):
            self.chooseAHole()
            self.popUp()
            self.moveTime=self.moveTime+randint(1,3)
        return Task.cont
    
    def popUp (self):
        #the pop up command
        self.popSound.play()
        w=Wait(.4)
        
        oldPos=self.creature.getPos()
        newPos=oldPos+Point3(0,0,35)
        
        u = LerpPosInterval(self.creature,.2,newPos,oldPos)
        d = LerpPosInterval(self.creature,.2,oldPos,newPos)
       
        s=Sequence(u,w,d)
        s.start()
        
    def chooseAHole(self):
        #DONT TOUCH
        self.creature.setPos(self.holes[randint(0,8)].getPos(render))

    def somethingPicked(self):
        #This is the method that will be called when something is clicked on
        hit = self.pick.getPickedObj()
        print hit
        #if we hit the creature
        #note this str(hit) should be equal to whatever is printed out by hit
        if (str(hit) == 'render/dmrivers_creature2'):
            
            self.thudSound.play()
            print 'got him'
            #Also increase the hit count, play the hit animation
            self.oneCount=self.oneCount+1
            self.oneSpin.pose("spin",self.oneCount)
       
        if(self.oneCount == 10):
                self.oneCount=0
                self.tenCount=self.tenCount+1
                self.oneSpin.pose("spin",self.oneCount)
                self.tenSpin.pose("spin",self.tenCount)
        
                
    def findCam(self):
        #Debug method
        print 'camera: ', camera.getPos(), camera.getHpr() 
       
w = World()
run()
