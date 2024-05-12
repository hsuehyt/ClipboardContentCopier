import pyperclip

def copy_text_to_clipboard(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            pyperclip.copy(content)
            print("Content copied to clipboard successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace the path below with the path to your file
file_path = r"C:\Users\user\Desktop\Password.txt"
copy_text_to_clipboard(file_path)

