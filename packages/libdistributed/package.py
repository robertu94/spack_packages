from spack import *


class Libdistributed(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/robertu94/libdistributed"
    git      = "https://github.com/robertu94/libdistributed"

    # FIXME: Add proper versions here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
