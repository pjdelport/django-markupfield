from setuptools import setup

long_description = open('README.rst').read()

setup(
    name='django-markupfield',
    version="2.0.0-dev",
    package_dir={'markupfield': 'markupfield'},
    packages=['markupfield', 'markupfield.tests'],
    package_data={'markupfield': ['locale/*/*/*']},
    description='Custom Django field for easy use of markup in text fields',
    author='James Turk',
    author_email='dev@jamesturk.net',
    license='BSD License',
    url='https://github.com/jamesturk/django-markupfield/',
    long_description=long_description,
    platforms=["any"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
    ],
)
