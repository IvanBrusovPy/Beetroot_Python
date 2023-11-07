from datetime import datetime


class MyOpen:
    counter = 0
    f = None

    def __init__(self, file_path, mode='r'):
        self.file = file_path
        self.mode = mode
        self.logger = open("logs.txt", "a")

    def __enter__(self):
        self.counter += 1
        try:
            self.f = open(self.file, self.mode)
        except Exception as e:
            self.__exit__(e, '', "")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Error: {exc_type}")
            print(f"{datetime.now().strftime('%d/%m/%y %H:%M:%S')} {exc_type} {exc_val} {exc_tb}", file=self.logger)
            return True
        self.f.close()

        self.logger.close()
        return True



file = MyOpen("test_file.txt", "a")
print(file.counter)
with file as f:
    f.write("2")
print(file.counter)
