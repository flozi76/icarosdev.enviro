import logging
import time

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

cpu_temps = [get_cpu_temperature()] * 5

while True:
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    #avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))


    logging.info("Cpu temperature: {:05.2f} *C".format(cpu_temp))
    #logging.info("Cpu temperature: {:05.2f} *C".format(avg_cpu_temp))
    time.sleep(0.5)