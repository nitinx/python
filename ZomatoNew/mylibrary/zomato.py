import json
import logging
from mylibrary.http import BaseHTTPClient


log = logging.getLogger(__name__)


class ZomatoClient(BaseHTTPClient):
    
    def __init__(self, user_key):
        super(ZomatoClient, self).__init__(
            "https://developers.zomato.com/api/v2.1",
            headers={"user-key": user_key}
        )

    def get_categories(self):
        return self.get("/categories")


class SuperiorZomatoClient(ZomatoClient):

    def __init__(self, *args, **kwargs):
        super(SuperiorZomatoClient, self).__init__(*args, **kwargs)

    def get_categories(self):
        log.debug("Calling get_categories method.")
        raw_categories = super(SuperiorZomatoClient, self).get_categories()
        refined = {}
        for cat in raw_categories["categories"]:
            _id = cat["categories"]["id"]
            _name = cat["categories"]["name"]
            refined[_id] = _name
        log.info("Result is: {}".format(
            json.dumps(refined, indent=4, sort_keys=True)
        ))
        return refined
