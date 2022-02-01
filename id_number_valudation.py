# Functino which validates South Adrican ID number
import datetime


def validate_idno(val):
    # strip any leading and trailing spaces
    val = val.strip() if val else None
    # check for blank entry
    if val == None:
        return False
    # check length invalid for less than 13 digits
    if len(val) != 13:
        return False
    # check if non numeric characters are included
    if not (val.isnumeric()):
        return False
    # check if first six digits can be converted to date
    try:
        check_date = datetime.datetime.strptime(val[:6], "%y%m%d")
    except:
        return False

    # algorithm check
    # sum all digits in non equal postions in string
    test1 = (
        int(val[0])
        + int(val[2])
        + int(val[4])
        + int(val[6])
        + int(val[8])
        + int(val[10])
    )

    # concatenate all digits in equal position in string and then multiply the number by 2
    test2 = int(val[1] + val[3] + val[5] + val[7] + val[9] + val[11]) * 2

    # convert result from test2 to string
    str_test2 = str(test2)

    # sum each digit of the result of test2
    test3 = 0
    for it in range(0, len(str_test2)):
        test3 = test3 + int(str_test2[it])

    # add test3 to test1
    test1 = test1 + test3

    # get the comparison digit
    comp_digit = 0 if int(str(test1)[-1]) == 0 else 10 - int(str(test1)[-1])

    # compare comparison digit to final digit of id, if a match ID is valid
    if comp_digit == int(val[12]):
        return True

    # return false as default
    return False


# enter 13 digit id between ""
if validate_idno(""):
    print("ID is valid")
else:
    print("ID is NOT valid")
