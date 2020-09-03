from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = "git@github.com:robertu94/libpressio_opt"

    version('develop', branch='develop')

    depends_on('libpressio@0.40.1:+hdf5+lua+libdistributed+mpi')
    depends_on('libdistributed@0.0.11:')
    depends_on('dlib')

    variant("test", default=False, description='build the unittests')

    def cmake_args(self):
        args = []
        if "+test" in self.spec:
            args.append("-DBUILD_TESTING=OFF")
        else:
            args.append("-DBUILD_TESTING=ON")
        return args
