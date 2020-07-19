"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""
n = int(input('Digite um número inteiro: '))
print('O antecessor do número é {} e o sucessor dele é {}'.format((n-1), (n+1)))# poderia ter feito o calculo antes
# do print, mas quanto menos variáveis, mais rápido o programa lê o código
