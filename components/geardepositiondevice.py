import wpilib
from networktables import NetworkTable

class GearDepositionDevice:

    # create solenoids or double solenoids here as we need them, then
    # initialize them in createObjects in robot.py
    sd = NetworkTable
    gear_push_solenoid = wpilib.Solenoid
    gear_drop_solenoid = wpilib.Solenoid

    def __init__(self):
        pass

    def setup(self):
        """Run just after createObjects.
        Useful if you want to run something after just once after the
        robot code is started, that depends on injected variables"""

    def on_enable(self):
        """Run every time the robot transitions to being enabled"""
        pass

    def on_disable(self):
        """Run every time the robot transitions to being disabled"""
        pass

    def push_gear(self):
        self.gear_push_solenoid.set(True)

    def retract_gear(self):
        self.gear_push_solenoid.set(False)

    def drop_gear(self):
        self.gear_drop_solenoid.set(True)

    def lock_gear(self):
        self.gear_drop_solenoid.set(False)

    def execute(self):
        """Run at the end of every control loop iteration"""
        pass
