weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num_weekdays = {key + 1: value for key, value in enumerate(weekdays)}
weekdays_num = {value: key for key, value in num_weekdays.items()}
print(num_weekdays)
