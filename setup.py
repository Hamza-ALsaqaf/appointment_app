from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in appointment_app/__init__.py
from appointment_app import __version__ as version

setup(
	name="appointment_app",
	version=version,
	description="Appointment Web Portal",
	author="Hamza H. Alsaqaf",
	author_email="hamza1alsaqaf@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
