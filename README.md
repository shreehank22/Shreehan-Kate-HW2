# RBE 4540/595 — Homework 2

**Author:** Shreehan Kate (skate@wpi.edu)

## Contents

- **Part 1** — Grasp matrix derivation (soft-finger contact model), see write-up PDF.
- **Part 2** — ROS 2 service/client pair that computes the grasp matrix from contact
  points and normals.
  - `src/grasp_matrix_interface` — custom `GraspMatrix.srv` interface
  - `src/grasp_matrix_py` — `server` (computes the grasp matrix) and `client`
    (sends the 3 contacts from Part 1, prints the resulting matrix)

## Build

```bash
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Run

Terminal 1:
```bash
source install/setup.bash
ros2 run grasp_matrix_py server
```

Terminal 2:
```bash
source install/setup.bash
ros2 run grasp_matrix_py client
```

The client sends the same 3 contact points/normals used in the Part 1 hand
derivation; the printed 3×9 grasp matrix matches that derivation (see `Result.png`).
