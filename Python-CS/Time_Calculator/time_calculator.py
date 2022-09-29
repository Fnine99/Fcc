def add_time(start, duration, day = None):
    week_days_dict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    # Start time array
    start_array = start.split(':')
    start_hour = int(start_array[0])
    start_array_minute = start_array[1].split(' ')
    start_minute = int(start_array_minute[0])
    am_pm = start_array_minute[1]
    am_pm_flip = {'AM': 'PM', 'PM': 'AM'}

    # Duration time array
    duration_array = duration.split(':')
    duration_hour = int(duration_array[0])
    duration_minute = int(duration_array[1])

    days_amount = int(duration_hour/24)


    # finish time
    finish_time_minute = start_minute + duration_minute
    if finish_time_minute >= 60:
        start_hour += 1
        finish_time_minute = finish_time_minute % 60

    am_pm_flip_amount = int((start_hour+duration_hour)/12)
    finish_time_hour = (start_hour+duration_hour) % 12

    if finish_time_minute <= 9:
        finish_time_minute = '0' + str(finish_time_minute)

    # if finish_time_hour <= 9:
    #     finish_time_hour = '0' + str(finish_time_hour)
    if finish_time_hour == 0: finish_time_hour = '12'


    if am_pm == 'PM' and start_hour + (duration_hour%12) >= 12:
        days_amount += 1


    # Even or Odd number, Even means same am_pm Odd means flip am_pm
    if am_pm_flip_amount % 2 == 0:
        am_pm = am_pm
    else:
        am_pm = am_pm_flip[am_pm]


    new_time = str(finish_time_hour) +':'+ str(finish_time_minute) +' '+ am_pm

    if day:
        day = day.lower()
        index = int((week_days_dict[day]) + days_amount) % 7
        finish_day = week_days[index]
        new_time = new_time + ', ' + finish_day
    if days_amount == 1:
        new_time = new_time + ' ' +'(next day)'
    elif days_amount > 1:
        new_time = new_time + ' ' + f'({days_amount} days later)'





    return new_time