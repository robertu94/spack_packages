from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = "git@github.com:robertu94/libpressio_opt"

    version('develop', branch='develop')

    depends_on('libpressio@0.40.1:+hdf5+lua')
    depends_on('libdistributed@0.0.10')
    depends_on('dlib')

    def cmake_args(self):
      return ["-DBUILD_TESTING=OFF"]
