
from setuptools import setup

setup(
	name = "weatherpy",
	version='1.0',
	description='weather script for python weatherpy',
	url='https://github.com/bradley101/weatherpy',
	author='Shantanu Banerjee',
	author_email="shantanu.banerjee.vt@gmail.com",
	license='MIT',
	packages=['weatherpy'],
	install_requires=[
		'urllib',
		'urllib2',
		'json',
		'os',
		'sys',
		'datetime'		
	],
	entry_points={
		"console_scripts": [
			"weatherpy=weatherpy.weatherpy:main"
		]
	}
	)
