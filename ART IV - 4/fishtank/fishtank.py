import direct.directbase.DirectStart
from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
import sys


class World(DirectObject):
                         
  def __init__(self):
        
    #Set the camera in a fixed position
    base.disableMouse()
    camera.setPosHpr(160.3, -820, 17.7, 6.5, 8.6, 0.6)
    ## camera.setPosHpr(0, 0, 0, -90, 0, 0)
    base.camLens.setFar(5000)
    base.setBackgroundColor( .5, .5, .5 )
    self.accept( "space", self.findCam ) # use to locate the right starting position

    
    #Load the environment
    self.enviro = Actor.Actor('models/enviroModel',
                              {'fish' : 'models/enviroAniFish'} )
    self.enviro.reparentTo(render)
    self.enviro.loop('fish')
    
    ## self.fish01 = self.enviro.controlJoint(None, "modelRoot", 'BoneFish01')
    self.fish01 = self.enviro.exposeJoint(None, "modelRoot", 'BoneFish01')
    self.mod01 = loader.loadModel('models/fish01')
    self.mod01.setPosHpr(0,-10,0,0,90,90)
    self.mod01.reparentTo(self.fish01)
        
    self.fish02 = self.enviro.exposeJoint(None, "modelRoot", 'BoneFish02')
    self.mod02 = loader.loadModel('models/fish02')
    self.mod02.setPosHpr(0,0,-10,90,0,0)
    self.mod02.reparentTo(self.fish02)
    
    self.fish03 = self.enviro.exposeJoint(None, "modelRoot", 'BoneFish03')
    self.mod03 = loader.loadModel('models/fish03')
    self.mod03.setPosHpr(0,-10,0,0,90,90)
    self.mod03.reparentTo(self.fish03)



    
  def findCam(self):
       print 'camera: ', base.camera.getPos(), base.camera.getHpr() 

w = World()
run()