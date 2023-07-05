import re

from cavatn.templates import (ANNOUNCE_TEMPLATE, PROPERTY_MAPPING,
                              TRANSACTION_MAPPING)
from helpers.base_entities import BaseScraper
from helpers.parsers import AnnouncementParser


class TunisieAnnonceScraper(BaseScraper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO: Upload all images same time
    def create_image(self, image_path):
        print("creating image", image_path)
        url = "https://www.cava.tn/products/startfileupload/"
        image_name = "".join(image_path.split("/")[-1])  # .split('.')[:-1])

        load = self.session.get(image_path).content
        print("load", load)
        print("image name: ", image_name)

        files = {"images[]": (image_name, load)}  # form data with image
        resp = self.session.post(url, files=files)
        print("resp", resp.text)
        expr = "/media/item/tmp/(\w+.\w+)"  # find out expression
        res = re.search(expr, resp.text)
        up_name = res.group(1)
        self.image_uploads.append(up_name)
        return up_name

    def set_cookies(self, cookies):
        super().set_cookies(cookies)

    def create_announcement(self):
        print("Createing announcement")
        url = "https://www.cava.tn/products/create"
        print(f"found image urls: {AnnouncementParser.images_urls}")
        for image in AnnouncementParser.images_urls:
            self.create_image(image)

        encoded_image_list = ",".join([f'"{img}"' for img in self.image_uploads])

        template = ANNOUNCE_TEMPLATE
        template["Products[subCategory]"] = PROPERTY_MAPPING[
            AnnouncementParser.property_type
        ]
        template["Products[attributes][17]"] = AnnouncementParser.surface
        template["Products[attributes][21]"] = AnnouncementParser.pieces
        template["Products[attributes][22]"] = AnnouncementParser.baths or 1
        template["Products[attributes][40]"] = TRANSACTION_MAPPING[
            AnnouncementParser.vocation
        ]
        template["Products[price]"] = AnnouncementParser.price
        template["Products[product_phone]"] = AnnouncementParser.phone

        data = {
            **template,
            "uploadedfiles": f"[{encoded_image_list}]",
        }
        resp = self.session.post(url, data=data)
        return resp
