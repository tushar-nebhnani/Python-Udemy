import os 
import shutil 
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DEST = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
}

class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return 
        
        filePath = event.src_path()
        ext = os.path.splitext(filePath)[1].lower()

        dest_folder = FILE_DEST.get(ext, 'Others')
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        os.makedirs(full_dest, exist_ok=True)
        move_to = os.path.join(full_dest, os.path.basename(filePath))

        try:
            shutil.move(filePath, move_to)
            # print message 
        except:
            print("Failed to move file.")


if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    oberser = Observer()
    oberser.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    oberser.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        oberser.stop()
        oberser.join()