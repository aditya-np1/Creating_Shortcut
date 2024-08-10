import os
import win32com.client

def create_shortcuts(source_folder, destination_folder):
    """Creates shortcuts for all files in the source folder to the destination folder.

    Args:
        source_folder (str): Path to the source folder.
        destination_folder (str): Path to the destination folder.
    """

    shell = win32com.client.Dispatch("WScript.Shell")

    for root, _, files in os.walk(source_folder):
        for file in files:
            source_file = os.path.join(root, file)
            shortcut_path = os.path.join(destination_folder, file + ".lnk")

            # Use long path syntax if necessary
            long_shortcut_path = "\\\\?\\" + shortcut_path

            try:
                shortcut = shell.CreateShortCut(long_shortcut_path)
                shortcut.TargetPath = source_file
                shortcut.save()
            except Exception as e:
                print(f"Error creating shortcut for {source_file}: {e}")

if __name__ == "__main__":
    source_folder = input("Enter source folder path: ")
    destination_folder = input("Enter destination folder path: ")
    create_shortcuts(source_folder, destination_folder)
