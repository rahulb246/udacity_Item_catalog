from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Algorithms, User

engine = create_engine('sqlite:///algorithms.db')
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



# create a dummy user
User1 = User(name="messi", email="messi@udacity.com")
session.add(User1)
session.commit()

User2 = User(name="neymar", email="neymar@udacity.com")
session.add(User2)
session.commit()

# Deep Learning Algorithms
c1 = Category(name = "Deep Learning Algorithms", user_id = 1)
session.add(c1)
session.commit()

a1 = Algorithms(name = "Convolutional Neural Networks",
			category_id = 1,
            user_id = 1)
session.add(a1)
session.commit()

a2 = Algorithms(name = "Deep Belief Networks",
			category_id = 1,
            user_id = 1)
session.add(a2)
session.commit()

a2 = Algorithms(name = "Deep Boltzman Machines",
			category_id = 1,
            user_id = 1)
session.add(a2)
session.commit()

# Regression Algorithms
r1 = Category(name = "Regression Algorithms", user_id = 2)
session.add(r1)
session.commit()

a1 = Algorithms(name = "Linear Regression",
			category_id = 2,
            user_id = 2)
session.add(a1)
session.commit()

a1 = Algorithms(name = "Logistic Regression",
			category_id = 2,
            user_id = 2)
session.add(a1)
session.commit()
