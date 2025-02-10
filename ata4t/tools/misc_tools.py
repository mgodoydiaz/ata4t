import datetime

def get_milliseconds(date_str, fmt = "%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.strptime(date_str, fmt)
    epoch_time = datetime.datetime(1970, 1, 1)
    delta = dt - epoch_time
    return int(delta.total_seconds() * 1000)
    
if __name__=="__main__":
    print(get_milliseconds("2023-04-05 22:00:00"))