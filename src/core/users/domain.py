import abc
import uuid
from dataclasses import dataclass

from core.auction.domain import Auction
from core.bidding.domain import Bidding


class BaseUser(abc.ABC):

    def __init__(
            self,
            *,
            user_id: uuid.UUID = uuid.uuid4(),
            username: str,
            password: str,
            email: str,
    ):
        self.user_id: uuid.UUID = user_id
        self.username: str = username
        self.password: str = password
        self.email: str = email


    def __str__(self):
        return f"<{self.__class__.__name__}> ID - {self.user_id}, USERNAME - {self.username}"


class Seller(BaseUser):

    def start_auction(self, *, auction: Auction) -> Auction:
        pass

    def cancel_auction(self, *, auction: Auction) -> Auction:
        pass

    def change_auction_item_details(self, *, auction: Auction) -> Auction:
        pass


class Buyer(BaseUser):

    def place_bid(self, *, auction: Auction) -> Bidding:
        pass

    def retract_bid(self, *, auction: Auction) -> Bidding:
        pass


class User(Seller, Buyer):
    pass
