bl_info = {
    "name": "Quick Modifiers",
    "author": "Quver",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "Properties > Modifiers",
    "description": "Quickly add bevel, subsurf and weighted normal modifiers",
    "category": "Modifiers"
}

import bpy

def add_modifiers(obj):
    bevel_mod = obj.modifiers.new(name='Bevel', type='BEVEL')
    bevel_mod.segments = 2
    bevel_mod.width = 0.01
    bevel_mod.limit_method = 'WEIGHT'

    subsurf_mod = obj.modifiers.new(name='Subdivision', type='SUBSURF')
    subsurf_mod.levels = 1
    subsurf_mod.render_levels = 2

    normal_mod = obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')
    normal_mod.keep_sharp = True

def set_autosmooth(obj, angle):
    obj.data.use_auto_smooth = True
    obj.data.auto_smooth_angle = angle

def add_button(self, context):
    self.layout.operator(QuickModifiers.bl_idname)

class QuickModifiers(bpy.types.Operator):
    bl_idname = "object.quick_modifiers"
    bl_label = "Add bevel and subdivide"
    bl_description = "Add Bevel, Subsurf, Weighted Normal modifiers, turn on autosmooth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj = context.active_object
        add_modifiers(obj)
        set_autosmooth(obj, angle=3.141592)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(QuickModifiers)
    bpy.types.DATA_PT_modifiers.prepend(add_button)
    bpy.types.VIEW3D_MT_object.append(add_button)

def unregister():
    bpy.utils.unregister_class(QuickModifiers)
    bpy.types.DATA_PT_modifiers.remove(add_button)
    bpy.types.VIEW3D_MT_object.remove(add_button)

if __name__ == "__main__":
    register()
