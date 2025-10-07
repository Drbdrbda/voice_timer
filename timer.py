import time

timers = []

def convert_to_seconds(seconds, minutes = 0, hours = 0):
    total_time = round(hours * (60) ** 2 + minutes * 60 + seconds, 2)
    return total_time 

# def convert_to_seconds(seconds):
#     total_time = round(seconds, 2)
#     return total_time

def convert_to_other_units(seconds, minutes = 0, hours = 0):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    units_of_time_list = [str(hours), str(minutes), str(seconds)]
    total_time = ':'.join(units_of_time_list)
    return total_time

def record_the_time(seconds):
    start_time = time.time()
    user_time = convert_to_seconds(seconds)
    result_time = start_time + user_time

    while True:
        current_time = time.time()
        if current_time >= result_time:
            print('ВРЕМЯ ВЫШЛО!')
            break

def add_timer(amount_of_timers):
    tracking_time_list = []

    for timer in range(amount_of_timers):
        print(f'\nКакое время засечь для таймера {timer+1}?')
        recorded_time = convert_to_seconds(int(input()), int(input()), int(input()))
        tracking_time_list.append(recorded_time)

    return tracking_time_list

def setup():
    global timers 

    amount_of_timers = int(input('Сколько таймеров хотите засечь? \n'))
    timers = add_timer(amount_of_timers)

    print(f"Созданы таймеры: {timers}")

def loop():
    global timers
    
    if not hasattr(loop, 'start_times'):
        loop.start_times = [time.time() for _ in range(len(timers))]
        print('\nТаймеры запущены')
    
    current_time = time.time()

    for i in range(len(timers) - 1, -1, -1):
        elapsed_time = current_time - loop.start_times[i]

        if elapsed_time >= timers[i]:
            print(f'\nПрошло {timers[i]} секунд. ВРЕМЯ ВЫШЛО!')
            del timers[i]
            del loop.start_times[i]

    if len(timers) == 0:
         print("\n🎉 Все таймеры завершены!")
         return False

    return True
            
def main():
    setup()

    #return_flag = input('Засчечь снова? (да/ нет) \n')

    try:
        while loop():
            time.sleep(0.5) 
    except KeyboardInterrupt:
        print("\n Программа остановлена")


main()

'''
def loop():
    global timers
    
    if not hasattr(loop, 'start_times'):
        loop.start_times = [time.time() for _ in range(len(timers))]
        loop.finished_timers = [False] * len(timers)
        print('Таймеры запущены')
    
    current_time = time.time()

    for i in range(len(timers)):
        if not loop.finished_timers[i]:
            elapsed_time = current_time - loop.start_times[i]

            if elapsed_time >= timers[i]:
                loop.finished_timers[i] = True
                if not loop.finished_timers[i]:
                    loop.finished_timers[i] = True
            
            if loop.finished_timers[i] == True:
                print(f' Таймер {i+1} ВРЕМЯ ВЫШЛО!')
                break

    if all(loop.finished_timers):
         print("\n🎉 Все таймеры завершены!")
         return False

    return True
'''