class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


try:
    age = int(input("Enter Age: "))

    if age > 60:
        raise TooOldException(
            "Your age has crossed the marriage age... no chance of getting married"
        )

    elif age < 18:
        raise TooYoungException(
            "Please wait some more time. You will get the best match soon."
        )

    else:
        print("You are eligible for marriage.")

except TooYoungException as e:
    print(e.msg)

except TooOldException as e:
    print(e.msg)

except ValueError:
    print("Please enter a valid number.")