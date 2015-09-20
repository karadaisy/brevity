#!/usr/bin/env python
from setuptools import setup


setup(name='brevity',
      version='0.2.0',
      description='Tweet shortening utility',
      long_description="""
Brevity
=======

*Brevity is the soul of tweet*

A small utility to shorten https://indiewebcamp.com/note posts to an
acceptable tweet-length summary. Appends an optional permalink or
citation.

Also supports autolinking web addresses in text.

Brevity checks URLs against the full list of ICANN TLDs, to avoid
linking things that look like web addresses but aren't.
""",
      author='Kyle Mahan',
      author_email='kyle@kylewm.com',
      url='http://indiewebcamp.com/brevity',
      py_modules=['brevity'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing',
          'Topic :: Utilities',
      ])
