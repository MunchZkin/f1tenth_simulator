from Adafruit_MotorHAT import Adafruit_MotorHAT

def set_speed(motor_ID, value):
	max_pwm = 115.0
	speed = int(min(max(abs(value * max_pwm), 0), max_pwm))

	if motor_ID == 1:
		motor = motor_left
	elif motor_ID == 2:
		motor = motor_right
	else:
		rospy.logerror('set_speed(%d, %f) -> invalid motor_ID=%d', motor_ID, value, motor_ID)
		return
	
	motor.setSpeed(speed)

	if value > 0:
		motor.run(Adafruit_MotorHAT.FORWARD)
	else:
		motor.run(Adafruit_MotorHAT.BACKWARD)

def all_stop():
	motor_left.setSpeed(0)
	motor_right_setSpeed(0)

	motor_left.run(Adafruit_MotorHAT.RELEASE)
	motor_right.run(Adafruit_MotroHat.RELEASE)


	def speed_cmd_callback(msg):
		set_speed(motor_left_ID , msg.data[0])
		set_speed(motor_right_ID , msg.data[1])

if __name__ == "__main__":

	motor_driver = Adafruit_MotorHAT(i2c_bus = 1)

	motor_left_ID = 1
	motor_right_ID = 2

	motor_left = motor_driver.getMotor(motor_left_ID)
	motor_right = motor_driver.getMotor(motor_right_ID)

	all_stop()

	rospy.init_node('jetbot_motors')
	motor_speed_topic = rospy.get_param("motor_speed_topic")

	rospy.Subscriber(motor_speed_topic, Float64MultiArray ,speed_cmd_callback)

	rospy.spin()