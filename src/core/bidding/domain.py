import datetime as dt
from dataclasses import dataclass
import uuid
import decimal


@dataclass
class Bidding:
    bidding_id: uuid.UUID
    user_id: uuid.UUID
    price: decimal.Decimal()
    created_at: dt.datetime
