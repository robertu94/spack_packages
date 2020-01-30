from spack import *


class Mgard(CMakePackage):
    """MGARD error bounded lossy compressor"""

    homepage = "https://github.com/CODARcode/MGARD"
    git      = "https://github.com/CODARcode/MGARD"

    version('master', branch='master')

    def cmake_args(self):
        args = []
        return args
