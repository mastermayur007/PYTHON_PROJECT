from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Image Slideshow Viewer")

# Image paths and resizing
image_path = [
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241022_19_10_41_Pro.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241022_19_10_58_Pro.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241215_21_18_35_Pro - Copy.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241215_21_19_51_Pro.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241022_19_10_41_Pro.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241022_19_10_41_Pro.jpg", 
    r"E:\INSTA_POST\TG LINKDEDO 💯\WIN_20241022_19_10_41_Pro.jpg", 
]
image_size = (1080, 1080)

# Load and resize images
try:
    images = [Image.open(path).resize(image_size) for path in image_path]
    photo_images = [ImageTk.PhotoImage(image) for image in images]
except FileNotFoundError as e:
    print(f"Error: {e}")
    root.destroy()
    exit()

# Create a cycle for the slideshow
slideshow = cycle(photo_images)

# Create a label to display images
label = tk.Label(root)
label.pack()

# Function to update the image
def update_image():
    photo_image = next(slideshow)  # Get the next image
    label.config(image=photo_image)
    root.after(3000, update_image)  # Schedule the next update after 3 seconds

# Button to start the slideshow
play_button = tk.Button(root, text="Play Slideshow", command=update_image)
play_button.pack()

# Start the Tkinter main loop
root.mainloop()
