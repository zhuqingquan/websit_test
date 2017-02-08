from sqlalchemy import *

#metadata = BoundMetaData('sqlite:///tutorial.db')

engine = create_engine("sqlite:///tutorial.db")
connection = engine.connect()
metadata = MetaData()
metadata.bind = engine
