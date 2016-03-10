from setuptools import setup

setup(
    name='django-babik-shadow-accounts',
    version='0.1.0',
    description='Provides shadow accounts',
    author='Aubrey Stark-Toller',
    author_email='aubrey@deepearth.uk',
    license='BSD',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='project django',
    packages=['babik_shadow_accounts'],
    install_requires = ['django>=1.8,<.10'],
    tests_require = ['pytest', 'pytest-django', 'pytest-cov',],
    setup_requires = ['pytest-runner']
)
