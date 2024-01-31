import unreal
from PySide6 import QtWidgets as qw
from PySide6.QtCore import Qt
import random as rnd

class spawntool(qw.QWidget):
    
    formWidth = 100

    axeRange = 2500
    scaleRange = 25

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spawn Tool")
        self.draw_ui()    
        self.bind_ui()    

    def draw_ui(self):
        self.init_layout()

        spawn_label = qw.QLabel("ACTOR")
        spawn_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        range_label = qw.QLabel("SPAWN RANGE")
        range_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scale_label = qw.QLabel("SPAWN SCALE")
        scale_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotation_hb = qw.QHBoxLayout()
        rotation_form = qw.QFormLayout()
        rotation_label = qw.QLabel("SPAWN ROTATION")
        self.check_rotation = qw.QCheckBox()
        self.check_rotation.setChecked(True)
        rotation_form.addRow(rotation_label, self.check_rotation)
        rotation_hb.addLayout(rotation_form)
        rotation_hb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #path
        label_path = qw.QLabel("BP Path : ")
        label_path.setFixedWidth(self.formWidth)
        self.text_actor_bp = qw.QLineEdit()
        self.text_actor_bp.setText("/Game/BP_Actor_Test")
        path_layout = qw.QFormLayout()
        path_layout.addRow(label_path, self.text_actor_bp)

        #quantity
        self.label_qty = qw.QLabel("Quantity : X ")
        self.label_qty.setFixedWidth(self.formWidth)
        self.slider_qty = self.ui_create_slider(1, 1000, 25)
        qty_layout = qw.QFormLayout()
        qty_layout.addRow(self.label_qty, self.slider_qty)

        #group
        label_group = qw.QLabel("Group Actors : ")
        label_group.setFixedWidth(self.formWidth)
        self.check_group = qw.QCheckBox()
        group_layout = qw.QFormLayout()
        group_layout.addRow(label_group, self.check_group)

        #range global
        label_range = qw.QLabel("Range on Axes : ")
        label_range.setFixedWidth(self.formWidth)
        self.slider_range_global = self.ui_create_slider(0, self.axeRange, 500)
        gRangeLayout = qw.QFormLayout()
        gRangeLayout.addRow(label_range, self.slider_range_global)

        #range X
        self.label_rangeX = qw.QLabel("Range on X : *")
        self.label_rangeX.setFixedWidth(self.formWidth)
        self.slider_range_x = self.ui_create_slider(0, self.axeRange, 500)
        xRangeLayout = qw.QFormLayout()
        xRangeLayout.addRow(self.label_rangeX, self.slider_range_x)

        #range Y
        self.label_rangeY = qw.QLabel("Range on Y : *")
        self.label_rangeY.setFixedWidth(self.formWidth)
        self.slider_range_y = self.ui_create_slider(0, self.axeRange, 500)
        yRangeLayout = qw.QFormLayout()
        yRangeLayout.addRow(self.label_rangeY, self.slider_range_y)

        #range Z
        self.label_rangeZ = qw.QLabel("Range on Z : *")
        self.label_rangeZ.setFixedWidth(self.formWidth)
        self.slider_range_z = self.ui_create_slider(0, self.axeRange, 500)
        zRangeLayout = qw.QFormLayout()
        zRangeLayout.addRow(self.label_rangeZ, self.slider_range_z)

        #rotation global
        self.label_rotation_global = qw.QLabel("Rotation : ")
        self.label_rotation_global.setFixedWidth(self.formWidth)
        self.slider_rotation_global = self.ui_create_slider(0, 360, 0)
        rotLayout = qw.QFormLayout()
        rotLayout.addRow(self.label_rotation_global, self.slider_rotation_global)

        #rotation yaw
        self.label_rotation_yaw = qw.QLabel("Yaw : *")
        self.label_rotation_yaw.setFixedWidth(self.formWidth)
        self.slider_rotation_yaw = self.ui_create_slider(0, 360, 0)
        yawLayout = qw.QFormLayout()
        yawLayout.addRow(self.label_rotation_yaw, self.slider_rotation_yaw)

        #rotation pitch
        self.label_rotation_pitch = qw.QLabel("Pitch : *")
        self.label_rotation_pitch.setFixedWidth(self.formWidth)
        self.slider_rotation_pitch = self.ui_create_slider(0, 360, 0)
        pitchLayout = qw.QFormLayout()
        pitchLayout.addRow(self.label_rotation_pitch, self.slider_rotation_pitch)

        #rotation roll
        self.label_rotation_roll = qw.QLabel("Roll : *")
        self.label_rotation_roll.setFixedWidth(self.formWidth)
        self.slider_rotation_roll = self.ui_create_slider(0, 360, 0)
        rollLayout = qw.QFormLayout()
        rollLayout.addRow(self.label_rotation_roll, self.slider_rotation_roll)

        self.widget_rotation = qw.QWidget()
        rotation_vb = qw.QVBoxLayout(self.widget_rotation)
        rotation_vb.addLayout(rotLayout)
        rotation_vb.addLayout(yawLayout)
        rotation_vb.addLayout(pitchLayout)
        rotation_vb.addLayout(rollLayout)

        #scale uniform
        label_scale_uniform = qw.QLabel("Uniform : ")
        self.check_scale_uniform = qw.QCheckBox()
        uniformLayout = qw.QFormLayout()
        uniformLayout.addRow(label_scale_uniform, self.check_scale_uniform)

        #scale global
        self.label_scale_global = qw.QLabel("Scale : ")
        self.label_scale_global.setFixedWidth(self.formWidth)
        self.slider_scale_global = self.ui_create_slider(1, self.scaleRange, 1)
        gScaleLayout = qw.QFormLayout()
        gScaleLayout.addRow(self.label_scale_global, self.slider_scale_global)

        #scale x
        self.label_scale_x = qw.QLabel("Scale X : *")
        self.label_scale_x.setFixedWidth(self.formWidth)
        self.slider_scale_x = self.ui_create_slider(1, self.scaleRange, 1)
        xScaleLayout = qw.QFormLayout()
        xScaleLayout.addRow(self.label_scale_x, self.slider_scale_x)
        #scale y
        self.label_scale_y = qw.QLabel("Scale Y : *")
        self.label_scale_y.setFixedWidth(self.formWidth)
        self.slider_scale_y = self.ui_create_slider(1, self.scaleRange, 1)
        yScaleLayout = qw.QFormLayout()
        yScaleLayout.addRow(self.label_scale_y, self.slider_scale_y)
        #scale z
        self.label_scale_z = qw.QLabel("Scale Z : *")
        self.label_scale_z.setFixedWidth(self.formWidth)
        self.slider_scale_z = self.ui_create_slider(1, self.scaleRange, 1)
        zScaleLayout = qw.QFormLayout()
        zScaleLayout.addRow(self.label_scale_z, self.slider_scale_z)

        self.widget_scale = qw.QWidget()
        scale_vb = qw.QVBoxLayout(self.widget_scale)
        scale_vb.addLayout(xScaleLayout)
        scale_vb.addLayout(yScaleLayout)
        scale_vb.addLayout(zScaleLayout)

        self.btn_spawn_actor = qw.QPushButton("Spawn")

        self.layout.addWidget(spawn_label)
        self.layout.addLayout(path_layout)
        self.layout.addLayout(qty_layout)
        self.layout.addLayout(group_layout)
        
        self.layout.addWidget(range_label)
        self.layout.addLayout(gRangeLayout)
        self.layout.addLayout(xRangeLayout)
        self.layout.addLayout(yRangeLayout)
        self.layout.addLayout(zRangeLayout)

        self.layout.addLayout(rotation_hb)
        self.layout.addWidget(self.widget_rotation)

        self.layout.addWidget(scale_label)
        
        self.layout.addLayout(uniformLayout)
        self.layout.addLayout(gScaleLayout)
        self.layout.addWidget(self.widget_scale)

        self.layout.addWidget(self.btn_spawn_actor)

        self.set_qty_label()
        self.set_range_x_label()
        self.set_range_y_label()
        self.set_range_z_label()

        self.set_rotation_yaw_label()
        self.set_rotation_pitch_label()
        self.set_rotation_roll_label()

        self.set_scale_x_label()
        self.set_scale_y_label()
        self.set_scale_z_label()

    def init_layout(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setFixedHeight(600)
        self.setFixedWidth(400)

    def bind_ui(self):
        self.btn_spawn_actor.clicked.connect(self.spawn_actors)
        self.slider_qty.valueChanged.connect(self.set_qty_label)

        self.slider_range_global.valueChanged.connect(self.set_range_global)
        self.slider_range_x.valueChanged.connect(self.set_range_x_label)
        self.slider_range_y.valueChanged.connect(self.set_range_y_label)
        self.slider_range_z.valueChanged.connect(self.set_range_z_label)

        self.check_rotation.stateChanged.connect(self.update_rotation_ui)
        self.slider_rotation_global.valueChanged.connect(self.set_rotation_global)
        self.slider_rotation_yaw.valueChanged.connect(self.set_rotation_yaw_label)
        self.slider_rotation_pitch.valueChanged.connect(self.set_rotation_pitch_label)
        self.slider_rotation_roll.valueChanged.connect(self.set_rotation_roll_label)

        self.check_scale_uniform.stateChanged.connect(self.update_scale_ui)
        self.slider_scale_global.valueChanged.connect(self.set_scale_global)
        self.slider_scale_x.valueChanged.connect(self.set_scale_x_label)
        self.slider_scale_y.valueChanged.connect(self.set_scale_y_label)
        self.slider_scale_z.valueChanged.connect(self.set_scale_z_label)


    def ui_create_slider(self, min: int = 1, max: int = 100, defaultValue: int = 1, orientation: Qt.Orientation = Qt.Horizontal):
        slider = qw.QSlider(orientation)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setValue(defaultValue)
        return slider

    def set_qty_label(self):
        self.label_qty.setText("Quantity : {0} ".format(self.slider_qty.value()))
    
    def set_range_global(self):
        value = self.slider_range_global.value()
        self.slider_range_x.setValue(value)
        self.slider_range_y.setValue(value)
        self.slider_range_z.setValue(value)

    def set_range_x_label(self):
        self.set_range_label(self.label_rangeX, "X", self.slider_range_x.value())
    def set_range_y_label(self):
        self.set_range_label(self.label_rangeY, "Y", self.slider_range_y.value())
    def set_range_z_label(self):
        self.set_range_label(self.label_rangeZ, "Z", self.slider_range_z.value())
    def set_range_label(self, label, axe, value):
        label.setText("Range on {0} : {1} ".format(axe, value))

    def update_rotation_ui(self):
        enable = True if self.check_rotation.checkState() is Qt.CheckState.Checked else False
        self.widget_rotation.setVisible(enable)

    def update_scale_ui(self):
        enable = False if self.check_scale_uniform.checkState() is Qt.CheckState.Checked else True
        self.widget_scale.setVisible(enable)
        self.set_scale_global()

    def set_rotation_global(self):
        value = self.slider_rotation_global.value()
        self.slider_rotation_yaw.setValue(value)
        self.slider_rotation_pitch.setValue(value)
        self.slider_rotation_roll.setValue(value)

    def set_rotation_yaw_label(self):
        self.set_rotation_label(self.label_rotation_yaw, "Yaw", self.slider_rotation_yaw.value())
    def set_rotation_pitch_label(self):
        self.set_rotation_label(self.label_rotation_pitch, "Pitch", self.slider_rotation_pitch.value())
    def set_rotation_roll_label(self):
        self.set_rotation_label(self.label_rotation_roll, "Roll", self.slider_rotation_roll.value())

    def set_rotation_label(self, label, axe, value):
        label.setText("{0} : {1} ".format(axe, value))

    def set_scale_global(self):
        value = self.slider_scale_global.value()
        self.slider_scale_x.setValue(value)
        self.slider_scale_y.setValue(value)
        self.slider_scale_z.setValue(value)
        if self.check_scale_uniform.checkState() is Qt.CheckState.Checked:
            self.set_scale_label(self.label_scale_global, "", value)
        else:
            self.set_scale_label(self.label_scale_global, "", "")

    def set_scale_x_label(self):
        self.set_scale_label(self.label_scale_x, "X", self.slider_scale_x.value())
    def set_scale_y_label(self):
        self.set_scale_label(self.label_scale_y, "Y", self.slider_scale_y.value())
    def set_scale_z_label(self):
        self.set_scale_label(self.label_scale_z, "Z", self.slider_scale_z.value())

    def set_scale_label(self, label, axe, value):
        label.setText("Scale {0} : {1} ".format(axe, value))

    def spawn_actors(self):
        bp_path = self.text_actor_bp.text()
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(bp_path)
        if bp_class:
            self.spawn_actor(bp_class)
        else:
            unreal.log_error("Blueprint Path '{0}' is not valid".format(bp_path))

    def spawn_actor(self, bp_class):
        actors = []
        
        for i in range(0, self.slider_qty.value()):
            x, y, z = self.get_location()
            yaw, pitch, roll = self.get_rotation()
            sx, sy, sz = self.get_scale()
            spawned_actor: unreal.Actor = unreal.EditorLevelLibrary.spawn_actor_from_class(bp_class, unreal.Vector(x, y, z), [yaw, pitch, roll])
            spawned_actor.set_actor_scale3d(unreal.Vector(sx, sy, sz))
            actors.append(spawned_actor)
        
        if self.check_group.checkState() is Qt.CheckState.Checked:
            ref = unreal.ActorGroupingUtils()
            unreal.ActorGroupingUtils.group_actors(ref, actors)

    def get_location(self):
        locRangeX = self.slider_range_x.value()
        locRangeY = self.slider_range_y.value()
        locRangeZ = self.slider_range_z.value()
        locX = rnd.randrange(-locRangeX, locRangeX)
        locY = rnd.randrange(-locRangeY, locRangeY)
        locZ = rnd.randrange(-locRangeZ, locRangeZ)
        return locX, locY, locZ
    
    def get_rotation(self):
        yaw = 0
        pitch = 0
        roll = 0
        if self.check_rotation.checkState() is Qt.CheckState.Checked:
            yRange = self.slider_rotation_yaw.value()
            pRange = self.slider_rotation_pitch.value()
            rRange = self.slider_rotation_roll.value()
            yaw = 0 if yRange == 0 else rnd.randrange(0, yRange)
            pitch = 0 if pRange == 0 else rnd.randrange(0, pRange)
            roll = 0 if rRange == 0 else rnd.randrange(0, rRange)
        return yaw, pitch, roll

    def get_scale(self):
        xRange = self.slider_scale_x.value()
        yRange = self.slider_scale_y.value()
        zRange = self.slider_scale_z.value()
        if self.check_scale_uniform.checkState() is Qt.CheckState.Unchecked:
            x = 1 if xRange == 1 else rnd.randrange(1, xRange)
            y = 1 if yRange == 1 else rnd.randrange(1, yRange)
            z = 1 if zRange == 1 else rnd.randrange(1, zRange)
        else:
            val = rnd.randrange(1, self.slider_scale_global.value())
            return val, val, val
        return x, y, z

    def get_random3(self, min, max):
        x = rnd.randrange(min, max)
        y = rnd.randrange(min, max)
        z = rnd.randrange(min, max)
        return x, y, z

    def get_random_float(self, min, max):
        return rnd.random() * rnd.randrange(min, max)

app = None
if not qw.QApplication.instance():
    app = qw.QApplication()
else:
    app = qw.QApplication.instance()

tool = spawntool()
tool.show()

