import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
import sys


class World(DirectObject):
    
  #Macro-like function used to reduce the amount to code needed to create the
  #on screen instructions
  def genLabelText(self, text, i):
    return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)
                       
  def __init__(self):
        
    #Set the camera in a fixed position
    base.disableMouse()
    ## camera.setPosHpr(-50, 0, 20, -90, 0, 0)
    camera.setPosHpr(0, 0, 0, -90, 0, 0)
    base.camLens.setFar(1000)
    base.setBackgroundColor( .5, .5, .5 )
    self.accept( "space", self.findCam ) # use to locate the right starting position

    #Load the camera nodes
    self.camNode = render.attachNewNode( "camNode" )
    ## self.camNode.reparentTo( render )
    self.camNode.setPos(-50, 0, 20 )
    self.camCarrot = self.camNode.attachNewNode( "camCarrot" )
    self.camCarrotB = self.camNode.attachNewNode( "camCarrotB" )
    ## self.camCarrot.reparentTo(self.camNode)
    self.camCarrot.setPos( 10, 0, 0 )
    self.camCarrotB.setPos( -10, 0, 0 )
    camera.reparentTo( self.camNode )
    
    #Setup onscreen text
    self.uakeyEventText = self.genLabelText("[Up Arrow]: Move Camera Forward", 0)
    self.uakeyEventText = self.genLabelText("[Down Arrow]: Move Camera Backward", 1)
    self.dkeyEventText = self.genLabelText("[D]: Rotate Camera to the Right", 2)
    self.akeyEventText = self.genLabelText("[A]: Rotate Camera to the Left", 3)
    self.wkeyEventText = self.genLabelText("[W]: Rotate Camera Up", 4)
    self.akeyEventText = self.genLabelText("[S]: Rotate Camera Down", 5)
    ## self.okeyEventText = self.genLabelText("[O]: Show Objectives Screen", 6)
    ## self.pkeyEventText = self.genLabelText("[P]: Show Flow Graph", 7)
    
    #Load the environment
    self.enviro = loader.loadModel('models/cavemodel')
    self.enviro.reparentTo(render)
    
    #Lighting
    self.directionalLight = DirectionalLight( "directionalLight" )
    self.directionalLight.setColor( Vec4( .9, .6, .6, 1 ) )
    self.directionalLight.setDirection( Vec3( -30, 10, -10 ) )
    self.dl2 = DirectionalLight( "directionalLight" )
    self.dl2.setColor(Vec4(.5, .5,.8,1))
    self.dl2.setDirection(Vec3 (3,-2,-1))
        
    render.setLight(NodePath(self.dl2))
    render.setLight(NodePath(self.directionalLight))
    
    ## #Load the card and textures
    ## self.card = loader.loadModel('models/card')
    ## self.card.reparentTo(render)
    ## self.card.setPos( self.camCarrot.getPos(render) )
    ## self.card.setH(-90)
    ## self.card.setScale(.047, .047, .047)
    ## ## self.card.setColor(0, 0, 0, 1)
    ## self.flowGraphTex = loader.loadTexture("models/flowgraph.png")
    ## self.objectivesTex = loader.loadTexture("models/objectives.png")
    ## self.card.setTexture(self.objectivesTex, 1)
    
    
    #Setup keyboard control for controling the camera
    self.accept( "w", self.rotCamU )
    self.accept( "s", self.rotCamD )
    self.accept( "d", self.rotCamR )
    self.accept( "a", self.rotCamL )
    self.accept( "arrow_up", self.moveCamF )
    self.accept( "arrow_down", self.moveCamB )
    ## self.accept( "o", self.showCardObj )
    ## self.accept( "p", self.showCardFlo )

    
  def rotCamR(self):
    self.camNode.setH(self.camNode.getH() - 5 )
    ## self.card.hide()
    
  def rotCamL(self):
    self.camNode.setH(self.camNode.getH() + 5 )
    ## self.card.hide()
    
  def rotCamU(self):
    self.camNode.setR(self.camNode.getR() - 1 )
    
  def rotCamD(self):
    self.camNode.setR(self.camNode.getR() + 1 )
    
  def moveCamF(self):
    self.camNode.setPos( self.camCarrot.getPos(render) )
    ## self.card.hide()
    
  def moveCamB(self):
    self.camNode.setPos( self.camCarrotB.getPos(render) )
    ## self.card.hide()
    
  ## def showCardObj(self):
    ## self.card.setPos( self.camCarrot.getPos(render) )
    ## self.card.setH( self.camNode.getH() - 90 )
    ## self.card.setTexture(self.objectivesTex, 1)
    ## self.card.show()
    
  ## def showCardFlo(self):
    ## self.card.setPos( self.camCarrot.getPos(render) )
    ## self.card.setH( self.camNode.getH() - 90 )
    ## self.card.setTexture(self.flowGraphTex, 1)
    ## self.card.show()
    
  def findCam(self):
       print 'camera: ', base.camera.getPos(), base.camera.getHpr() 
       print 'camNode: ', self.camNode.getPos(), self.camNode.getHpr() 
       print 'camCarrot: ', self.camCarrot.getPos(), self.camCarrot.getHpr()

w = World()
run()