from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.engine import create_engine

from config import app_config

engine = create_engine(app_config.DB_URL.unicode_string(), echo=True)
SessionFactory: sessionmaker = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(session_factory=SessionFactory)