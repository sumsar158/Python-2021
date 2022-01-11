"""Robot."""
from FollowerBot import FollowerBot


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    for i in range(15):
        print(robot.get_position())
        robot.set_wheels_speed(30)
        robot.sleep(1)


if __name__ == '__main__':
    robot = FollowerBot(track_image='line.png', start_x=242, start_y=346)
    follow_the_line(robot)
