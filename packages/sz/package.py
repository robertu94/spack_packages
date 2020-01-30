from spack import *


class Sz(CMakePackage):
    """The SZ Error Bounded Lossy Compressor"""

    homepage = "https://github.com/disheng222/sz"
    git      = "https://github.com/disheng222/sz"

    version('master', branch='master')

    variant('python', default=False, description="builds the python wrapper")


    depends_on('zlib')
    depends_on('zstd')

    extends('python', when="+python")
    depends_on('python@3:', when="+python")
    depends_on('swig@3.12:', when="+python")
    depends_on('py-numpy', when="+python")

    def cmake_args(self):
        args = []
        if "+python" in  self.spec:
            args.append("-DBUILD_PYTHON_WRAPPER=ON")
        return args
