### light.py
distance_miles = float(input('Enter Distance (miles): '))
m_distance = distance_miles * 1.61 * 1000 # converting miles to m
light_speed = 299792458
seconds = m_distance / light_speed  # total seconds

# separating total seconds into hrs, min, secs.
hours = int(seconds // 3600)  # 1 hour = 3600 seconds
minutes = int((seconds % 3600) // 60)
seconds = round(seconds % 60,1)

print('Light travel time:', hours, 'h', minutes, 'm', seconds, 's')