def convert(number):
    factors = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }

    result = []
    for factor, sound in factors.items():
        if number % factor == 0:
            result.append(sound)

    if len(result) == 0:
        result.append(str(number))

    return ''.join(result)
