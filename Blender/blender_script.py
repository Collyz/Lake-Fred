from bpy import data as D, context as C
from scipy.spatial import Delaunay
import numpy as np


class Lake_Delaunay:

    
    def __init__(self):
        self.verts = []
        self.faces = []
        self.edges = []
        self.all_points = []
        self.surface_points = [] #points with z = 0
        self.depth_points = [] #points with z != 0
        
    
    def load_data(self, file_path, delim, skip_lines, scale=1):
        # Loading the data from the CSV file into np array
        data = np.genfromtxt(file_path, delimiter=delim, skip_header=skip_lines)
        # Retrieve x, y, and z values (-z value since z is depth)
        x_values, y_values, z_values = scale*data[:, 0], scale*data[:, 1], scale*data[:, 2]
        # Create a 3D array containing x, y, and z coordinates
        self.all_points = np.column_stack((x_values, y_values, z_values))
        
        
    def delaunay_2d(self):
        # Scipy implementation of 2D Delaunay Triangulation using
        triangulation = Delaunay(self.all_points[0:, :2])
        tri = triangulation.simplices
        self.faces = [list(face) for face in tri]
        
    
    def separate_values(self):
        # Separate surface and depth points
        self.surface_points = self.all_points[self.all_points[:, 2] == 0]
        self.depth_points = self.all_points[self.all_points[:, 2] != 0]
        
        
    def create_mesh(self, data_name, obj_name):
        # Creating the mesh
        if len(self.faces) != 0:
            # Create a new mesh data block
            mesh_data = D.meshes.new(data_name)
            mesh_data.from_pydata(self.all_points, self.edges, self.faces)

            # Create the mesh object and link it to the scene
            mesh_obj = D.objects.new(obj_name, mesh_data)
            C.collection.objects.link(mesh_obj)

            # Update the scene
            C.view_layer.objects.active = mesh_obj
            mesh_obj.select_set(True)

            # Finally, update the mesh to display it
            mesh_data.update()

            return mesh_obj
        else:
            print("Faces Empty")
            
    def extrude(self, obj_name, extr_val, up=True):
        # Find the mesh object by name
        mesh_obj = D.objects[obj_name]

        # Select the mesh
        mesh_obj.select_set(True)

        # Switch to Edit Mode
        bpy.context.view_layer.objects.active = mesh_obj
        bpy.ops.object.mode_set(mode='EDIT')

        if up:
            # Extrude the mesh up
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, extr_val)})
        else:
            # Extrude the mesh down
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, -extr_val)})

        # Switch back to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        mesh_obj.select_set(False)

        
if __name__ == "__main__":
    delaunay = Lake_Delaunay()
    delaunay.load_data("C:\\Users\\mmowl\\Desktop\\Lake Fred\\Lake-Fred\\lake_data_processed.txt", ',', 1, scale=2.5)
    delaunay.delaunay_2d()
    mesh_obj = delaunay.create_mesh('delaunay_data_1', 'delaunay_obj_1')
    mesh_obj = delaunay.create_mesh('delaunay_data_2', 'delaunay_obj_2')

    # Extruding the mesh both up and down
    # extr = 10
    # delaunay.extrude('delaunay_obj_1', extr_val=extr, up=True)  # Extrude up
    # delaunay.extrude('delaunay_obj_2', extr_val=extr*2, up=False)  # Extrude down