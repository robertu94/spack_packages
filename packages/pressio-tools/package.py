from spack import *


class PressioTools(CMakePackage):
    """General Utilities for LibPressio"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/robertu94/pressio-tools"
    git      = "git@github.com:robertu94/pressio-tools"

    # FIXME: Add proper versions here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('libpressio+hdf5')
    depends_on('libdistributed')
    depends_on('boost')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
