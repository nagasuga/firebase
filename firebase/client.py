import json

import requests


class Firebase(object):
    def __init__(self, url, auth_token=None):
        self.url = url

    def _call(self, url, method, headers=None, params=None, data=None):
        print('')
        print('Firebase.call')
        print('    ==>', url)
        print('')
        return requests.request(method=method, url=url, params=params, data=data)

    def make_path(self, *paths):
        """Returns the full path from positional arguments to allow
        generated path rather than having full path."""

        return '/' + '/'.join(paths)

    def _full_url(self, path):
        return self.url + path + '.json'

    def get(self, path, params=None):
        url = self._full_url(path)
        return self._call(url, method='GET', params=params)

    def put(self, path, data):
        url = self._full_url(path)
        return self._call(url, method='PUT', data=json.dumps(data))

    def post(self, path, data):
        url = self._full_url(path)
        return self._call(url, method='post', data=json.dumps(data))

    def delete(self, path):
        url = self._full_url(path)
        return self._call(url, method='delete')

    def patch(self, path, data):
        """We can update specific children at a location without
        overwriting existing data using a PATCH request. Named
        children in the data being written with PATCH will be
        overwritten, but omitted children will not be deleted."""

        url = self._full_url(path)
        return self._call(url, method='PUT', data=json.dumps(data))
