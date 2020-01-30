from spack import *


class Fpzip(CMakePackage):
    """fpzip compressor"""

    homepage = "https://github.com/llnl/fpzip"
    git      = "https://github.com/llnl/fpzip"

    version('master', branch='master')
