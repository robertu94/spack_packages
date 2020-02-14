from spack import *


class Sz(CMakePackage):
    """The SZ Error Bounded Lossy Compressor"""

    homepage = "https://github.com/disheng222/sz"
    git      = "https://github.com/disheng222/sz"

    version('master', branch='master')

    variant('python', default=False, description="builds the python wrapper")
    variant('netcdf', default=False, description="build the netcdf reader")
    variant('hdf5', default=False, description="build the hdf5 filter")
    variant('pastri', default=False, description="build the pastri mode")
    variant('time_compression', default=False, description="build the time based compression mode")
    variant('random_access', default=False, description="build the random access compression mode")
    variant('shared', default=True, description="build shared versions of the libraries")


    depends_on('zlib')
    depends_on('zstd')

    extends('python', when="+python")
    depends_on('python@3:', when="+python")
    depends_on('swig@3.12:', when="+python")
    depends_on('py-numpy', when="+python")
    depends_on('hdf5', when="+hdf5")
    depends_on('netcdf-c', when="+netcdf")

    def cmake_args(self):
        args = []
        if "+python" in  self.spec:
            args.append("-DBUILD_PYTHON_WRAPPER=ON")
        if "+netcdf" in  self.spec:
            args.append("-DBUILD_NETCDF_READER=ON")
        if "+hdf5" in  self.spec:
            args.append("-DBUILD_HDF5_FILTER=ON")
        if "+pastri" in  self.spec:
            args.append("-DBUILD_PASTRI=ON")
        if "+time_compression" in  self.spec:
            args.append("-DBUILD_TIMECMPR=ON")
        if "+random_access" in  self.spec:
            args.append("-DBUILD_RANDOMACCESS=ON")
        if "+shared" in  self.spec:
            args.append("-DBUILD_SHARED_LIBS=ON")
        else:
            args.append("-DBUILD_SHARED_LIBS=OFF")
        return args
