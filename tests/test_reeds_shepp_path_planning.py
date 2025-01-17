import conftest  # Add root path to sys.path
from PathPlanning.ReedsSheppPath import reeds_shepp_path_planning as m
import numpy as np


def check_edge_condition(px, py, pyaw, start_x, start_y, start_yaw, end_x,
                         end_y, end_yaw):
    assert (abs(px[0] - start_x) <= 0.01)
    assert (abs(py[0] - start_y) <= 0.01)
    assert (abs(pyaw[0] - start_yaw) <= 0.01)
    print("x", px[-1], end_x)
    assert (abs(px[-1] - end_x) <= 0.01)
    print("y", py[-1], end_y)
    assert (abs(py[-1] - end_y) <= 0.01)
    print("yaw", pyaw[-1], end_yaw)
    assert (abs(pyaw[-1] - end_yaw) <= 0.01)


def test1():
    m.show_animation = False
    m.main()


def test2():
    N_TEST = 10

    for i in range(N_TEST):
        start_x = (np.random.rand() - 0.5) * 10.0  # [m]
        start_y = (np.random.rand() - 0.5) * 10.0  # [m]
        start_yaw = np.deg2rad((np.random.rand() - 0.5) * 180.0)  # [rad]

        end_x = (np.random.rand() - 0.5) * 10.0  # [m]
        end_y = (np.random.rand() - 0.5) * 10.0  # [m]
        end_yaw = np.deg2rad((np.random.rand() - 0.5) * 180.0)  # [rad]

        curvature = 1.0 / (np.random.rand() * 5.0)

        px, py, pyaw, mode, clen = m.reeds_shepp_path_planning(
            start_x, start_y, start_yaw, end_x, end_y, end_yaw, curvature)

        check_edge_condition(px, py, pyaw, start_x, start_y, start_yaw,
                             end_x, end_y, end_yaw)
