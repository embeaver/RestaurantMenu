# Deleting an item from the database
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()
