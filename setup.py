#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
	name = 'bambu-attachments',
	version = '2.0.1',
	description = 'A setup for handling generic model attachments',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-attachments',
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	install_requires = ['Django>=1.4'],
	packages = [
		'bambu_attachments',
		'bambu_attachments.migrations',
		'bambu_attachments.templatetags'
	],
	package_data = {
		'bambu_attachments': [
			'templates/attachments/*.html'
		]
	},
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)
