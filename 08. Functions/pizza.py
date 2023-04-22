def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")




def build_profile(first='' , last='' , **info):
    info['firstname'] = first
    info['lastname'] = last 
    return info 
