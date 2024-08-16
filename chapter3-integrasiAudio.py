import tkinter as tk
from tkinter import filedialog
import pygame

# Inisialisasi Pygame mixer
pygame.mixer.init()

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Multimedia Application")

def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            # Memuat dan memutar file musik menggunakan Pygame
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Terjadi kesalahan saat memutar musik: {e}")

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()
