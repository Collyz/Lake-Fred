from scipy.spatial import Delaunay, delaunay_plot_2d
import numpy as np

class Lake_Delaunay:

    
    def __init__(self):
        self.verts = []
        self.faces = []
        self.edges = []
        self.all_points = []
        self.surface_points = [] #points with z = 0
        self.depth_points = [] #points with z != 0
        
    
    def load_data(self, file_path, delim, skip_lines):
        # Loading the data from the CSV file into np array
        data = np.genfromtxt(file_path, delimiter=delim, skip_header=skip_lines)
        # Retrieve x, y, and z values (-z value since z is depth)
        x_values, y_values, z_values = data[:, 0], data[:, 1], -data[:, 2]
        # Create a 3D array containing x, y, and z coordinates
        self.all_points = np.column_stack((x_values, y_values, z_values))
        
        
    def delaunay_2d(self):
        # Scipy implementation of 2D Delaunay Triangulation using
        triangulation = Delaunay(self.all_points[0:, :2])
        tri = triangulation.simplices
        self.faces = [list(face) for face in tri]
        
    
    def separate_values(self):
        # Separate surface and depth points
        self.surface_points = all_points[all_points[:, 2] == 0]
        self.depth_points = all_points[all_points[:, 2] != 0]
        
        
    def create_mesh(self):
        # Creating the mesh
        if(len(self.faces) != 0):
            mesh_data = bpy.data.meshes.new("delaunay_data")
            mesh_data.from_pydata(self.all_points, self.edges, self.faces)
            mesh_obj = bpy.data.objects.new("delaunay_obj", mesh_data)
            bpy.context.collection.objects.link(mesh_obj)
            print("Success")
        else:
            print("Faces Empty")


if __name__ == "__main__":
    delaunay = Lake_Delaunay()
    delaunay.load_data("C:\\Users\\mmowl\\Desktop\\Lake Fred\\Lake Scripts\\Delaunay\\Lake_Fred_CSV_2.csv", ',', 1)
    delaunay.delaunay_2d()
