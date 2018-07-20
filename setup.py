from setuptools import setup, find_packages

setup(name='open-platform',

      version='0.1',

      # url needs to be discussed
      url='https://github.com/OpenFuturePlatform/open-api-python-sdk',

      author='openfuture.io',

      author_email='eldiiar.egemberdiev@zensoft.io',

      description='A library for interactions with Open Platform.',

      license=open('LICENSE.txt').read(),

      long_description=open('README.md').read(),

      long_description_content_type="text/markdown",

      classifiers=[

          'Development Status :: 2 - Pre-Alpha',

          'Intended Audience :: Developers',

          "Programming Language :: Python",

          "Programming Language :: Python :: 3",

          "Operating System :: OS Independent",

          'Topic :: Software Development :: Libraries :: Python Modules',

      ],

      packages=find_packages(),

      setup_requires=['requests'],

      zip_safe=False, )
