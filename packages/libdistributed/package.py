from spack import *


class Libdistributed(CMakePackage):
    """a collection of facilities for MPI that create for higher level facilities for programming in C++"""

    homepage = "https://github.com/robertu94/libdistributed"
    url      = "https://github.com/robertu94/libdistributed/archive/0.0.3.tar.gz"
    git      = "https://github.com/robertu94/libdistributed"

    version('master', branch='master')
    version('0.1.0', sha256='e10daa6d4a6dc371057e92d2b706ae16450b41ed7c0d386cffeb68e160f556c1')
    version('0.0.10', sha256='3af4ce81b3ae016e80e401adfcfad856e15a76da4d2a81535cb4bd993c11104b')
    version('0.0.8', sha256='78bc1fbc99e46ea0e03cb181623262be0f527767efd3249baa249cb24b794762')
    version('0.0.7', sha256='b2c65752df7bc55fcdc9a5eb7b36c203667f2fb6382d3eaecdaf1504421d4d7b')
    version('0.0.6', sha256='05ce6ae880aec19f6945ee5f3c2f4099343ca6b555ea6c8e005a48a6e09faf5b')
    version('0.0.5', sha256='09c1e9a0b34371fa8e6f3d50671bcce7fcc3e4c7c26f3e19017b07b64695d199')
    version('0.0.4', sha256='7813980011091822534d196d372b8cb6fdc12d35acd5acb42c6eeeaf10a44490')
    version('0.0.3', sha256='c476b3efe20e1af4c976e89ff81b7eed01ddddae73ac66f005108747facbeff7')
    version('0.0.2', sha256='c25309108fe17021fd5f06ba98386210708158c439e98326e68f66c42875e58a')
    version('0.0.1', sha256='4c23ce0fd70a12ee5f8760ea00377ab6370d86b30ab42476e07453b19ea4ac44')

    depends_on('mpi@2:')
    depends_on('libstdcompat@0.0.2:', when="@0.1.0:")

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

