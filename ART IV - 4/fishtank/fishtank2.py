import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
import sys, os
from direct.showbase.BufferViewer import *
from direct.task import Task
from direct.showbase.DirectObject import *

# Figure out what directory this program is in.
MYDIR=os.path.abspath(sys.path[0])
MYDIR=Filename.fromOsSpecific(MYDIR).getFullpath()

class World(DirectObject):
                         
  def __init__(self):
        
    #Set the camera in a fixed position
    base.disableMouse()
    camera.setPosHpr(160.3, -820, 17.7, 6.5, 8.6, 0.6)
    ## camera.setPosHpr(0, 0, 0, -90, 0, 0)
    base.camLens.setFar(5000)
    base.setBackgroundColor( .5, .5, .5 )
    self.accept( "space", self.findCam ) # use to locate the right starting position

    # This shader's job is to render the model with discrete lighting
    # levels.  The lighting calculations built into the shader assume
    # a single nonattenuating point light.

    tempnode = NodePath(PandaNode("temp node"))
    tempnode.setShader(Shader.load(MYDIR+"/lightingGen.sha"))
    base.cam.node().setInitialState(tempnode.getState())
        
    # This is the object that represents the single "light", as far
    # the shader is concerned.  It's not a real Panda3D LightNode, but
    # the shader doesn't care about that.

    light = render.attachNewNode("light")
    light.setPos(30,-50,0)
                
    # this call puts the light's nodepath into the render state.
    # this enables the shader to access this light by name.
    
    render.setShaderInput("light", light)

    # The "normals buffer" will contain a picture of the model colorized
    # so that the color of the model is a representation of the model's
    # normal at that point.

    normalsBuffer=base.win.makeTextureBuffer("normalsBuffer", 0, 0)
    normalsBuffer.setClearColor(VBase4(0.5,0.5,0.5,1))
    self.normalsBuffer=normalsBuffer
    normalsCamera=base.makeCamera(normalsBuffer, aspectRatio=base.getAspectRatio())
    normalsCamera.node().setScene(render)
    tempnode = NodePath(PandaNode("temp node"))
    tempnode.setShader(Shader.load(MYDIR+"/normalGen.sha"))
    normalsCamera.node().setInitialState(tempnode.getState())

    #what we actually do to put edges on screen is apply them as a texture to 
    #a transparent screen-fitted card
    
    drawnScene=normalsBuffer.getTextureCard()
    drawnScene.setTransparency(1)
    drawnScene.setColor(1,1,1,0)
    drawnScene.reparentTo(render2d)
    self.drawnScene = drawnScene

    # this shader accepts, as input, the picture from the normals buffer.
    # it compares each adjacent pixel, looking for discontinuities.
    # wherever a discontinuity exists, it emits black ink.
                
    self.separation = 0.001 * 1.111
    self.cutoff = 0.3 * 0.8
    inkGen=Shader.load(MYDIR+"/inkGen.sha")
    drawnScene.setShader(inkGen)
    drawnScene.setShaderInput("separation", Vec4(self.separation,0,self.separation,0));
    drawnScene.setShaderInput("cutoff", Vec4(self.cutoff,self.cutoff,self.cutoff,self.cutoff));
        
    # Panda contains a built-in viewer that lets you view the results of
    # your render-to-texture operations.  This code configures the viewer.

    self.accept("v", base.bufferViewer.toggleEnable)
    self.accept("V", base.bufferViewer.toggleEnable)
    base.bufferViewer.setPosition("llcorner")
    
    
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

if (base.win.getGsg().getSupportsBasicShaders()):
    w = World()
else:
    print "Toon Shader: Video driver reports that shaders are not supported."

run()