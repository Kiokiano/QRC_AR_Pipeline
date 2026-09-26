import bpy
import sys

def process_helmet():
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')
    
    # Assuming the helmet is the active object or selecting all
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
    
    # 1. Center Origin to Geometry (Bounding Box Center)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    
    # 2. Height Normalization to 0.28m
    # Get dimensions
    dim = bpy.context.active_object.dimensions
    scale_factor = 0.28 / dim.z
    bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
    
    # 3. Cranial Z-pivot adjustment (0.40 shift)
    # Apply transformation to move origin
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.translate(value=(0, 0, 0.40))
    
    # Export as glb (simplified)
    # bpy.ops.export_scene.gltf(filepath="processed/output.glb")

if __name__ == "__main__":
    process_helmet()
