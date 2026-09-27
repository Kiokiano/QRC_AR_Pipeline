import bpy
import sys
import os

def process_helmet(input_file, output_file):
    # Clear existing scene
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Import GLB
    bpy.ops.import_scene.gltf(filepath=os.path.abspath(input_file))
    
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')
    
    # Select mesh objects
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            
    if not bpy.context.active_object:
        print("No mesh objects found.")
        return

    # 1. Center Origin to Geometry (Bounding Box Center)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    
    # 2. Height Normalization to 0.28m
    dim = bpy.context.active_object.dimensions
    if dim.z > 0:
        scale_factor = 0.28 / dim.z
        bpy.ops.transform.resize(value=(scale_factor, scale_factor, scale_factor))
    
    # 3. Cranial Z-pivot adjustment (0.40 shift)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.transform.translate(value=(0, 0, 0.40))
    
    # 3.5 Report Dimensions
    dim = bpy.context.active_object.dimensions
    print(f"FINAL_DIMENSIONS: {dim.x:.4f}x{dim.y:.4f}x{dim.z:.4f}")
    
    # 4. Export as glb
    bpy.ops.export_scene.gltf(filepath=output_file, export_format='GLB')

if __name__ == "__main__":
    # Get arguments from command line (after '--')
    args = sys.argv[sys.argv.index("--") + 1:]
    if len(args) >= 2:
        process_helmet(args[0], args[1])
