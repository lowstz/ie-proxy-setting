# _*_ coding: utf-8 _*_

from distutils.core import setup
import py2exe

setup(
	zipfile = None,
    options = {
        'py2exe': {
            'optimize': 2, 
            'bundle_files': 1,
            'includes' : [],
        }
    }, 
    console=['ie_setting.py']
) 