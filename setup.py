
from setuptools import setup

setup(
	name = "wepy",
	version='1.0',
	description='weather script for python - wepy',
	url='https://github.com/bradley101/wepy',
	author='Shantanu Banerjee',
	author_email="shantanu.banerjee.vt@gmail.com",
	license='MIT',
	packages=['wepy'],
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
			"wepy=wepy.wepy:main"
		]
	}
	)
