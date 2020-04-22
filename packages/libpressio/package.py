from spack import *


class Libpressio(CMakePackage):
    """A generic abstraction for the compression of dense tensors"""

    homepage = "https://github.com/codarcode/libpressio"
    url      = "https://github.com/robertu94/libpressio/archive/0.31.1.tar.gz"
    git      = "https://github.com/robertu94/libpressio"

    version('master', branch='master')
    version('0.38.1', sha256='99ff1ff61408e17f67ab427c51add074f66ab7375a506ae70dcb24c47a8ea636')
    version('0.38.0', sha256='e95aa6e4161324fa92fa236ea2bf08a7267a883ef4ca5fbb8bbf75e70db1ce4f')
    version('0.37.0', sha256='98877fa2daf91ac91c2e0e0014684131d6efc4a1f2f77917d40fdbf424d74588')
    version('0.36.0', sha256='452a3973cf359786409e064ca4b63a5f81072a9d72a52d1a4084d197f21fc26b')
    version('0.35.0', sha256='50e6de305e1ffdcf423cec424e919bb0bdebee6449d34ff26a40421f09392826')
    version('0.34.4', sha256='5a997c6f4b8c954a98046a851d0f3b31ce7c5be6e7e615068df4f1d7b86c9630')
    version('0.34.3', sha256='1f5994862c33df4588d411b49fba20a40294627d0b325bbd5234f169eb1d4842')
    version('0.34.2', sha256='3b8d3f801799023c8efe5069895723ce4e742330282774dc0873c2fa3910eeb2')
    version('0.34.1', sha256='791ff249a685fab1733d4c3c936db6a064aa912d47926ad4bd26b1829f6e2178')
    version('0.34.0', sha256='da62a15da103e763e34dae43be3436873e4fb550630dddc55232ae644accda02')
    version('0.33.0', sha256='61200855a0846ce765b686fa368496f44534e633031811803ba2cb31f94c25b1')
    version('0.32.0', sha256='187e75fc6d3f84003829d2b8aec584e99d72d65f2d82835998714ae05ae008af')
    version('0.31.1', sha256='32c1fd8319fbbb844a0a252d44761f81f17c6f3549daadce47e81524d84605a4')
    version('0.31.0', sha256='9d4bc8b2c1a210a58f34216cebe7cd5935039d244b7e90f7e2792bda81ff7ddc')
    version('0.30.1', sha256='e2249bdced68d80a413de59f8393922553a8900a14e731030e362266e82a9af8')
    version('0.30.0', sha256='91de53099d9381e3744e7a1ac06d2db0f9065378c4d178328b78ac797ee3ec65')
    version('0.29.1', sha256='ced1e98fbd383669e59ec06d2e0c15e27dbceda9ac5569d311c538b2fe6d3876')
    version('0.29.0', sha256='a417a1d0ed75bd51131b86fba990502666d8c1388ad6282b3097aa461ccf9785')
    version('0.28.0', sha256='5c4e0fe8c7c80615688f271b57b35ee9d924ac07c6d3d56d0303e610338ed332')
    version('0.27.1', sha256='3f7d2401ff8b113781d93c5bf374f47ca35b2f962634c6310b73620da735e63d')
    version('0.27.0', sha256='387ee5958de2d986095cda2aaf39d0bf319d02eaeeea2a565aea97e6a6f31f36')
    version('0.26.0', sha256='c451591d106d1671c9ddbb5c304979dd2d083e0616b2aeede62e7a6b568f828c')


    variant('blosc', default=True, description='support the blosc lossless compressors')
    variant('fpzip', default=True, description='support for the FPZIP lossy compressor')
    variant('hdf5', default=True, description='support reading and writing from hdf5 files')
    variant('magick', default=True, description='support the imagemagick image compressors')
    variant('mgard', default=True, description='support for the MAGARD error bounded lossy compressor')
    variant('python', default=False, description='build the python wrappers')
    variant('sz', default=True, description='support for the SZ error bounded lossy compressor')
    variant('zfp', default=True, description='support for the ZFP error bounded lossy compressor')
    variant('boost', default=False, description='support older compilers using boost')
    variant('petsc', default=True, description='support IO using petsc format')
    variant('mpi', default=True, description='support for launching processes using mpi')
    variant('lua', default=True, description='support for composite metrics using lua')

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
    depends_on('petsc', when="+petsc")
    depends_on('mpi@2:', when="+mpi")
    depends_on('sol2', when="+lua")

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
        if "+petsc" in self.spec:
            args.append("-DLIBPRESSIO_HAS_PETSC=ON")
        if "+boost" in self.spec:
            args.append("-DLIBPRESSIO_CXX_VERSION=11")
        if "+mpi" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MPI=ON")
        if "+lua" in self.spec:
            args.append("-DLIBPRESSIO_HAS_LUA=ON")



        return args
