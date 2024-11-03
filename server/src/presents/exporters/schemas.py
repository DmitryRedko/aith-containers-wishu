from typing import Optional, List
from pydantic import BaseModel


class GiftImagesSchema(BaseModel):
    image: str


class GiftLinksSchema(BaseModel):
    link: str


class GiftSchema(BaseModel):
    name: str
    description: Optional[str]
    min_price: Optional[float]
    max_price: Optional[float]
    images: List[GiftImagesSchema]
    links: List[GiftLinksSchema]
