from setuptools import setup

try:
    import pypandoc
    description = pypandoc.convert(source='README.md', format='markdown_github', to='rst', outputfile='README.rst')
except (IOError, ImportError):
    description = open('README.md').read()


version = '0.1'

setup(
    name='shuiyuan',
    packages=['shuiyuan'],
    version=version,
    description='small package description',
    long_description=description,
    author='jason',
    author_email='dengyongqing@aliyun.com',
    url='https://github.com/dengyongqing/shuiyuan',
    download_url='https://github.com/dengyongqing/shuiyuan/archive/{}.tar.gz'.format(version),
    keywords=['key1', 'key2', 'key3'],
    license='MIT',
    classifiers=[ # look here https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
    ],
    install_requires=[
        'selenium'
    ],
)