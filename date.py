import re
import tkinter as tk
from tkinter import filedialog

def remove_date_time(text):
    # Define regular expressions to match date and time patterns
    datetime_pattern = r'\d{1,2}/\d{1,2}/\d{2,4},? ?\d{1,2}:\d{2}\s*[APap][Mm][\s]*-[\s,]*'

    # Use regular expression to find and remove date and time patterns
    cleaned_text = re.sub(datetime_pattern, '', text)
    
    return cleaned_text.strip()

def browse_file():
    global cleaned_text  # Declare the cleaned_text variable as global
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
            input_text = input_file.read()
        
        cleaned_text = remove_date_time(input_text)
        output_text.delete(1.0, tk.END)  # Clear any previous text in the Text widget
        output_text.insert(tk.END, cleaned_text)  # Insert the cleaned text into the Text widget

def download_file():
    global cleaned_text  # Declare the cleaned_text variable as global
    if cleaned_text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)
            print(f"File has been downloaded to {file_path}")
    else:
        print("No output text to download.")

# Create a tkinter window
root = tk.Tk()
root.title("File Upload")

# Create a button to browse and upload a file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=0)

# Create a Text widget to display the cleaned text (with a larger size)
output_text = tk.Text(root, wrap=tk.WORD, width=120, height=40)
output_text.grid(row=1, column=0)

# Create a scrollbar for the Text widget
scrollbar = tk.Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
output_text.config(yscrollcommand=scrollbar.set)

# Create a button to download the output file
download_button = tk.Button(root, text="Download", command=download_file)
download_button.grid(row=2, column=0)

# Initialize the cleaned_text variable
cleaned_text = ''

# Start the tkinter main loop
root.mainloop()
