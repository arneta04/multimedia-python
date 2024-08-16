import pygame
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

# Fungsi untuk menjalankan Pygame
def run_game():
    # Inisialisasi Pygame
    pygame.init()

    # Mengatur tampilan
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Simple Game")

    # Memuat gambar
    image = pygame.image.load('mark lee.jpeg')

    # Variabel untuk posisi gambar
    x = 0
    running = True

    # Loop utama permainan
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Memperbarui posisi
        x += 5
        if x > 800:
            x = 0

        # Mengisi layar dengan warna hitam
        screen.fill((0, 0, 0))

        # Menggambar gambar di posisi baru
        screen.blit(image, (x, 100))

        # Memperbarui tampilan
        pygame.display.flip()

    # Keluar dari Pygame
    pygame.quit()

# Membuat jendela utama Tkinter
root = tk.Tk()
root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename(title="Pilih File Musik", filetypes=[("Audio Files", ".mp3;.wav")])
    if file_path:
        try:
            # Inisialisasi mixer Pygame
            pygame.mixer.init()

            # Memuat dan memutar musik
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat memutar musik: {e}")

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan Pygame dalam thread terpisah
game_thread = threading.Thread(target=run_game)
game_thread.start()

# Menjalankan loop acara Tkinter
root.mainloop()