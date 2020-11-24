from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = "git@github.com:robertu94/libpressio_opt"

    version('develop', branch='develop')

    depends_on('libpressio@0.40.1:+libdistributed+mpi')
    depends_on('libdistributed@0.0.11:')
    depends_on('dlib')

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

