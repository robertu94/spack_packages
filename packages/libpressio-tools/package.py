from spack import *


class LibpressioTools(CMakePackage):
    """General Utilities for LibPressio"""

    homepage = "https://github.com/robertu94/pressio-tools"
    git      = "git@github.com:robertu94/pressio-tools"

    version('master', branch='master')

    depends_on('libpressio+hdf5+lua')
    depends_on('libdistributed')
    depends_on('libpressio-opt')
    depends_on('boost')
