import clr  # provided by pythonnet, .NET interface layer
import sys
import time

# this is seriously nasty.  Points for a better way of fixing this!
sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")

# NB the
# ppak addition
clr.AddReference("Thorlabs.MotionControl.KCube.PositionAlignerCLI")
clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
clr.AddReference("System")
clr.AddReference("System.Collections")
from System.Collections.Generic import List  # noqa
from System import Int32, String  # noqa

# ppak addition
# from Thorlabs.MotionControl.KCube.PositionAlignerCLI import PositionAlignerCLI  # noqa
# from System import Decimal  # noqa
from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI  # noqa
from Thorlabs.MotionControl.KCube.PositionAlignerCLI import KCubePositionAligner  # noqa


def list_devices():
    """Return a list of Kinesis serial numbers"""
    DeviceManagerCLI.BuildDeviceList()
    return DeviceManagerCLI.GetDeviceList()


# help(KCubePositionAligner)
li = List[Int32](range(3))
list(li)  # returns []
li.Add(5)
list(li)  # returns [5]
print('li', list(li))
print('list_devices', list(list_devices()))
# foreach (var i in list_devices())
# {
#     Console.WriteLine(i)
# }
serial = String("69250945")
# serial=str(69000001)
kpa101 = KCubePositionAligner.CreateKCubePositionAligner(serial)
kpa101.Connect(serial)

time.sleep(0.5)  # ThorLabs have this in their example...

# kpa101.StartPolling(250);
# kpa101.EnableDevice();

print(kpa101.get_DeviceName())
print(kpa101.get_Status())
print("Closed Number X: %3.5f" % kpa101.GetClosedLoopPosition().X)
print("Closed Number Y: %3.5f" % kpa101.GetClosedLoopPosition().Y)
print("Demand Number X: %3.5f" % kpa101.GetDemandedPosition().X)
print("Demand Number Y: %3.5f" % kpa101.GetDemandedPosition().Y)
print("Difference Number X: %3.5f" % kpa101.get_Status().PositionDifference.X)
print("Difference Number Y: %3.5f" % kpa101.get_Status().PositionDifference.Y)
print("Difference Number X: %3.5f" % kpa101.Status.PositionDifference.X)
print("Difference Number Y: %3.5f" % kpa101.Status.PositionDifference.Y)
# kpa101.Disconnect()
