from spack import *


class LibpressioTools(CMakePackage):
    """General Utilities for LibPressio"""

    homepage = "https://github.com/robertu94/pressio-tools"
    url      = "https://github.com/robertu94/pressio-tools/archive/refs/tags/0.0.15.tar.gz"
    git      = "https://github.com/robertu94/pressio-tools"

    version('master', branch='master')
    version('0.0.19', sha256='cc8a4bb5259b7b8e14248a1a741067a865a0db36645c878d346da983e74c9521')
    version('0.0.18', sha256='766fcf6c4bd475de66107d379c76805d6368d71ee83cade645f2b7cd27801718')
    version('0.0.17', sha256='cf76e8a929aa128d09f8f953171d5cf395223245bc81d2ea4e22099849e40b94')
    version('0.0.16', sha256='1299e441fb15666d1c8abfd40f3f52b1bf55b6bfda4bfcc71177eec37160a95e')
    version('0.0.15', sha256='bcdf865d77969a34e2d747034ceeccf5cb766a4c11bcc856630d837f442ee33e')

    depends_on('mpi', when="+mpi")
    depends_on('libpressio+hdf5+libdistributed+mpi', when="+mpi")

    depends_on('libpressio+hdf5', when="~mpi")

    depends_on('boost')
    depends_on('libpressio-opt', when="+opt")
    depends_on('libpressio-errorinjector', when="+error_injector")
    depends_on('libpressio-tthresh', when="+tthresh")
    depends_on('libpressio-rmetric', when="+rcpp")

    variant("opt", default=False, description="support the libpressio-opt package")
    variant("error_injector", default=False, description="support the libpressio-errorinjector package")
    variant('tthresh', default=False, description="depend on the GPL licensed libpressio-tthresh")
    variant('rcpp', default=False, description="depend on the GPL licensed libpressio-rmetric")
    variant('mpi', default=False, description="depend on MPI for distributed parallelism")

    def cmake_args(self):
        args=[]
        if "+mpi" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_MPI=YES")
        if "+opt" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_OPT=YES")
        if "+error_injector" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_ERROR_INJECTOR=YES")
        if "+tthresh" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_TTHESH=YES")
        if "+rcpp" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_RMETRIC=YES")
        if self.run_tests:
            args.append("-DBUILD_TESTING=ON")
        else:
            args.append("-DBUILD_TESTING=OFF")

        return args

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def test(self):
        make('test')

