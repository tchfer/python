#Faça um programa em Python que abra e reproduza o um arquivo MP3 aleatório dentro de uma pasta do computador.
import pygame
import os
import random
pygame.mixer.init()
path = '/home/fernando/Documents/PYTHON/lista_guanabara/Pearl Jam - MTV Unplugged (2019)'
files = os.listdir(path)
d = random.choice(files)
pygame.mixer.music.load(d)
pygame.mixer.music.play(loops=1, start=0)
pygame.mixer.music.set_volume(100)
print('Você está ouvindo o melhor unplugged da MTV!\nReproduzindo - {}'.format(d))
p = input("Digite algo e clique 'enter' para finalizar.\n")
