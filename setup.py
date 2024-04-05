from setuptools import setup, find_packages

# Package metadata
NAME = 'youtube_selenium_py'
VERSION = '1.0.6'
DESCRIPTION = "A Python package to create youtube channels, sub channels, upload videos, create community posts, edit channel, delete channel, and so much more."
URL = 'https://github.com/Automa-Automations/youtube_selenium_py'
AUTHOR = 'William Ferns'
AUTHOR_EMAIL = 'business@agnostica.site'
LICENSE = 'MIT'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]
KEYWORDS = ['youtube', 'API', 'video', 'channel', 'upload', 'statistics', 'python', 'development', 'selenium']
PROJECT_URLS = {
    'Bug Reports': 'https://github.com/Automa-Automations/youtube_selenium_py/issues',
    'Source': 'https://github.com/Automa-Automations/youtube_selenium_py',
    'Automa Automations': 'https://github.com/Automa-Automations',
}

# Package requirements
with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

# Package setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    project_urls=PROJECT_URLS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
)
