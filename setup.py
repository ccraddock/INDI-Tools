#!/usr/bin/env python
#
# INDI-Tools/setup.py
#
# Author: Daniel Clark, 2016

'''
This is the setup.py installation script to install the awsutils
package
'''

# Import packages
from distutils.core import setup

# Use disutils' setup function to install the package
setup(name='INDI-Tools',
      version='0.0.1',
      description='Python utilities developed by FCP-INDI',
      author='Daniel Clark',
      author_email='daniel.clark@childmind.org',
      url='https://github.com/FCP-INDI/AWSUtils',
      packages=['indi_aws', 'indi_schedulers'])
