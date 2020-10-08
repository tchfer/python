'''8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.'''

def duracao_jogo():
    initial_hour = int(input("Digite o horário que o jogo começa(horas) -> "))
    initial_minute = int(input("Agora digite os minutos do início do jogo -> "))
    ending_hour = int(input("Digite o horário que o jogo termina(horas) -> "))
    ending_minute = int(input("Agora digite os minutos do término do jogo -> "))
    if initial_minute > ending_minute:
        ending_minute += 60
        ending_hour -= 1
    if initial_hour > ending_hour:
        ending_hour += 24
    minute_duration = ending_minute - initial_minute
    hour_duration = ending_hour - initial_hour
    print("O jogo durou {} hrs:{} mins".format(hour_duration, minute_duration))

def main():
    duracao_jogo()

main()