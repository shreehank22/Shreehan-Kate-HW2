import rclpy
from rclpy.node import Node
from grasp_matrix_interface.srv import GraspMatrix
import numpy as np



class GraspMatrixClient(Node):
    def __init__(self):
        super().__init__('grasp_matrix_client')
        self.cli = self.create_client(GraspMatrix, 'grasp_matrix')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GraspMatrix.Request()
        self.req.px = [-0.06, 0.03536, 0.06304]
        self.req.py = [0.0, 0.03536, -0.04925]
        self.req.nx = [1.0, -0.7071, -0.7880]
        self.req.ny = [0.0, -0.7071, 0.6157]
        print(f'Sending contacts:\npx={self.req.px}\npy={self.req.py}\nnx={self.req.nx}\nny={self.req.ny}')
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    grasp_matrix_client = GraspMatrixClient()
    rclpy.spin_until_future_complete(grasp_matrix_client, grasp_matrix_client.future)
    response = grasp_matrix_client.future.result()
    G = np.array(response.grasp_matrix).reshape(response.rows, response.columns)
    print(f'Grasp matrix G ({response.rows}x{response.columns}):')
    print(G)
    grasp_matrix_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()