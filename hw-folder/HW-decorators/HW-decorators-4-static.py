# 4

# make some functions inside class independent by using static
import psutil
from datetime import datetime


def make_func_great_again(func):
    def inner_greatness(*args, **kwar):
        result = func(*args, **kwar)
        return result
    return inner_greatness


class CPUMonitor:
    def __init__(self):
        self._times = []
        self._loads = []
        self._temps = []

    # def record(self, seconds):
    #     start_time = datetime.now()
    #     print("Recording started...")
    #     while True:
    #         self._times.append(datetime.now())
    #         cpu_load = self.get_cpu_load()
    #         self._loads.append(cpu_load)
    #         print(f"\rRecording in progress... Current CPU load: {cpu_load}%", end="")
    #         if (self._times[-1] - start_time).total_seconds() > seconds:
    #             print("\nRecording stopped")
    #             break

    def record_v1(self, seconds):
        start_time = datetime.now()
        print("Recording started...")
        while True:
            self._times.append(datetime.now())
            cpu_load = self.get_cpu_load_craft()
            self._loads.append(cpu_load)
            print(f"\rRecording in progress... Current CPU load: {cpu_load}%", end="")
            if (self._times[-1] - start_time).total_seconds() > seconds:
                print("\nRecording stopped")
                break

    def reset(self):
        self._times = []
        self._loads = []
        self._temps = []

    # @staticmethod
    # def get_cpu_load(format_=False):
    #     load_percent = psutil.cpu_percent()
    #     if format_:
    #         load_percent = str(load_percent) + "%"
    #     return load_percent

    @make_func_great_again
    def get_cpu_load_craft(format_=False):
        load_percent = psutil.cpu_percent()
        if format_:
            load_percent = str(load_percent) + "%"
        return load_percent


if __name__ == "__main__":
    monitor = CPUMonitor()
    # monitor.record(3)
    monitor.record_v1(3)
    # print("Built in static:", CPUMonitor.get_cpu_load())
    # print("Built in static:", CPUMonitor().get_cpu_load())
    print("Crafted static:", CPUMonitor.get_cpu_load_craft())
    print("Crafted static:", CPUMonitor().get_cpu_load_craft())
