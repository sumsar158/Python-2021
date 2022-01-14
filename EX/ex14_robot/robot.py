"""Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    for i in range(15):
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
            robot.set_wheels_speed(45)
            robot.sleep(0.5)
            line_detected = True

        robot.set_wheels_speed(11)
        robot.sleep(0.1)

    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    line_found = False
    while not line_found:
        # Drives forward until finds a line.
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        if sum(robot.get_line_sensors()) != 6144:
            line_found = True

    while not sum(robot.get_line_sensors()) == 6144:
        if robot.get_third_line_sensor_from_left() != 0 and robot.get_third_line_sensor_from_right() != 0:
            robot.set_wheels_speed(80)
            robot.sleep(0.01)

        if robot.get_third_line_sensor_from_left() != 0 and robot.get_third_line_sensor_from_right() != 1024:
            robot.set_left_wheel_speed(-10)
            robot.set_right_wheel_speed(15)
            robot.sleep(0.001)

        elif robot.get_third_line_sensor_from_right() != 0 and robot.get_third_line_sensor_from_left() != 1024:
            robot.set_left_wheel_speed(15)
            robot.set_right_wheel_speed(-15)
            robot.sleep(0.001)

        else:
            robot.set_wheels_speed(40)
            robot.sleep(0.01)

    robot.done()


def hop_over_dotted_line(robot):
    for i in range(70):
        robot.set_wheels_speed(100)
        robot.sleep(0.01)


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    line_found = False
    turn_around = False
    first_hop = False

    while not line_found:
        # Drives forward until finds a line.
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        if sum(robot.get_line_sensors()) != 6144:
            line_found = True

    while not sum(robot.get_line_sensors()) == 6144:

        if robot.get_third_line_sensor_from_left() != 0 and robot.get_third_line_sensor_from_right() != 0:
            robot.set_wheels_speed(80)
            robot.sleep(0.01)

        if robot.get_third_line_sensor_from_left() != 0 and robot.get_third_line_sensor_from_right() != 1024:
            robot.set_left_wheel_speed(-10)
            robot.set_right_wheel_speed(15)
            robot.sleep(0.001)

        elif robot.get_third_line_sensor_from_right() != 0 and robot.get_third_line_sensor_from_left() != 1024:
            robot.set_left_wheel_speed(15)
            robot.set_right_wheel_speed(-15)
            robot.sleep(0.001)

        elif robot.get_position() == (236, 228):
            first_hop = True
            # Hop over the gap.
            hop_over_dotted_line(robot)

        else:
            robot.set_wheels_speed(65)
            robot.sleep(0.01)

        if robot.get_position() == (126, 136) and first_hop:
            # Turn around on gray.
            turn_around = True
            robot.set_left_wheel_speed(-100)
            robot.set_right_wheel_speed(100)
            robot.sleep(0.3)

        if robot.get_position() == (294, 228) and turn_around:
            # Hop over on the way back.
            hop_over_dotted_line(robot)

    print("------Line Lost------")
    print(robot.get_line_sensors())
    print(robot.get_position())
    print("------Line Lost------")

    robot.done()


if __name__ == '__main__':
    robot = FollowerBot(track_image='track.png', start_x=265, start_y=310, timeout=180)
    the_true_follower(robot)
