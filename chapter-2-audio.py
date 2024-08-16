from pydub import AudioSegment
import pygame
import os


# 2.2.1 Memuat File Audio
try:
    audio = AudioSegment.from_file('NCT DREAM-Broken Melodies.mp3')
    print("✅ Audio loaded successfully.")
except Exception as e:
    print(f"❌ An error occurred while loading audio: {e}")
    exit()

    
# 2.2.2 Pemotongan Audio
try:
    clipped_audio = audio[:10000]  # 10 detik pertama
    clipped_audio.export('clipped_result.mp3', format='mp3')
    print("✅ Audio clipped and saved as clipped_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while clipping audio: {e}")

# 2.2.3 Penggabungan Audio
try:
    audio2 = AudioSegment.from_file('result.wav')
    combined_audio = audio + audio2
    combined_audio.export('combined_result.mp3', format='mp3')
    print("✅ Audio merged and saved as combined_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while merging audio: {e}")

# 2.2.4 Pengubahan Format Audio
try:
    audio.export('converted_result.wav', format='wav')
    print("✅ Audio converted and saved as converted_result.wav.")
except Exception as e:
    print(f"❌ An error occurred while converting audio format: {e}")

# Pastikan file 'converted_result.wav' ada sebelum melanjutkan ke langkah berikutnya
if not os.path.exists('converted_result.wav'):
    print("❌ File 'converted_result.wav' tidak ditemukan.")
    exit()


# 2.2.5 Pengaturan Volume
try:
    louder_audio = audio + 5  # Meningkatkan volume sebesar 5dB
    louder_audio.export('louder_result.mp3', format='mp3')
    print("✅ Audio volume increased and saved as louder_result.mp3.")
except Exception as e:
    print(f"❌ An error occurred while adjusting audio volume: {e}")

# 2.2.6 Memutar Audio Menggunakan Pygame
try:
    pygame.mixer.init()  # Inisialisasi pygame mixer
    pygame.mixer.music.load('converted_result.wav')  # Memuat file audio
    pygame.mixer.music.play()  # Memutar audio

    # Menunggu sampai audio selesai diputar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    print("✅ Audio is playing.")
except Exception as e:
    print(f"❌ An error occurred while playing the audio: {e}")
