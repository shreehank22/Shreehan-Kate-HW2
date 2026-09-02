import rclpy 
from rclpy.node import Node
from grasp_matrix_interface.srv import GraspMatrix
import numpy as np

class GraspMatrixServer(Node):
    def __init__(self):
        super().__init__('grasp_matrix_server')
        self.srv = self.create_service(GraspMatrix,'grasp_matrix',self.grasp_matrix_callback)
    def grasp_matrix_callback(self,request,response):
        N = len(request.px)
        rows = 3
        columns = 3*N
        grasp_matrix = 0.0*np.ones((rows,columns))
        for i in range(N):
            nx_i = request.nx[i]
            ny_i = request.ny[i]
            px_i = request.px[i]
            py_i = request.py[i]
            tx_i = -ny_i
            ty_i = nx_i
            moment_n = px_i*ny_i - py_i*nx_i
            moment_t = px_i*ty_i - py_i*tx_i
            grasp_matrix[0,3*i] = nx_i
            grasp_matrix[1,3*i] = ny_i
            grasp_matrix[2,3*i] = moment_n

            grasp_matrix[0,3*i+1] = tx_i
            grasp_matrix[1,3*i+1] = ty_i
            grasp_matrix[2,3*i+1] = moment_t

            grasp_matrix[0,3*i+2] = 0
            grasp_matrix[1,3*i+2] = 0
            grasp_matrix[2,3*i+2] = 1


        response.grasp_matrix = grasp_matrix.flatten().tolist()
        response.rows = rows
        response.columns = columns
        return response

def main(args=None):
    rclpy.init(args=args)
    GraspMatrixSolver = GraspMatrixServer()
    print("Grasp Matrix Server is running...")
    rclpy.spin(GraspMatrixSolver)
    GraspMatrixSolver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()