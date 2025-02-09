import pygame
import time

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load("music.mp3")
    print("Música carregada com sucesso!")
except pygame.error as e:
    print(f"Erro ao carregar a música: {e}")
    exit()

pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.play()
print("Tocando música...")

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Música terminou.")