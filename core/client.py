import logging

import deepdiff
import requests
from hamcrest import assert_that, equal_to

logging.basicConfig(level=logging.DEBUG)


class ApiClient(object):
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _build_url(self, url):
        logging.debug(f"Request url: {self.base_url}/{url}")
        return f"{self.base_url}/{url}"

    def get(self, url, headers=None, cookies=None):
        return ApiResponse(self.session.get(self._build_url(url), headers=headers, cookies=cookies))

    def post(self, url, body, headers=None, cookies=None):
        return ApiResponse(self.session.post(self._build_url(url), json=body, headers=headers, cookies=cookies))


class ApiResponse(object):
    def __init__(self, response):
        self._response = response

    def body(self):
        return self._response.json()

    def check_status(self, status_code):
        logging.info("About to check " + str(self._response.status_code))
        assert_that(self._response.status_code, equal_to(status_code))

    def exact_body(self, expected_body, ignore=None):
        resp = self.body()
        diff = deepdiff.DeepDiff(resp, expected_body, exclude_paths=ignore)
        if diff:
            logging.info(diff.to_json())
            assert_that(diff.to_json(), equal_to({}))
