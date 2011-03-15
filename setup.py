#-*- coding:utf-8 -*-
import setuptools

version = '0.0.1'

setuptools.setup(
    name='omoikane',
    packages=['omoikane'],
    install_requires=[
        'sqlalchemy',
        'elixir',
        'pylons',
        'paste',
        'zptutils',
        'wsgilib',
        ],
    version=version)

