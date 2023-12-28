from sqlalchemy import create_engine

engine = create_engine('sqlite:///cookies.db')
# engine2 = create_engine('sqlite:///:memory:')
# engine3 = create_engine('sqlite:///home/cookiemonster/cookies.db')
# engine4 = create_engine('sqlite:///c:\\User\\cookiemonster\\cookies.db')

print(engine)
