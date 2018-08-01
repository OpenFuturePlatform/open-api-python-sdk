from setuptools import setup, find_packages

setup(name='open-api-sdk',

      version='${VERSION}',

      # url needs to be discussed
      url='https://github.com/OpenFuturePlatform/open-api-python-sdk',

      author='OPEN Platform',

      author_email='openplatform@zensoft.io',

      description='SDK library for interactions with Open Platform.',

      license='MIT licence',

      long_description=open('README.md').read(),

      long_description_content_type="text/markdown",

      classifiers=[

          "Programming Language :: Python :: 3",

          "Operating System :: OS Independent",

          'Topic :: Software Development :: Libraries :: Python Modules',

          'License :: OSI Approved :: MIT License',
      ],

      packages=find_packages(),

      install_requires=['requests'],

      zip_safe=False, )
