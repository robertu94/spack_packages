from spack import *


class Libpressio(CMakePackage):
    """A generic abstraction for the compression of dense tensors"""

    homepage = "https://github.com/codarcode/libpressio"
    git      = "https://github.com/codarcode/libpressio"

    version('master', branch='master')

    variant('blosc', default=True, description='support the blosc lossless compressors')
    variant('fpzip', default=True, description='support for the FPZIP lossy compressor')
    variant('hdf5', default=True, description='support reading and writing from hdf5 files')
    variant('magick', default=True, description='support the imagemagick image compressors')
    variant('mgard', default=True, description='support for the MAGARD error bounded lossy compressor')
    variant('python', default=False, description='build the python wrappers')
    variant('sz', default=True, description='support for the SZ error bounded lossy compressor')
    variant('zfp', default=True, description='support for the ZFP error bounded lossy compressor')
    variant('boost', default=False, description='support older compilers using boost')

    depends_on('boost', when="+boost")
    depends_on('c-blosc', when="+blosc")
    depends_on('fpzip', when="+fpzip")
    depends_on('hdf5', when="+hdf5")
    depends_on('imagemagick', when="+magick")
    depends_on('mgard', when="+mgard")
    depends_on('python@3:', when="+python")
    depends_on('swig@3.12:', when="+python", type="build")
    depends_on('sz', when="+sz")
    depends_on('zfp', when="+zfp")

    def cmake_args(self):
        args = []
        if "+python" in self.spec:
            args.append("-DBUILD_PYTHON_WRAPPERS=ON")
        if "+hdf5" in self.spec:
            args.append("-DLIBPRESSIO_HAS_HDF=ON")
        if "+sz" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZ=ON")
        if "+zfp" in self.spec:
            args.append("-DLIBPRESSIO_HAS_ZFP=ON")
        if "+fpzip" in self.spec:
            args.append("-DLIBPRESSIO_HAS_FPZIP=ON")
        if "+blosc" in self.spec:
            args.append("-DLIBPRESSIO_HAS_BLOSC=ON")
        if "+magick" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MAGICK=ON")
        if "+mgard" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MGARD=ON")
        if "+boost" in self.spec:
            args.append("-DLIBPRESSIO_CXX_VERSION=11")


        return args
