from setuptools import setup, find_packages
setup(name='open-platform',
      version='0.1',
      url='https://git.zensoft.io/open-platform/sdk/python',
      author='Eldiiar Egemberdiev',
      author_email='eldiiar.egemberdiev@zensoft.io',
      description='A library for interactions with Open Platform.',
      license=open('LICENSE.txt').read(),
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          "Programming Language :: Python :: 3",
          'Topic :: Software Development :: Libraries',
      ],
      packages=find_packages(exclude=['tests']),
      zip_safe=False,)

