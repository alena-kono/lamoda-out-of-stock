from datetime import datetime
from typing import Dict, List

from sqlalchemy import DateTime, Integer, String, inspect
from sqlalchemy.sql.schema import Column

from app.db import Base, Session
from app.stock.utils import add_current_datetime, convert_quantity_to_int


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    sku = Column(String(), index=True)
    quantity = Column(Integer, nullable=False, default=0)
    date_time = Column(DateTime, nullable=False)

    def __repr__(self) -> str:
        cls_name, instance_props = self.__class__.__name__, self.__dict__
        return f'<{cls_name}({instance_props})>'

    @staticmethod
    def preprocess_stock_states(stock_states: List[Dict]) -> List[Dict]:
        now = datetime.now()
        for sku_size in stock_states:
            convert_quantity_to_int(sku_size)
            add_current_datetime(sku_size, now)
        return stock_states

    def bulk_insert_mapping(self, stock_states: List[Dict]) -> None:
        mapper_class = inspect(self.__class__)
        with Session() as session:
            session.bulk_insert_mappings(
                mapper_class,
                stock_states
                )
            session.commit()
