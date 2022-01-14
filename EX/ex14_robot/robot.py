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
    line_detected = False

    while not line_detected:
        if robot.get_right_line_sensor() < 1024 or robot.get_left_line_sensor() < 1024:
            print(robot.get_right_line_sensor(), robot.get_left_line_sensor())
            print(robot.get_position())
            robot.set_wheels_speed(45)
            robot.sleep(0.5)
            print(robot.get_position())

            line_detected = True
        robot.set_wheels_speed(11)
        robot.sleep(0.1)

    robot.done()


def small_turn(robot: FollowerBot):
    """Make a small turn."""
    if robot.get_third_line_sensor_from_left() != 0 and robot.get_third_line_sensor_from_right() == 0:
        robot.set_left_wheel_speed(-5)
        robot.set_right_wheel_speed(10)
    elif robot.get_third_line_sensor_from_left() == 0 and robot.get_third_line_sensor_from_right() != 0:
        robot.set_left_wheel_speed(10)
        robot.set_right_wheel_speed(-5)


def medium_turn(robot: FollowerBot):
    """Make a medium turn."""
    if robot.get_second_line_sensor_from_left() != 0 and robot.get_second_line_sensor_from_right() == 0:
        robot.set_left_wheel_speed(-10)
        robot.set_right_wheel_speed(20)
    elif robot.get_second_line_sensor_from_left() == 0 and robot.get_second_line_sensor_from_right() != 0:
        robot.set_left_wheel_speed(20)
        robot.set_right_wheel_speed(-10)


def big_turn(robot: FollowerBot):
    """Make a big turn."""
    if robot.get_second_line_sensor_from_left() != 0 and robot.get_second_line_sensor_from_right() == 0:
        robot.set_left_wheel_speed(-15)
        robot.set_right_wheel_speed(30)
    elif robot.get_second_line_sensor_from_left() == 0 and robot.get_second_line_sensor_from_right() != 0:
        robot.set_left_wheel_speed(30)
        robot.set_right_wheel_speed(-15)


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    condition = False
    print(robot.get_line_sensors())
    starting_position = robot.get_position()
    robot.set_wheels_speed(100)
    robot.sleep(0.08)

    while not condition:
        print(robot.get_line_sensors())
        print(robot.get_position())

        if robot.get_third_line_sensor_from_left() == 0 or robot.get_third_line_sensor_from_right() == 0:
            small_turn(robot)
            robot.sleep(0.01)

        elif robot.get_second_line_sensor_from_right() == 0 or robot.get_second_line_sensor_from_left() == 0:
            medium_turn(robot)
            robot.sleep(0.01)

        elif robot.get_left_line_sensor() == 0 or robot.get_right_line_sensors() == 0:
            big_turn(robot)
            robot.sleep(0.01)

        if sum(robot.get_line_sensors()) == 6144 and robot.get_position() != 2 * starting_position:

            condition = True

        else:
            robot.set_wheels_speed(50)
        robot.sleep(0.01)

    print(robot.get_line_sensors(), condition)
    print(robot.get_position())
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    robot = FollowerBot(track_image='track.png', start_x=380, start_y=255)
    follow_the_line(robot)
