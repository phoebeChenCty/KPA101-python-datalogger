from pylablib.devices.Thorlabs.kinesis import KinesisQuadDetector as controller
import csv
import schedule  # for timing logging
import time
from datetime import date
from pathlib import Path


def write_position():
    position_line = d.get_readings()
    print('msg:', position_line)
    writer = csv.writer(f)
    writer.writerow(position_line)


# CONSTANTS
serial_id = str(69250945)
header_str1 = "xdiff,ydiff,sum,xpos,ypos\n"

# antenna under test for filename
ap = 'data_'
# polling_interval = 500  # polling milliseconds
sampling_interval = 0.1  # interval seconds, how fast the code samples the poll


try:
    #input("Press enter to continue")

    # help(KCubePositionAligner)
    print('Thor_logger: [antenna %s] [file sampling %2.3f s]' % (
        ap, sampling_interval))

    d = controller(str(69250945))

    # pause before recording data
    time.sleep(2)  # ThorLabs have this in their example...

    print(f'Home directory: {Path.home()}')
    print(f'Current directory: {Path.cwd()}')

    # file_time=str(int(time.time()))
    file_time = str(date.today())
    file_name = str('position_'+ap+file_time+'.csv')
    file_path = Path.cwd() / 'output' / file_name
    print('Log file location:', file_path)

    # open the file and write the header
    f = open(file_path, 'w', newline='')
    f.write(header_str1)

    # delcare start time
    start_time = time.time()

    # write the postion
    schedule.every(sampling_interval).seconds.do(write_position)

    while True:
        schedule.run_pending()
        # time.sleep(0.05)

except KeyboardInterrupt:
    print("Did you press break?")
except SyntaxError:
    print('SyntaxError: ', SyntaxError)
finally:
    schedule.clear()  # otherwise you end up with multiple instances of scheduled jobs
    f.close()  # close the file for writing.
    print("This is the end as we know it")
