from spack import *


class LibpressioOpt(CMakePackage):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    homepage = "https://github.com/robertu94/libpressio_opt"
    git      = homepage
    url      = "https://github.com/robertu94/libpressio_opt/archive/refs/tags/0.11.0.tar.gz"

    version('develop', branch='develop')
    version('sdr-develop', branch='develop', git="git@github.com:szcompressor/SDRFramework")
    version("0.13.4", sha256="e9f715d11fe3558a31e1d9a939150209449ec8636ded047cb0adcd3db07569ae")
    version('0.13.3', sha256='98436b7fa6a53dd9cc09a9b978dc81c299501930cb8b844713080fc42d39d173')
    version('0.13.2', sha256='8a16ba23b5078b0ee3a75d8a64ba64b492ecfadc221dd28ae463f4d3f4f7d847')
    version('0.13.1', sha256='a831d326871c183a7e64b2015d687da3f17cf89c2d7d1d6770e3acbc1346aa8c')
    version('0.13.0', sha256='6a64116dd6727e2dc05840b0e804fcaf82debde09c69e4905197462a769e998e')
    version('0.12.1', sha256='e5d0b4d8b4885dfe555148e23f34e0bc904a898871dea8d412265075f1f8c858')
    version('0.12.0', sha256='5f28f37de858634cf481d911f202360f078902803f82b5f49b7eec9b59948d64')
    version('0.11.0', sha256='cebbc512fcaa537d2af1a6919d6e0400cdc13595d71d9b90b74ad3eb865c9767')

    depends_on('libpressio@0.85.0:+libdistributed+mpi', when="@0.13.3:")
    depends_on('libpressio@0.66.1:+libdistributed+mpi', when="@:0.13.2")
    depends_on('libdistributed@0.0.11:')
    depends_on('libdistributed@0.4.0:', when="@0.13.3:")
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

