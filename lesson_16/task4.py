from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        with open('log.txt', 'w') as f:
            print(str(msg), file=f)


try:
    a = [1]
    b = a[2]
except IndexError as e:
    raise CustomException(f"Type: {e} at {datetime.now()}")
