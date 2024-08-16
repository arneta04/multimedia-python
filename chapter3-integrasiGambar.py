from PIL import Image, ImageTk
import tkinter as tk

# Inisialisasi root window
root = tk.Tk()
root.title("Menampilkan Gambar")

# Memuat gambar menggunakan Pillow
image = Image.open('mark lee.jpeg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Menjalankan main loop
root.mainloop()