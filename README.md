# 📁 Simple File Organizer

A simple "drop-and-run" Python script that cleans up the current directory by sorting files into subfolders based on their type (e.g., images, documents, videos).

There are no command-line arguments. Just place it in a folder and run it.

## Example: Before and After

**Your messy folder might look like this:**
```
Downloads/
├── organize.py
├── my_vacation.jpg
├── budget_2023.xlsx
├── final_report.pdf
├── funny_video.mp4
└── project_files.zip
```

**After running the script, it will be neatly organized:**
```
Downloads/
├── organize.py
├── images/
│   └── my_vacation.jpg
├── spreadsheets/
│   └── budget_2023.xlsx
├── documents/
│   └── final_report.pdf
├── video/
│   └── funny_video.mp4
└── archives/
    └── project_files.zip
```

## How to Use

Follow these three simple steps:

1.  **Save the Script:** Save the code below as a Python file named `organize.py`.
2.  **Place the Script:** Put the `organize.py` file into any folder you want to clean up (like your `Downloads` folder).
3.  **Run it:** Open your terminal or command prompt inside that same folder and run the following command:

    ```bash
    python organize.py
    ```

The script will immediately scan the directory and start moving files.

## 🔧 How to Customize the Folders

The script uses a Python dictionary called `FOLDER_MAPPING` to decide where each file goes. You can easily edit this dictionary at the top of the `organize.py` file to add new file types or change the folder names.

For example, to add `.webp` images and `.docx` documents, you would edit the `FOLDER_MAPPING` like this:

```python
FOLDER_MAPPING = {
    "images": ["jpg", "jpeg", "png", "gif", "svg", "heic", "webp"], # <--- Added .webp
    "documents": ["pdf", "doc", "docx", "txt", "rtf", "odt"],      # <--- Added .docx
    # ... rest of the dictionary
}
```

Files with extensions not found in the mapping will be moved to a folder named `other`.

---
