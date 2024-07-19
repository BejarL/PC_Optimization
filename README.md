# PC Optimization Tool

## Overview
The PC Optimization Tool is a simple GUI application designed to help users clean up and optimize their PC by performing tasks like deleting temporary files, deleting log files, and clearing the DNS cache.

## Features
- **Delete Temporary Files**: Removes temporary files from the system's TEMP directory.
- **Delete Log Files**: Deletes log files from specified directories.
- **Clear DNS Cache**: Clears the DNS cache to help resolve network-related issues.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installation)
- Pillow (for image handling)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pc-optimization-tool.git
    cd pc-optimization-tool
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Place your icon images in the `icons` directory.

## Usage
Run the application:
```bash
python pc_optimization.py