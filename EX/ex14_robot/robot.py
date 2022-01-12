"""Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    for i in range(15):
        print(robot.get_position())
        robot.set_wheels_speed(20)
        robot.sleep(1)
        robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while not robot.get_line_sensors():
        robot.set_wheels_speed(5)
    if robot.get_line_sensors():
        robot.set_wheels_speed(0)
        for i in range(6):
            robot.set_wheels_speed(5)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    for i in range(15):
        print(robot.get_position())
        robot.set_wheels_speed(20)
        robot.sleep(1)
        robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    robot = FollowerBot(track_image='track.png', start_x=450, start_y=200)
    drive_to_line(robot)
