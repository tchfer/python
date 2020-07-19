# -------------------------------------------------------------------------------
# takes in time a game started and finished to display how long it lasted
# (C) 2020 Flavio Fernando da Silva, Presidente Prudente, Brazil
# email tchfernando@gmail.com
# -------------------------------------------------------------------------------
#data input by user
initial_hour = int(input("Enter the hour the game begins -> "))
initial_minute = int(input("Now enter the minutes -> "))
ending_hour = int(input("Enter the hour the game ends -> "))
ending_minute = int(input("Enter the ending minutes -> "))
#calculates the length of game and outputs result
if initial_minute > ending_minute:
    ending_minute = ending_minute + 60
    ending_hour = ending_hour -1
if initial_hour > ending_hour:
    ending_hour = ending_hour + 24
minute_duration = ending_minute - initial_minute
hour_duration = ending_hour - initial_hour
print("The game lasted {}hrs:{}mins".format(hour_duration, minute_duration))