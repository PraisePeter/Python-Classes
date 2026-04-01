distance_mi = 0
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = True

if distance_mi == 0:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif distance_mi <= 1 and is_raining:
    print(False)
# else:
# print(False)

if distance_mi > 1 and distance_mi <= 6:
    if is_raining and has_bike == False:
        print(False)
    elif is_raining == False and has_bike == False:
        print(False)
    elif has_bike == True and not is_raining:
        print(True)
if distance_mi > 6:
    if has_ride_share_app == True:
        print(True)
    elif has_car == True:
        print(True)
    elif has_car == False or has_ride_share_app == False:
        print(False)


