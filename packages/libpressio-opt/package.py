from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = "git@github.com:robertu94/libpressio_opt"
    url      = "https://github.com/robertu94/libpressio_opt/archive/refs/tags/0.11.0.tar.gz"

    version('develop', branch='develop')
    version('sdr-develop', branch='develop', git="git@github.com:szcompressor/SDRFramework")
    version('0.13.0', sha256='6a64116dd6727e2dc05840b0e804fcaf82debde09c69e4905197462a769e998e')
    version('0.12.1', sha256='e5d0b4d8b4885dfe555148e23f34e0bc904a898871dea8d412265075f1f8c858')
    version('0.12.0', sha256='5f28f37de858634cf481d911f202360f078902803f82b5f49b7eec9b59948d64')
    version('0.11.0', sha256='cebbc512fcaa537d2af1a6919d6e0400cdc13595d71d9b90b74ad3eb865c9767')

    depends_on('libpressio@0.66.1:+libdistributed+mpi')
    depends_on('libdistributed@0.0.11:')
    depends_on('dlib@19.22:')

    def cmake_args(self):
        args = []
        if self.run_tests:
            args.append("-DBUILD_TESTING=ON")
        else:
            args.append("-DBUILD_TESTING=OFF")
        return args

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def test(self):
        make('test')

