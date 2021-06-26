from datetime import datetime
from typing import Any, Dict, NoReturn, Union
from app.exceptions import ConvertionError


def convert_str_to_int(string: str) -> Union[int, NoReturn]:
    try:
        converted_int = int(string)
    except ValueError:
        raise ConvertionError(f'str {string} cannot be converted to int')
    return converted_int


def convert_quantity_to_int(sku_size: Dict[str, Any]) -> None:
    str_qty = sku_size.get('quantity')
    if str_qty:
        int_qty = convert_str_to_int(str_qty)
        sku_size['quantity'] = int_qty


def add_current_datetime(sku_size: Dict[str, Any], now: datetime) -> None:
    sku_size.update({'date_time': now})
