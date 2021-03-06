from pecan import conf, expose
import requests

from pulpito.controllers.util import prettify_run
from urllib.parse import urljoin

base_url = conf.paddles_address


class QueueController(object):
    @expose('index.html')
    def index(self):
        url = urljoin(base_url, '/runs/queued/')
        resp = requests.get(url)
        runs = resp.json()
        for run in runs:
            prettify_run(run)
        return dict(
            title="The Queue",
            runs=runs,
        )


