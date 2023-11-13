from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
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
        delaunay_plot_2d(triangulation)
        plt.title("Delaunay Triangulation on Lake Fred Points")
        plt.show()
        
    
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
    delaunay.load_data("C:\\Users\\mmowl\\Desktop\\Lake Fred\\Lake-Fred\\Experimenting With 2D_Delaunay\\lake_data_processed.txt", ',', 1)
    delaunay.delaunay_2d()
    plt.plot(delaunay.faces)
    plt.show()
    # Generate random points for demonstration
    

    # def delaunay_plot_2d_custom(ax, tri):
    #     ax.triplot(tri.points[:, 0], tri.points[:, 1], tri.simplices, 'b-')

    # def voronoi_plot_2d_custom(ax, vor):
    #     voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2, line_alpha=0.6, point_size=2)

    # # Generate random points for demonstration
    # rng = np.random.default_rng()
    # points = rng.random((50, 2))

    # # Perform Delaunay triangulation
    # tri = Delaunay(points)

    # # Create a single subplot
    # fig, ax = plt.subplots()

    # # Plot Delaunay triangulation
    # delaunay_plot_2d_custom(ax, tri)

    # # Overlay Voronoi diagram on the same subplot
    # vor = Voronoi(points)
    # voronoi_plot_2d_custom(ax, vor)

    # plt.title("Delaunay Triangulation and Voronoi Diagram")
    # plt.show()
