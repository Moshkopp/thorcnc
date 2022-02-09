from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="thorcnc",
    version="0.0.1",
    author="John Doe",
    author_email="<doe.john@example.com>",
    description="ThorCNC - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/USERNAME/REPO",
    download_url="https://github.com/USERNAME/REPO/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'thorcnc=thorcnc:main',
        ],
        'qtpyvcp.vcp': [
            'thorcnc=thorcnc',
        ],
    },
)
