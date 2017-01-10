
def print_restaraunt_ratings(restaurant_ratings):
    """Print restaurant ratings in alphabetical order.
    """

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print restaurant, 'is rated at', rating + '.'    


def add_user_restaurant_rating(restaurant_ratings):
    """Incorporate user restaurant rating.
    """

    add_restaurant_name = raw_input('Which restaurant would you like to add?\n')
    add_restaurant_rating = raw_input('What rating do you want to give it?\n')

    restaurant_ratings[add_restaurant_name] = add_restaurant_rating
    
    print_restaraunt_ratings(restaurant_ratings)

    return restaurant_ratings


def rate_restaurants(file_name):
    """Reformat and print restaurant ratings.

    Takes in a text file, creates a dictionary of
    restaurants and their ratings. Prints them in alphabetical
    order.
    """

    lines = open(file_name)

    restaurant_ratings = {}

    for line in lines:
        restaurant_name, restaurant_rating = line.rstrip().split(':')
        restaurant_ratings[restaurant_name] = restaurant_rating

    while True:
        choice_1 = '1. See current ratings,'
        choice_2 = '2. Add a new restaurant,'
        choice_3 = '3. Quit'

        user_choice = raw_input('Would you like to {} {} {}'.format(choice_1, choice_2, choice_3))

    print_restaraunt_ratings(restaurant_ratings)
    
    restaurant_ratings = add_user_restaurant_rating(restaurant_ratings)

rate_restaurants('scores.txt')