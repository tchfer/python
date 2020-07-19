angle = float(input("Enter the measure of the angle in degrees: "))
if angle >= 360 or angle <= -360:
  rounds = angle // 360
  angle = angle % 360
else:
  rounds = 0
if (angle == 0 or angle == 90 or angle == 180
               or angle == 270 or angle == 360
               or angle == -90 or angle == -180
               or angle == -270 or angle == -360):
  print("It's on one of the axis.")
else:
  if (angle > 0 and angle < 90) or (angle < -270 and angle > -360):
    print("First quadrant")
  if (angle > 90 and angle < 180) or (angle < -180 and angle > -270):
    print("Second quadrant")
  if (angle > 180 and angle < 270) or (angle < -90 and angle > -180):
    print("Third quadrant")
  if (angle > 270 and angle < 360) or (angle < 0 and angle > -90):
    print("Fourth quadrant")
  print(rounds, "Round(s) per turn")
if angle < 0:
  print("Clockwise direction")
else:
  print("Counter clockwise direction")