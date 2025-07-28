import shutil
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
SOURCE_DIR = Path(r"Y:\Sabre\Archive")
DEST_DIR = Path(r"Y:\Sabre\MostRecentArchiveCopy")
FILENAME_PREFIX = "BID_BATCH_EXTRACT_"
EXTENSION = ".zip.gpg"

def get_latest_batch_file(source_dir, prefix, extension): # this function retrieves the latest batch file based on the prefix and extension
    files = [f for f in source_dir.glob(f"{prefix}*{extension}") if f.is_file()]
    if not files:
        return None
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files[0]

def build_timestamped_filename(file_path): # this function builds a timestamped filename based on the file's last modified time
    modified_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    timestamp = modified_time.strftime("%Y%m%d_%H%M%S")
    return f"{file_path.stem}_{timestamp}{file_path.suffix}"

def copy_and_rename_file(src_file, dest_dir): # this function copies the file to the destination directory and renames it with a timestamp
    dest_dir.mkdir(parents=True, exist_ok=True)
    new_name = build_timestamped_filename(src_file)
    dest_path = dest_dir / new_name
    shutil.copy2(src_file, dest_path)
    print(f"Copied and renamed to: {dest_path}")
    return dest_path

def main(): # this function orchestrates the process of finding the latest batch file and copying it
    latest_file = get_latest_batch_file(SOURCE_DIR, FILENAME_PREFIX, EXTENSION)
    if not latest_file:
        print("No matching batch files found.")
        return

    print(f"Latest file found: {latest_file.name}")
    copy_and_rename_file(latest_file, DEST_DIR)

if __name__ == "__main__":
    main()
