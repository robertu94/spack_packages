from spack import *


class Mgard(CMakePackage):
    """MGARD error bounded lossy compressor"""

    homepage = "https://github.com/CODARcode/MGARD"
    git      = "https://github.com/CODARcode/MGARD"

    version('master', branch='master')
    version('2020-10-01', commit="b67a0ac")

    depends_on("zlib")
    depends_on("zstd")

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING=OFF"
        ]
        return args
