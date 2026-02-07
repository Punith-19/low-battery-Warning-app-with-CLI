import time
import psutil
import threading
class MoniterBattery:
    def __init__(self):
        self.running = False
        self.thread = None
        self.threshold = 30

    def Battery_check_loop(self):
        # Intervel to read percentage
        sleep_time = 50
        
        while self.running:
            curr_bstter_percent = psutil.sensors_battery().percent
            plugged_in = psutil.sensors_battery().power_plugged
            if(curr_bstter_percent<=self.threshold and not plugged_in):
                print("warning battery low plugin")
            time.sleep(sleep_time)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target = self.Battery_check_loop)
        self.thread.daemon = True
        self.thread.start()
        print("\tMonitoring Started!!")

    def stop(self):
        self.running = False
        print("\tMonitoring Stopped")

    def get_status(self):
        if self.running:
            return "Running" 
        else: return "Stopped"

    def cli_header(self):
        ## display header in cli
        print("\n" + "="*50)
        print("        BATTERY ALERT MONITOR")
        print("="*50)
        print(f"Status: {self.get_status()}")
        print(f"Current threshold: {self.threshold}%")
        print("="*50)

    def set_threshold(self):
        print("\tenter a new threshold value in '%' from 1 to 100")
        self.threshold = int(input())
        print(f"\tthreshold changed to {self.threshold}")

    def cli_menu(self):
        print("use:\n 'start' to start monitoring\n 'stop' to stop monitoring\n 'set' to set a new threshold\n 'exit' to terminate program")