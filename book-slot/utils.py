import datetime
import logging

def get_date(weekday_index):
    print('INFO: Fetching date to book the slot...')
    current_date = datetime.datetime.now()
    
    # TODO: Enable this logic later
    # if current_date.weekday() == weekday_index:
    #     return current_date.strftime("%d/%m/%Y")
    
    # Finding delta days
    days_delta = weekday_index - current_date.weekday()
    if days_delta <= 0: days_delta += 7
    
    # adding days to required result
    date = current_date + datetime.timedelta(days_delta)
    date = date.strftime("%d/%m/%Y")
    
    print(f'INFO: Selected Date: {date}')
    return date

def get_logger():
    return logging.basicConfig(level=logging.INFO)
