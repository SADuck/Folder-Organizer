# This is the simpler "drop and run" version.
import os
import shutil
from pathlib import Path

# --- YOU CAN CUSTOMIZE THIS SECTION ---
FOLDER_MAPPING = {
    "images": ["jpg", "jpeg", "png", "gif", "svg", "heic"],
    "documents": ["pdf", "doc", "docx", "txt", "rtf", "odt"],
    "spreadsheets": ["xls", "xlsx", "csv"],
    "archives": ["zip", "rar", "7z", "tar", "gz"],
    "audio": ["mp3", "wav", "aac"],
    "video": ["mp4", "mov", "avi", "mkv"],
    "code": ["py", "js", "html", "css", "java"],
}
# --- END OF CUSTOMIZATION ---

def organize_files_in_current_directory():
    """
    Scans the current directory and organizes files into subfolders
    based on the FOLDER_MAPPING configuration.
    """
    current_dir = Path.cwd() # This gets the current working directory
    print(f"Scanning files in: {current_dir}")

    for item_path in current_dir.iterdir():
        if item_path.is_dir() or item_path.name == __file__:
            continue

        file_extension = item_path.suffix.lower().replace('.', '')
        destination_folder_name = extension_to_folder.get(file_extension, "other")
        destination_path = current_dir / destination_folder_name
        destination_path.mkdir(exist_ok=True)

        try:
            shutil.move(str(item_path), str(destination_path))
            print(f"Moved: {item_path.name} -> {destination_folder_name}/")
        except Exception as e:
            print(f"Error moving {item_path.name}: {e}")
    
    print("\nOrganization complete!")

if __name__ == "__main__":
    # Create the reverse mapping for faster lookups
    extension_to_folder = {
        ext: folder for folder, exts in FOLDER_MAPPING.items() for ext in exts
    }
    organize_files_in_current_directory()