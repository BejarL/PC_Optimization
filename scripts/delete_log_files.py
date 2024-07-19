import os

def delete_log_files():
    """
    Deletes all .log files from specified directories.
    """
    log_dirs = [
        os.path.expanduser("~\\AppData\\Local\\Temp"),  # Path to temporary files
        os.path.expanduser("~\\AppData\\Local\\Logs"),  # Path to log files
    ]
    for log_dir in log_dirs:
        if os.path.exists(log_dir):  # Check if the directory exists
            for root, dirs, files in os.walk(log_dir):  # Traverse directory tree
                for file in files:
                    if file.endswith('.log'):  # Check if the file is a log file
                        try:
                            os.remove(os.path.join(root, file))  # Delete the log file
                        except Exception as e:
                            print(f"Error deleting log file: {file} - {e}")  # Print error if deletion fails
    print("Log files deleted successfully")