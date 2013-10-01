import direct.directbase.DirectStart 
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task 
## from direct.actor import Actor 
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import * 

class World(DirectObject):
    def __init__ (self):
        #Set the camera in a fixed position
        ## base.disableMouse()
        ## base.camera.setPosHpr(-0.785, -142.458, 83.247, 0, -30.29, 0)
        ## base.camLens.setFar(10000)
        base.setBackgroundColor( .5, .5, .5 )
        self.accept( "space", self.findCam )  # comment out later
        
        #Load the environment model 
        self.environ = loader.loadModel("models/maze.egg") 
        self.environ.reparentTo(render)
        self.environ.setScale(0.1) 
        ## self.environ.hide() # comment out later
        
        #Lighting
        self.directionalLight = DirectionalLight( "directionalLight" )
        self.directionalLight.setColor( Vec4( .9, .6, .6, 1 ) )
        self.directionalLight.setDirection( Vec3( -30, 10, -10 ) )
        self.dl2 = DirectionalLight( "directionalLight" )
        self.dl2.setColor(Vec4(.5, .5,.8,1))
        self.dl2.setDirection(Vec3 (3,-2,-1))
        
        render.setLight(NodePath(self.dl2))
        render.setLight(NodePath(self.directionalLight))
        
        # assign keyboard events
        
        self.accept( "t", self.teststuff, [  1 ] ) 
        self.accept( "y", self.teststuff, [ -1 ] ) 
        self.accept( "u", self.teststuff2, [  1 ] ) 
        self.accept( "i", self.teststuff2, [ -1 ] ) 
        self.accept( "o", self.teststuff3, [  1 ] ) 
        self.accept( "p", self.teststuff3, [ -1 ] ) 
        self.accept( "k", self.teststuff4, [  Vec3(1,0,0) ] ) 
        self.accept( "l", self.teststuff4, [ Vec3(-1,0,0) ] )
        
################################################################

    def findCam(self):
        
        print 'camera: ', camera.getPos(), camera.getHpr() 
       
################################################################
    def teststuff(self, value):
        self.directionalLight.setX(self.directionalLight.getX() + value)
        print self.directionalLight.getX()
        ## print 'in test stuff'
    def teststuff2(self, value):
        self.directionalLight.setY(self.directionalLight.getY() + value)
        print self.directionalLight.getY()
        ## print 'in test stuff2'
    def teststuff3(self, value):
        self.directionalLight.setZ(self.directionalLight.getZ() + value)
        print self.directionalLight.getZ()
        ## print 'in test stuff2'
    def teststuff4(self, value):
        self.dl2.setDirection(self.dl2.getDirection() + value)
        print self.dl2.getDirection()
        ## print 'in test stuff2'
################################################################

       
w = World()
run()
