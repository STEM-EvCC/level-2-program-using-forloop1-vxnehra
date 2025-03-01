mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
total = 0
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
total_success = 0


for mission in mission_names:
    total += 1
print(f" The total amount of space missions is equal to {total}")

for success in mission_success:
  if success == True:
    total_success += 1
print(f" The total amount of successful missions is equal to {total_success}")

for rate in mission_success:
  rate = (total_success / total)*100
print(f" The rate of successful missions is equal to {rate:.2f}%")

for launched in mission_years:
    if launched < 2000:
        print(f"- {mission_names[mission_years.index(launched)]}")

