import os

def disable_hpet():
    os.system("bcdedit /set useplatformclock true") # Run the command to disable HPET
    print("HPET disabled successfully")
    
if __name__ == "__main__":
    disable_hpet()