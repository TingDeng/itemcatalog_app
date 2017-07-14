from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import City, Base, Trip, User

engine = create_engine('sqlite:///cityinfo.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Joy Morgan", email="121114864@qq.com",
             picture='https://en.opensuse.org/images/0/0b/Icon-user.png')
session.add(User1)
session.commit()

# Info for Florida cities
#Info for Orlando
city1 = City(user_id=1, name="Orlando")

session.add(city1)
session.commit()

trip1 = Trip(user_id=1, name="Gyu-Kaku Japanese BBQ", 
                     description="Gyu-Kaku Japanese BBQ is the ideal spot to enjoy an ice cold beer as you grill your own meat.",
                     price="$50.00", info="Restaurants", city=city1)

session.add(trip1)
session.commit()


trip2 = Trip(user_id=1, name="EMBASSY SUITES", 
                     description="Complimentary breakfast and evening reception.",
                     price="$115.00", info="Hotels", city=city1)

session.add(trip2)
session.commit()

trip3 = Trip(user_id=1, name="SeaWorld", 
                     description="SeaWorld Orlando has many live shows and attractions including rides and animal exhibits.",
                     price="$79.99", info="Things to do", city=city1)

session.add(trip3)
session.commit()

trip4 = Trip(user_id=1, name="Disney World", 
                     description="Interactive rides, animal adventures, magical attractions",
                     price="$99.50", info="Things to do", city=city1)

session.add(trip4)
session.commit()

trip5 = Trip(user_id=1, name="Universal Studios", 
                     description="Ride the movies, live the adventure, experience epic thrills",
                     price="$110.00", info="Things to do", city=city1)

session.add(trip5)
session.commit()

trip6 = Trip(user_id=1, name="Hot & Juicy Crawfish", 
                     description="Casual, hands-on joint for Cajun crawfish",
                     price="$70.00", info="Restaurants", city=city1)

session.add(trip6)
session.commit()

trip7 = Trip(user_id=1, name="Sheraton", 
                     description="A few blocks from Walt Disney World",
                     price="$99.00", info="Hotels", city=city1)

session.add(trip7)
session.commit()

# Info for Tampa
city2 = City(user_id=1, name="Tampa")

session.add(city2)
session.commit()


trip8 = Trip(user_id=1, name="Clearwater Beach", 
                     description="Best Beach Town in Florida",
                     price="$20.00", info="Things to do", city=city2)

session.add(trip8)
session.commit()

trip9 = Trip(user_id=1, name="Mitchell's Fish Market",
                     description="Seafood dishes, a raw bar & happy-hour martinis", 
					 price="$40.00", info="Restaurants", city=city2)

session.add(trip9)
session.commit()

trip10 = Trip(user_id=1, name="Seasons 52", 
                     description="Rotating menu of seasonal American dishes",
                     price="$40.00", info="Restaurants", city=city2)

session.add(trip10)
session.commit()

trip11 = Trip(user_id=1, name="DoubleTree Suites Tampa Bay", 
                     description="Waterfront Suites",
                     price="$109.00", info="Hotels", city=city2)

session.add(trip11)
session.commit()

trip12 = Trip(user_id=1, name="Tampa Riverwalk", 
                     description="It is a beautiful path that follows the river around the downtown area",
                     price="$5.00", info="Things to do", city=city2)

session.add(trip12)
session.commit()

trip13 = Trip(user_id=1, name="Hyatt Regency Clearwater", 
                     description="Set between the Gulf of Mexico and Clearwater Bay",
                     price="$275.00", info="Hotels", city=city2)

session.add(trip13)
session.commit()


# Info for Key West
city3 = City(user_id=1, name="Key West")

session.add(city3)
session.commit()


trip14 = Trip(user_id=1, name="The Inn", 
                     description=" Tropically furnished rooms",
                     price="$127.00", info="Hotels", city=city3)

session.add(trip14)
session.commit()

trip15 = Trip(user_id=1, name="Casa Marina Resort", 
                     description="The Mediterranean-styled rooms offer city views or ocean views",
                     price="$279.00", info="Hotels", city=city3)

session.add(trip15)
session.commit()

trip16 = Trip(user_id=1, name="Ernest Hemingway House", 
                     description="Grand Architecture, Lush Gardens, Educational Tours",
                     price="$13.00", info="Things to do", city=city3)

session.add(trip16)
session.commit()

trip17 = Trip(user_id=1, name="Southernmost point buoy",
                     description="marking the southernmost point in the continental United States",
                     price="$0.00", info="Things to do", city=city3)

session.add(trip17)
session.commit()

trip28 = Trip(user_id=1, name="El Siboney Restaurant",
                     description="Traditional Cuban home cooking & housemade sangria in a casual, family-friendly setting",
                     price="$40.00", info="Restaurants", city=city3)

session.add(trip28)
session.commit()

trip18 = Trip(user_id=1, name="Smathers Beach", 
                     description="The largest public beach in Key West",
                     price="$0.00", info="Things to do", city=city3)

session.add(trip18)
session.commit()


# Info for Miami
city4 = City(user_id=1, name="Miami")

session.add(city4)
session.commit()


trip19 = Trip(user_id=1, name="Wynwood Arts District", 
                     description="If you like urban art, in big walls, this is the place to be!",
                     price="$0.00", info="Things to do", city=city4)

session.add(trip19)
session.commit()

trip20 = Trip(user_id=1, name="Biscayne National Park", 
                     description="Biscayne National Park encompasses coral reefs, islands and shoreline mangrove forest",
                     price="$25.00", info="Things to do", city=city4)

session.add(trip20)
session.commit()

trip21 = Trip(user_id=1, name="InterContinental Miami",
                     description="InterContinental Miami is a luxury Miami hotel located on the water", 
					 price="$152.00", info="Hotels", city=city4)

session.add(trip21)
session.commit()

trip22 = Trip(user_id=1, name="Joe's Stone Crab", 
                     description="Operating for over 100 years, it has the best claws in town",
                     price="$100.00", info="Restaurants", city=city4)

session.add(trip22)
session.commit()

trip23 = Trip(user_id=1, name="Nikko by Sunshine", 
                     description="Stylish, modern kitchen serving eclectic Asian dishes",
                     price="$70.00", info="Restaurants", city=city4)

session.add(trip23)
session.commit()


# Info for West Palm Beach
city5 = City(user_id=1, name="West Palm Beach")

session.add(city5)
session.commit()


trip24 = Trip(user_id=1, name="Lion Country Safari", 
                     description="Lion Country Safari, West Palm Beach. Florida's only drive-through safari boasts 800-plus animals",
                     price="$80.00", info="Things to do", city=city5)

session.add(trip24)
session.commit()

trip25 = Trip(user_id=1, name="Palm Beach", 
                     description="the Atlantic coast barrier island",
                     price="$0.00", info="Things to do", city=city5)

session.add(trip25)
session.commit()

trip29 = Trip(user_id=1, name="Hullabaloo", 
                     description="Trendy gastropub for Italian fare, cocktails & brews, with a vintage Airstream camper on the patio",
                     price="$50.00", info="Restaurants", city=city5)

session.add(trip29)
session.commit()

trip30 = Trip(user_id=1, name="PGA Resort", 
                     description="The service at this facility is top notch",
                     price="$139.00", info="Hotels", city=city5)

session.add(trip30)
session.commit()


# Info for St. Augustine
city6 = City(user_id=1, name="St. Augustine")

session.add(city6)
session.commit()


trip26 = Trip(user_id=1, name="ST. AUGUSTINE LIGHTHOUSE", 
                     description="Climb 219 steps to the top for breathtaking views of the nation's oldest city and the Atlantic Ocean",
                     price="$24.95", info="Things to do", city=city6)

session.add(trip26)
session.commit()

trip27 = Trip(user_id=1, name="Castillo de San Marcos", 
                     description="The oldest masonry fort in the continental United States",
                     price="$10.00", info="Things to do", city=city6)

session.add(trip27)
session.commit()

trip31 = Trip(user_id=1, name="Harry's Seafood, Bar & Grille", 
                     description="Chain outpost serving up Creole dishes in a leafy courtyard or on a balcony overlooking the bay",
                     price="$30.00", info="Restaurants", city=city6)

session.add(trip31)
session.commit()

trip32 = Trip(user_id=1, name="Casa Monica Resort & Spa", 
                     description="In the center of Downtown, this grand Moroccan-themed hotel has an ornate lobby with frescos, fountains and chandeliers",
                     price="$209.00", info="Hotels", city=city6)

session.add(trip32)
session.commit()

print "Added trip info for Florida cities!"