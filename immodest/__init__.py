# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
immodest - Image Model Estimator

Universal modelling of galaxy structure in arbitrary sets of image data

This aims to be an Astropy affiliated package.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    from example_mod import *
