import tempfile

from presents.exporters.base import BaseExporter
from openpyxl import Workbook


class XlsxExporter(BaseExporter):

    def _create_file(self, filename):
        gifts = self.get_gifts()
        wb = Workbook()
        ws = wb.active

        # заголовки
        headers = ["Название", "Описание", "Минимальная цена", "Максимальная цена", "Ссылки"]
        ws.append(headers)

        for gift in gifts:
            gift_row = [gift.name, gift.description, gift.min_price, gift.max_price]
            # собираем все ссылки
            for link in gift.links:
                gift_row.append(link.link)

            ws.append(gift_row)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx', prefix=filename) as tmpfile:
            wb.save(tmpfile.name)
            return tmpfile.name

    def export(self):
        created_filename = self._create_file(self.get_filename())
        return created_filename
