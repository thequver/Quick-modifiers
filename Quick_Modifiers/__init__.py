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
from Quick_Modifiers.Quick_Modifiers import *

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
