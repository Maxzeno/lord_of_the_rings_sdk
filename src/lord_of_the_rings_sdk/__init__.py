import requests

class LordOfTheRings:
	""" SDK for Lord of the rings api """
	def __init__(self, token=None, base_url='https://the-one-api.dev/v2'):
		self.base_url = base_url
		if token is not None:
			self.res = self.set_session(token)
		else:
			self.res = requests

	def set_session(self, token):
		""" sets session """
		session = requests.session()
		session.headers = {'authorization': f'Bearer {token}'}
		return session

	def _base_request(self, path, the_id=None, extra_path='', limit='', page='', offset='', sort='', filter='', *args, **kwargs):
		""" creates the request"""
		all_params = self.parameters(limit, page, offset, sort, filter)
		if the_id is None:
			url = f'{self.base_url}/{path}{all_params}'
			resp = self.res.get(url, *args, **kwargs)
		else:
			url = f'{self.base_url}/{path}/{the_id}/{extra_path}{all_params}'
			resp = self.res.get(url, *args, **kwargs)
		return resp

	def parameters(self, limit, page, offset, sort, filter):
		""" Url parameter """
		all_params = f'limit={limit}' if limit is not '' else ''
		if all_params and page is not '':
			all_params = f'{all_params}&page={page}'

		if all_params and offset is not '':
			all_params = f'{all_params}&offset={offset}'

		if all_params and sort is not '':
			all_params = f'{all_params}&sort={sort}'

		if all_params and filter is not '':
			all_params = f'{all_params}&{filter}'

		all_params = f'?{all_params}' if all_params is not '' else all_params
		return all_params

	def book(self, *args, **kwargs):
		""" Returns books. If the_id is given returns a specific book"""
		path = 'book'
		return self._base_request(path, *args, **kwargs)

	def movie(self, *args, **kwargs):
		""" Returns movie. If the_id is given returns a specific book"""
		path = 'movie'
		return self._base_request(path, *args, **kwargs)

	def character(self, *args, **kwargs):
		""" Returns character. If the_id is given returns a specific book"""
		path = 'character'
		return self._base_request(path, *args, **kwargs)

	def quote(self, *args, **kwargs):
		""" Returns quote. If the_id is given returns a specific book"""
		path = 'quote'
		return self._base_request(path, *args, **kwargs)

	def chapter(self, *args, **kwargs):
		""" Returns chapter. If the_id is given returns a specific book"""
		path = 'chapter'
		return self._base_request(path, *args, **kwargs)