while True:
  year = input("Please provide a year: ")
  if year.isdigit():

    new_year = int(year)

    s_leap_year = None

    if new_year % 4 == 0:
        if new_year % 100 == 0:
            if new_year % 400 == 0:
                is_leap_year = True
            else:
                  is_leap_year = False
        else:
            is_leap_year = True
    else:
          is_leap_year = False

    if is_leap_year:
        print(f'{year} is a leap year')
        break
    else:
        print(f'{year} is not a leap year')
        break

  else:
    print("This is not a number")
