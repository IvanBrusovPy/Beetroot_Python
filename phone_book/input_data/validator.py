def is_valid(value, data_type):
    match data_type:
        case "phone_num":
            return str(value).isdigit()
        case "name":
            return str(value).isalpha()



