from distutils.core import setup, Extension
try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
except ImportError:
    raise ImportError("Requires cython to "
            "be installed before running setup.py (pip install cython)")
try:
    import numpy as np
except ImportError:
    raise ImportError("Requires numpy to "
            "be installed before running setup.py (pip install numpy)")
try:
    import pybedtools
except ImportError:
    raise ImportError("Requires pybedtools to "
            "be installed before running setup.py (pip install numpy)")

setup(
    name='bedpetobed',
    version='0.1',
    description='parsing bedpe file and make bed file from that',
    url='',
    author='Douglas Wu',
    author_email='wckdouglas@gmail.com',
    license='MIT',
    packages=['bedpetobed'],
    zip_safe=False,
    scripts = ['bin/bedpe_to_bed.py'],
    ext_modules = cythonize([Extension('bedpetobed.filter_bed',
                                    ['bedpetobed/filter_bed.pyx'],
                                    include_dirs = [np.get_include(),'./include'],
                                    libraries = ["stdc++", 'z'],
                                    extra_compile_args=['-libstdc++'])],
                                    language="c++"),
    install_requires=[
          'cython',
          'numpy',
          'pybedtools'
      ],
    cmdclass = {'build_ext': build_ext}
)
