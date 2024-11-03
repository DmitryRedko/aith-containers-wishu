from abc import ABC, abstractmethod
from typing import List

from presents.models import Gift, PresentsList
from presents.exporters.schemas import GiftSchema, GiftLinksSchema, GiftImagesSchema


class BaseExporter(ABC):
    def __init__(self, list_id):
        self.list_id = list_id

    def get_filename(self):
        list = PresentsList.objects.get(id=self.list_id)
        return list.name

    def get_gifts(self) -> List[GiftSchema]:
        gifts = Gift.objects.filter(list_id=self.list_id).prefetch_related('images', 'links')
        items = []
        for gift in gifts:

            links = []
            for link in gift.links.all():
                links.append(
                    GiftLinksSchema(link=link.link)
                )

            images = []
            for image in gift.images.all():
                images.append(
                    GiftImagesSchema(image=image.image.url)
                )

            items.append(GiftSchema(
                id=gift.id,
                name=gift.name,
                description=gift.description,
                min_price=gift.min_price,
                max_price=gift.max_price,
                images=images,
                links=links,
            ))

        return items

    @abstractmethod
    def export(self):
        """
        Экспорт списка подарков
        :return:
        """