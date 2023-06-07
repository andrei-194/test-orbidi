from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    def __init__(self):
        self.db_url = 'postgresql://developer:qS*7Pjs3v0kw@db.g97.io:5432/data_analyst'
        self.engine = None
        self.session = None

    def connect(self):
        self.engine = create_engine(self.db_url)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def disconnect(self):
        if self.session is not None:
            self.session.close()
        if self.engine is not None:
            self.engine.dispose()
