from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, AmbientLight
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the cube model
        self.cube = self.loader.loadModel("models/box")
        self.cube.reparentTo(self.render)
        self.cube.setScale(0.5, 0.5, 0.5)
        self.cube.setPos(0, 0, 0)

        # Add a point light to the scene
        self.point_light = PointLight('point_light')
        self.point_light.setColor((1, 1, 1, 1))
        self.point_light_node = self.render.attachNewNode(self.point_light)
        self.point_light_node.setPos(5, -5, 7)
        self.render.setLight(self.point_light_node)

        # Add ambient light to the scene
        self.ambient_light = AmbientLight('ambient_light')
        self.ambient_light.setColor((0.2, 0.2, 0.2, 1))
        self.ambient_light_node = self.render.attachNewNode(self.ambient_light)
        self.render.setLight(self.ambient_light_node)

        # Rotate the cube
        self.taskMgr.add(self.rotateCube, "rotateCubeTask")

    def rotateCube(self, task):
        angle_degrees = task.time * 20.0
        angle_radians = angle_degrees * (3.14159 / 180.0)
        self.cube.setHpr(angle_degrees, angle_degrees, angle_degrees)
        return Task.cont

app = MyApp()
app.run()
