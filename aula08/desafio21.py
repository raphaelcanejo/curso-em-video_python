# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("humble.mp3")
pygame.mixer.music.play()
print('Está tocando a música Humble de Kendrick Lamar')
pygame.event.wait()
