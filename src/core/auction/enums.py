import enum


class CurrencyEnum(enum.StrEnum):
    RUB = "RUB"
    USD = "USD"


class AuctionStatusEnum(enum.StrEnum):
    ACTIVE = "ACTIVE"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"
