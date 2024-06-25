import traceback
from urllib.parse import parse_qs, urlparse

from helpers.base_entities import BaseScraper
from helpers.parsers import AnnouncementParser
from menzili.templates import (ANNOUNCE_TEMPLATE, PROPERTY_MAPPING,
                               TRANSACTION_MAPPING)


class MenziliScraper(BaseScraper):
    _upload_count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO: Upload all images same time
    def create_image(self, image_path):
        self._upload_count += 1
        url = "https://www.menzili.tn/upload.php"

        print("creating image", image_path)

        image_name = "".join(image_path.split("/")[-1])  # .split('.')[:-1])

        load = self.session.get(image_path).content
        print("load", load[:10])
        print("image name: ", image_name)

        files = {
            f"photo{self._upload_count}": (image_name, load)
        }  # form data with image
        resp = self.session.post(url, files=files)
        print("resp", resp.json())
        content = resp.json()

        return content

    def set_cookies(self, cookies):
        super().set_cookies(cookies)

    def create_announcement(self, extra_data):
        template = ANNOUNCE_TEMPLATE
        print("Creating announcement")
        url = "https://www.menzili.tn/deposer-une-annonce"
        print(f"found image urls: {AnnouncementParser.images_urls}")
        for image in AnnouncementParser.images_urls:
            resp_json = self.create_image(image)
            img_id = resp_json["id_img"]
            ANNOUNCE_TEMPLATE["img_tmp"] += f"\\{img_id}"

        # encoded_image_list = ','.join([f"\"{img}\"" for img in self.image_uploads])

        # TODO: Finishe reset of inputs (currently uses bare info)
        template["pri"] = AnnouncementParser.price
        template["tel"] = AnnouncementParser.phone
        template["tit"] = AnnouncementParser.title
        template["ann"] = AnnouncementParser.description
        template["reg"] = AnnouncementParser.governorate("menzili")
        template["vil"] = AnnouncementParser.delegation("menzili")
        # TODO: Check passed data
        template.update(extra_data)

        data = {
            **template,
        }
        print("Posting menzili with data :: ", data)
        resp = self.session.post(url, data=data)
        return resp

    def confirm_announcement(self, location):
        if not location:
            print("Menzili issue :: No Location found after announcement created")
            return

        try:
            queries = parse_qs(urlparse(location).query)
            id_ann = queries.get("id_ann")[0]
            id_compte = queries.get("id_compte")[0]

            form = {
                "freepack": "0",
                "type_acc": "2",
                "id_ann": id_ann,
                "id_compte": id_compte,
                "relance": "0",  # ?
            }
            self.session().post(location, data=form, allow_redirects=True)
        except Exception as e:
            traceback.print_exception(type(e), e, e.___traceback__)
