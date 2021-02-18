import requests

third_digit_input = input("Enter the ip third digit range e.g 119-127: ")

third_digit_input = third_digit_input.replace(" ", "")

third_digit_input = third_digit_input.split("-")

last_digit_input = input("Enter the ip last digit range e.g 0-255: ")

last_digit_input = last_digit_input.replace(" ", "")

last_digit_input = last_digit_input.split("-")

for third_digit in range(int(third_digit_input[0]), int(third_digit_input[1])):
    for last_digit in range(int(last_digit_input[0]), int(last_digit_input[1])):
        url = "http://196.223.{}.{}".format(third_digit, last_digit)
        try:
            r = requests.get(url, timeout=2)
            print("{} got a status code of {}".format(url, r.status_code))
        except:
            print("Couldn't connect to {}".format(url))
