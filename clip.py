import sys
from Moniter_battery import MoniterBattery;
class cliclass:
    MoniterBattery().cli_header()
    def cli():
        while(True):
            try:
                command = input("\n BMcli> ").strip().lower()
                if command == "start":
                    MoniterBattery().start()
                elif command == "stop":
                    MoniterBattery().stop()
                elif command == "exit":
                    MoniterBattery().stop()
                    print("Goodbye!")
                    sys.exit()
                elif command == "set":
                    MoniterBattery().set_threshold()
                elif command == "help":
                    MoniterBattery().cli_menu()
            except KeyboardInterrupt:
                print("\n\nExiting...")
                MoniterBattery.stop()
                break