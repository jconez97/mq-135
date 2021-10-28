from mq import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("NH4: %g ppm, CO: %g ppm, CO2: %g ppm" % (perc["GAS_NH4"], perc["CO"], perc["CO2"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
