from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = "git@github.com:robertu94/libpressio_opt"
    url      = "https://github.com/robertu94/libpressio_opt/archive/refs/tags/0.11.0.tar.gz"

    version('develop', branch='develop')
    version('0.11.0', sha256='cebbc512fcaa537d2af1a6919d6e0400cdc13595d71d9b90b74ad3eb865c9767')

    depends_on('libpressio@0.66.1:+libdistributed+mpi')
    depends_on('libdistributed@0.0.11:')
    depends_on('dlib@19.22:')

    def cmake_args(self):
        args = []
        if self.run_tests:
            args.append("-DBUILD_TESTING=OFF")
        else:
            args.append("-DBUILD_TESTING=ON")
        return args

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def test(self):
        make('test')

