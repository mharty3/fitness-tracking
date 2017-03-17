def bodyfat(measurements, sex='male', age=24):

    if ((type(measurements) == list) | (type(measurements) == tuple)):
        if (len(measurements) == 3):
            measurements = sum(measurements)
        else:
            raise ValueError('Enter three meaurements (in mm) or the sum of three measurements (in mm)')


    if (sex == 'male') | (sex == 'Male') | (sex == 'm') | (sex == 'M'):
        body_density = 1.10938 - (0.0008267 * measurements) + (0.0000016 * measurements**2) - (0.0002574 * age)
    elif (sex == 'female') | (sex == 'Female') | (sex == 'f') | (sex == 'F'):
        body_density = 1.0994921 - (0.0009929 * measurements) + (0.0000023 * measurements) - (0.0001392 * age)
    else:
        raise ValueError('Invalid value entered for sex: use male, female, Male, Female, m, f, M, or F')

    fat = ((4.95 / body_density) - 4.5)
    return fat

print(bodyfat((8, 20, 10), sex='m'))
