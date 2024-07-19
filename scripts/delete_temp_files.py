import os
import shutil

def delete_temp_files():
    """
    Deletes all temporary files from the system's TEMP directory.
    """
    temp_path = os.getenv('TEMP')  # Get the path of the temporary files directory
    if temp_path:
        for root, dirs, files in os.walk(temp_path):  # Traverse the directory tree
            for file in files:
                try:
                    os.remove(os.path.join(root, file))  # Delete each file
                except Exception as e:
                    print(f"Error deleting file '{file}': {e}")  # Print error if deletion fails
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))  # Recursively delete each directory
                except Exception as e:
                    print(f"Error deleting directory '{dir}': {e}")  # Print error if deletion fails
    print("Temporary files deleted successfully")