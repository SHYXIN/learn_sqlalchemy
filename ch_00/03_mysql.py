from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://cookiemonster:chocolatechip@mysql01.monster.inter/cookies',
                       pool_recyle=3600)
