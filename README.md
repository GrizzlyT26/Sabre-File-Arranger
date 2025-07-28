Latest Batch File Copier
This Python script automates the task of locating and copying the most recently modified batch archive file from a network directory. It ensures the file is renamed with a timestamp for easier tracking and avoids overwriting files.

Description
The script searches a given source directory (Y:\Sabre\Archive) for files matching a specific naming pattern:
BID_BATCH_EXTRACT_*.zip.gpg
Once the latest file is identified, it is:
- Copied to the destination directory: Y:\Sabre\MostRecentArchiveCopy
- Renamed to include its last modified timestamp for traceability
  
How It Works
1. Scan for Files: Searches for all .zip.gpg files starting with BID_BATCH_EXTRACT_
2. Identify Latest File: Sorts by last modified time
3. Rename Format: OriginalName_YYYYMMDD_HHMMSS.zip.gpg
4. Copy to Destination: Preserves file metadata while renaming
Configuration
Edit these constants in the script as needed:

SOURCE_DIR = Path(r"Y:\Sabre\Archive")
DEST_DIR = Path(r"Y:\Sabre\MostRecentArchiveCopy")
FILENAME_PREFIX = "BID_BATCH_EXTRACT_"
EXTENSION = ".zip.gpg"
How to Use
1. Ensure Python 3.6+ is installed.
2. Save the script as copy_latest_batch.py
3. Run the script:
   python copy_latest_batch.py
Example Output
Original File:
BID_BATCH_EXTRACT_20250728.zip.gpg

Renamed Output:
BID_BATCH_EXTRACT_20250728_134522.zip.gpg
Requirements
No external libraries needed — uses Python standard library:
- shutil
- pathlib
- datetime
Contact
For support or suggestions, contact the script maintainer.
Automate file tracking with accuracy and ease! ⏱️📂

