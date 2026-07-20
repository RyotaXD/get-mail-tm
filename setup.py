from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name="get-mail-tm",
	version="0.1.0",
	author="Bayu Putra Tama",
	description="Temp mail generator using mail.tm API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	install_requires=[
		"requests"
	],
	python_requires='>=3.6',
)
