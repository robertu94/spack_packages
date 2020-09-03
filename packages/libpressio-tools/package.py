from spack import *


class LibpressioTools(CMakePackage):
    """General Utilities for LibPressio"""

    homepage = "https://github.com/robertu94/pressio-tools"
    git      = "git@github.com:robertu94/pressio-tools"

    version('master', branch='master')

    depends_on('mpi')
    depends_on('libpressio+hdf5+lua+libdistributed+mpi')
    depends_on('libdistributed')
    depends_on('boost')
    depends_on('libpressio-opt', when="+opt")
    depends_on('libpressio-errorinjector', when="+error_injector")

    variant("opt", default=False, description="support the libpressio-opt package")
    variant("error_injector", default=False, description="support the libpressio-errorinjector package")
    variant("test", default=False, description="build the unittests")

    def cmake_args(self):
        args=[]
        if "+opt" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_OPT=YES")
        if "+error_injector" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_ERROR_INJECTOR=YES")
        if "+test" in self.spec:
            args.append("-DBUILD_TESTING=ON")
        else:
            args.append("-DBUILD_TESTING=OFF")

        return args
