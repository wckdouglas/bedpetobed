import pyximportcpp
pyximportcpp.install(setup_args={
            'include_dirs': ['include/']
        })
from filter_bed import *
