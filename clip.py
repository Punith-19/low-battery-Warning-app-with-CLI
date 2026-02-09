import sys
from Moniter_battery import MoniterBattery;
class cliclass:
    @staticmethod
    
    def cli(moniter):
        moniter.cli_menu()
        while(True):
            try:
                command = input("\n BMcli> ").strip().lower()
                if command == "start":
                    moniter.start()
                elif command == "stop":
                    moniter.stop()
                elif command == "exit":
                    moniter.stop()
                    print("Goodbye!")
                    sys.exit()
                elif command == "set":
                    moniter.set_threshold()
                elif command == "help":
                    moniter.cli_menu()
            except KeyboardInterrupt:
                print("\n\nExiting...")
                moniter.stop()
                break
            except ValueError as e:
                print(f"\n\tInput error: {e}")
                print("\tPlease try again.")
                
            except Exception as e:
                print(f"\n\tUnexpected error: {e}")
                print("\tProgram will continue. Type 'help' for commands.")