

def choose_diffrent_city(city):

    answer = input('the current city is {}, would you like to choose another city? (enter "NO" or the city name): '.format(city))
    is_alpha_or_space = all(c.isalpha() or c.isspace() for c in answer)
    while is_alpha_or_space is not True:
        answer = input('Please enter again,the current city is {}, would you like to choose another city? (enter "NO" or the city name): '.format(city))
        is_alpha_or_space = all(c.isalpha() or c.isspace() for c in answer)
    if answer.lower() != 'no':
        city = str(answer.title())
    return city
