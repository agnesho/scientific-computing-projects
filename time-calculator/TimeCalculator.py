days_of_week = {0: 'Monday', 
1: 'Tuesday', 
2: 'Wednesday', 
3: 'Thursday', 
4: 'Friday', 
5: 'Saturday', 
6: 'Sunday',
7: 'No day given'}

# Change hours and minutes to minutes only #
def min_only(hour, minutes):
  return hour * 60 + minutes

# Change minutes back to hours and minutes #
# e.g. 100 minutes = 1 hour + 40 minutes
def hour(total_minutes):
  return total_minutes // 60

def minutes(total_minutes):
  return total_minutes % 60

# How many days from start time to new time? #
def new_day(start_time, duration_time, current_day, days_of_week):
  new_time = start_time + duration_time
  day_count = 0

  if new_time >= 1440:
    # Count how many days pass
    day_count = (duration_time - (1440 - start_time)) // 1440 + 1

    new_time = new_time - day_count * 1440
    
  return [new_time, day_count]

########## Main Function ##########
def add_time(start, duration, day_given='No day given'):
  start_lst = [i.split(':') for i in start.split()]
  duration_lst = duration.split(':')
  current_day = day_given[0].upper() + day_given[1:].lower()
  
  # Start time
  start_hr = int(start_lst[0][0])

  # Change to 24-hour clock format
  if 'PM' in start_lst[1]:
    start_hr += 12
  start_min = int(start_lst[0][1])
  start_time = min_only(start_hr, start_min)

  # Duration time
  duration_time = min_only(int(duration_lst[0]), int(duration_lst[1]))

  # New time
  new_time = new_day(start_time, duration_time, current_day, days_of_week)[0]
  day_count = new_day(start_time, duration_time, current_day, days_of_week)[1]
  # New time in hours and minutes
  new_hr = hour(new_time)
  new_min = minutes(new_time)

  # Extract key (0-7) from days_of_week dictionary given value ('Monday', 'Tuesday' etc.)
  value_list = list(days_of_week.values())
  start_day = value_list.index(current_day)
  # Which day of the week?
  day_of_week = (start_day + day_count) % 7
  try:
    day = days_of_week[day_of_week] 
  except:
    day = None

  # 'AM' or 'PM'
  # 12:00 AM - 12:59 AM
  if 0 < new_time < 59:
    new_hr += 12
    am_or_pm = 'AM'
  # 12:00 PM - 12:59 PM
  elif 720 <= new_time <= 779:
    am_or_pm = 'PM'
  # 1:00 PM to 11:59 PM
  elif 780 <= new_time <= 1439 :
    new_hr -= 12
    am_or_pm = 'PM'
  else:
    am_or_pm = 'AM'
  
  # Output
  if day_given == 'No day given' or day == None:
    if day_count == 0:
      return ('{}:{:0>2} {}'.format(new_hr, new_min, am_or_pm))
    elif day_count == 1:
      return ('{}:{:0>2} {} (next day)'.format(new_hr, new_min, am_or_pm))
    else:
      return ('{}:{:0>2} {} ({} days later)'.format(new_hr, new_min, am_or_pm, day_count))

  elif current_day in (v for v in days_of_week.values()):
    if day_count == 0:
      return ('{}:{:0>2} {}, {}'.format(new_hr, new_min, am_or_pm, day))
    elif day_count == 1:
      return ('{}:{:0>2} {}, {} (next day)'.format(new_hr, new_min, am_or_pm, day))
    else:
      return ('{}:{:0>2} {}, {} ({} days later)'.format(new_hr, new_min, am_or_pm, day, day_count))