# all veggie burgers in database
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

# print information about veggie burgers
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print('\n')

UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
print(UrbanVeggieBurger.price)

# Update the UrbanVeggieBurger price to $2.99, the id was 8
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

# Update the other veggie burgers to compete with Urban restaurant price
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()