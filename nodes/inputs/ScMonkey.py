import bpy

from bpy.props import FloatProperty, BoolProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_input import ScInputNode

class ScMonkey(Node, ScInputNode):
    bl_idname = "ScMonkey"
    bl_label = "Monkey (Suzanne)"

    in_uv: BoolProperty(default=True, update=ScNode.update_value)
    in_size: FloatProperty(default=2.0, min=0.0, update=ScNode.update_value)
    

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketBool", "Generate UVs").init("in_uv")
        self.inputs.new("ScNodeSocketNumber", "Size").init("in_size", True)
        
    
    def error_condition(self):
        return (
            super().error_condition()
            or self.inputs["Size"].default_value <= 0
        )
    
    def functionality(self):
        if (self.inputs["World Origin"].default_value):
            bpy.ops.mesh.primitive_monkey_add(
                size = self.inputs["Size"].default_value,
                calc_uvs = self.inputs["Generate UVs"].default_value,
                align='WORLD',
                location=(0.0, 0.0, 0.0),
                rotation=(0.0, 0.0, 0.0)
            )
        else:
            bpy.ops.mesh.primitive_monkey_add(
                size = self.inputs["Size"].default_value,
                calc_uvs = self.inputs["Generate UVs"].default_value
            )