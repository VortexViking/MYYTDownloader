import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import webbrowser

def download_youtube_video():
    video_url = url_entry.get()
    save_path = save_path_entry.get() or '.'

    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=save_path)
        messagebox.showinfo("Success", f'Download completed: {yt.title}')
    except Exception as e:
        messagebox.showerror("Error", f'An error occurred: {e}')

def open_hyperlink(event):
    webbrowser.open_new("https://youtube.com/@IamVortexViking")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x300")
root.configure(bg="#2E2E2E")

# Create and place the URL entry
url_label = tk.Label(root, text="YouTube Video URL:", bg="#2E2E2E", fg="white")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the save path entry
save_path_label = tk.Label(root, text="Save Path (optional):", bg="#2E2E2E", fg="white")
save_path_label.pack(pady=10)
save_path_entry = tk.Entry(root, width=50)
save_path_entry.pack(pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download Video", command=download_youtube_video, bg="#4CAF50", fg="white")
download_button.pack(pady=20)

# Create and place the hyperlink
hyperlink = tk.Label(root, text="Visit VortexViking's Channel", fg="blue", bg="#2E2E2E", cursor="hand2")
hyperlink.pack(pady=10)
hyperlink.bind("<Button-1>", open_hyperlink)

# Start the GUI event loop
root.mainloop()
