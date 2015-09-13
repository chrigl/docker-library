from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.chrigl.viewlets',
      version=version,
      description="Viewlets for plonetheme.chrigl",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Christoph Glaubitz',
      author_email='chris@chrigl.de',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme', 'plonetheme.chrigl'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plonetheme.chrigl',
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=['PasteScript'],
      paster_plugins=['ZopeSkel'],
      )
