from datetime import datetime
from typing import Dict, List, NoReturn, Optional, Union

from sqlalchemy import DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.schema import Column

from app.config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False, future=True)
Session = sessionmaker(engine)
Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    sku = Column(String(), unique=True)
    quantity = Column(Integer)
    date_time = Column(DateTime)

    def __repr__(self) -> str:
        return f'<Stock({self.__dict__})>'

    @staticmethod
    def _convert_str_to_int(string: str) -> Union[int, NoReturn]:
        try:
            converted_int = int(string)
        except ValueError:
            raise ValueError
        return converted_int

    def _add_one_sku(self, sku: str, quantity: str):
        int_quantity = self._convert_str_to_int(quantity)
        date_time = datetime.now()
        stock = Stock(
            sku=sku,
            quantity=int_quantity,
            date_time=date_time,
        )
        return stock

    def extract_stock(self, stock_states: List[Dict]) -> list:
        stock_objects = []
        for sku_qty in stock_states:
            stock = self._add_one_sku(sku_qty['sku'], sku_qty['quantity'])
            stock_objects.append(stock)
        return stock_objects

    @staticmethod
    def save_bulk(stock_objects: list) -> None:
        # main() time performance: 0.0041 s
        with Session() as session:
            session.bulk_save_objects(stock_objects)
            session.commit()
