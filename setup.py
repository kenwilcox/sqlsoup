from setuptools import setup, find_packages
import sys
import os
import re

extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
    )

v = open(os.path.join(os.path.dirname(__file__), 'sqlsoup', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')


setup(name='sqlsoup',
      version=VERSION,
      description="A one step database access tool, built on the SQLAlchemy ORM.",
      long_description=open(readme).read(),
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Database :: Front-Ends',
      ],
      keywords='SQLAlchemy ORM',
      author='Mike Bayer',
      author_email='mike@zzzcomputing.com',
      url='http://bitbucket.org/zzzeek/sqlsoup',
      license='MIT',
      packages=find_packages('.', exclude=['test*']),
      include_package_data=True,
      tests_require = ['nose >= 0.11'],
      test_suite = "nose.collector",
      zip_safe=False,
      install_requires=[
          'SQLAlchemy>=0.7.0',
      ],
      **extra
)
