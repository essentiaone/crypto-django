from setuptools import find_packages, setup


setup(
    name='crypto-django',
    version='0.1.1',
    packages = find_packages(),
    include_package_data=True,
    license='MIT',
    description='',
    url='https://github.com/essentiaone/crypto-django',
    author='Essentia.one developers',
    author_email='dev@essentia.one',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'bit==0.4.3',
        'bitcash==0.5.2',
        'Django==2.1.1',
        'eth-utils==1.2.1',
        'eth-hash[pycryptodome]',
    ],
)
