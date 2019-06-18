# Filling the restaurantmenu.db database with information

# Can be done from Python command line or in using python code (this)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

# Connection between database tables and corresponding class definitions
Base.metadata.bind = engine
# Staging zone for all objects loaded into the database
# will not go into database until Session.commit
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Add a Restaurant
myFirstRestaurant = Restaurant(
    name = "Pizza Palace"
)
session.add(myFirstRestaurant)
session.commit()
# to show this in database from command line: session.query(Restaurant).all()
# to show the first result in database: firstResult = session.query(Restaurant).first()
# then firstResult.name

# Add a menu item
cheesepizza = MenuItem(
    name = "Cheese Pizza",
    description = "Made with all natural ingredients and fresh mozzarella",
    course = "Entree",
    price = "$8.99",
    restaurant = myFirstRestaurant
)
session.add(cheesepizza)
session.commit()

# Explore SQLAlchemy queries
# to show the column names for items in database:
# items = session.query(MenuItem).all()
# for item in items:
#   print(item.name)
