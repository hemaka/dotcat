import sys
from setuptools import setup, find_packages

requirements = ['Flask', 'Flask-RESTful']
if sys.version_info[:2] < (2, 6):
    requirements.append('simplejson')

setup(
    name='dotcat',
    version='0.0.1',
    url='https://github.com/hemaka/dotcat.git',
    license='BSD',
    author='Jim He',
    author_email='hemaka@gmail.com',
    description='Test api for flask',
    packages=find_packages(),
    package_data = {
        'dotcat': [
            'static/*/*.css',
            'static/*/*.js',
            'static/*/*.gif',
            'static/*/*.png',
            'templates/*.html',
            'templates/*/*.html',
            'templates/*/*/*.html',
            'tests/*.html',
            'tests/*/*.html',
        ],
    },
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='runtests.runtests',
)