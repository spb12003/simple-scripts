import os

def open_files():
    # List of files you want to open. Provide full paths to the files.
    files = [
        "C:\\Users\\shawn\\OneDrive\\Documents\\Writing\\Bonds-Not-SOV.docx",
        "C:\\Users\\shawn\\OneDrive\\Documents\\Bitcoin\\Shawn_Burns_Resume_Nov_2023.docx",
        # ... add as many as you need
    ]

    for file in files:
        os.startfile(file)

if __name__ == "__main__":
    open_files()