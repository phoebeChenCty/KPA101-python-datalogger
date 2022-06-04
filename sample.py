from pylablib.devices.Thorlabs.kinesis import KinesisQuadDetector as controller

d = controller(str(69250945))
print(d.get_readings())
