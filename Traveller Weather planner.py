distance = 3
is_raining = False
has_bike = True
has_car = False
has_car_share_app = False

if not distance:
  print(False)
elif distance <= 1 and not is_raining:
  print(True)
elif distance <= 1 and is_raining :
  print(False)

elif 1 < distance <=6 and has_bike and not is_raining:
  print(True)
elif 1< distance <=6:
  print(False)

elif distance > 6 and (has_car or has_car_share_app):
  print(True)
elif distance > 6:
  print(False)
