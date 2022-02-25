from datetime import datetime, timedelta


def main():
    print("The time is set to go off at: {0}".format(show_set_alarm(get_input())))


def get_input():
    valid = False
    while not valid:
        current_time = input("Enter current time in 24h format (enter to use current time): ")
        if current_time == "":
            current_time = datetime.now().strftime("%H:%M:%S")
        else:
            if len(current_time) == 2:
                current_time = "{0}:00:00".format(current_time)
            elif len(current_time) == 5:
                current_time = "{0}:00".format(current_time)
        try:
            datetime.strptime(current_time, "%H:%M:%S")
            valid = True
        except ValueError:
            valid = False

    alarm = ""
    while not isinstance(alarm, int):
        try:
            alarm = int(input("Enter number of hours the alarm will go off: "))
        except ValueError:
            alarm = ""

    return current_time, alarm


def show_set_alarm(user_input):
    return (datetime.strptime(user_input[0], "%H:%M:%S") + timedelta(hours=user_input[1])).strftime("%H:%M:%S")


if __name__ == "__main__":
    main()

