from setuptools import find_packages, setup


setup(
    name='crypto-django',
    version='0.1.0',
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
)
