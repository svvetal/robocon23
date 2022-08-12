'''
                              |-------|                            
                              |       |                        
                              |   M1  |
                              |       |                               
                              |-------|
                                /  \
                               /    \
                              /      \
                             /        \
                            /          \
                           /            \
                          /              \
                         /                \
                        /                  \
                       /                    \
                      /                      \
                     /                        \
          |-------| /                          \  |-------|
          |       |/                            \ |       |
          |   M2  |-------------------------------|   M3  |
          |       |                               |       |
          |-------|                               |-------|
'''
#PS4 controller Library
from pyPS4Controller.controller import Controller

#Raspi GPIO Library
import RPi.GPIO as GPIO
from time import sleep

loco_dir1_pin = 14
loco_dir2_pin = 15  
loco_dir3_pin = 18
loco_pwm1_pin = 23
loco_pwm2_pin = 24
loco_pwm3_pin = 25


left_x = 0
left_y = 0
right_x = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(loco_dir1_pin, GPIO.OUT)
GPIO.setup(loco_pwm1_pin, GPIO.OUT)
GPIO.setup(loco_dir2_pin, GPIO.OUT)
GPIO.setup(loco_pwm2_pin, GPIO.OUT)
GPIO.setup(loco_dir3_pin, GPIO.OUT)
GPIO.setup(loco_pwm3_pin, GPIO.OUT)

p=GPIO.PWM(loco_pwm1_pin, 100)
q=GPIO.PWM(loco_pwm2_pin, 100)
r=GPIO.PWM(loco_pwm3_pin, 100)

p.start(0)
q.start(0)
r.start(0)


class MyController(Controller):

  def on_L3_up(self, value):
    final = -0.003875*value
    duty = final*0.787401574803149606
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_L3_up: {}".format(duty))

  def on_L3_down(self, value):
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    final = 0.003875*value
    duty = final*0.787401574803149606
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_L3_down: {}".format(duty))

  def on_L3_left(self, value):
    final = 0.003875*value
    duty = final*0.787401574803149606
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_L3_left: {}".format(duty))

  def on_L3_right(self, value):
    final = 0.003875*value
    duty = final*0.787401574803149606
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_L3_right: {}".format(duty))

  def on_R3_left(self, value):
    final = 0.003875*value
    duty = final*0.787401574803149606
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_R3_left: {}".format(duty))

  def on_R3_right(self, value):
    final = 0.003875*value
    duty = final*0.787401574803149606
    GPIO.output(loco_dir1_pin, GPIO.HIGH)
    GPIO.output(loco_dir2_pin, GPIO.HIGH)
    GPIO.output(loco_dir3_pin, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    q.ChangeDutyCycle(duty)
    r.ChangeDutyCycle(duty)
    print("on_R3_right: {}".format(duty))

MyController(interface="/dev/input/js0").listen()