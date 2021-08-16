from spack import *


class Libpressio(CMakePackage):
    """A generic abstraction for the compression of dense tensors"""

    homepage = "https://github.com/codarcode/libpressio"
    url      = "https://github.com/robertu94/libpressio/archive/0.31.1.tar.gz"
    git      = "https://github.com/robertu94/libpressio"

    version('master', branch='master')
    version('develop', branch='develop')
    version('0.70.5', sha256='c6ee62643c08a7ceca7c45eb28edff0eeb070671bf0d502563b6cc8ada4bf695')
    version('0.70.4', sha256='6df62154d0a8919fa91f6fce4ffb2f77584d5ddc61c85eee34557d36de9906b2')
    version('0.70.3', sha256='40cca7f6d3bd19fdcf6f6c17521acdf63dfda0fb5b173c23d4521818b16a9a46')
    version('0.70.2', sha256='30929e02c0ce5db8d9ff1eeca42df92e68439c7dd5a3c1fea0bb44ead2343442')
    version('0.70.1', sha256='855923ca58b1c549681d368d2112d05b96fae9e3199f2a10c2013fcb2f630036')
    version('0.70.0', sha256='1e987dcea76b2bd01f7e59b404267c7614a7c99b3fbc0ae745bf8e9426f489c6')
    version('0.69.0', sha256='22e47deb4791778846b9c858295b756f91e1d8c884ccf246c2df2bf9b56a04d5')
    version('0.68.0', sha256='c7008e6f6b4451812070ece7e9b2fb6cc2fb04971255f95c8274375a698c6794')
    version('0.66.3', sha256='7423339831525a128115d446b1dd7fb7942f2aed24e0ec3778396d2c0c379678')
    version('0.66.2', sha256='89a6459b6fcf1273f8afc7317e7351c09be977aeb3bb6554941166074ee2030f')
    version('0.66.1', sha256='1de2d3d911fc91f7aa9f57eda467f1aadd7060a680538b82c678a5f4e7e6c5d0')
    version('0.66.0', sha256='c3063a85c8f17df6ba1722f06eaab74fe14a53f37f5a86664c23a7f35d943f3a')
    version('0.65.0', sha256='beb4f7bc73b746fe68c4333fa4d4e1dba05f5f5fb386874b83cbf7f105e83c45')
    version('0.64.0', sha256='1af87b410eabee7f377b047049eae486cf3161fa67546789440f1d1e56e2324d')
    version('0.63.0', sha256='32d716f52073d7ea246d01fefb420bfe5b834ebc10579edd79ebce7a87dd1a81')
    version('0.62.0', sha256='248eedc764312da401aa29304275e009196ebdb5b08594a1522bb165c16874aa')
    version('0.61.0', sha256='7b4304b7556d8ec0742d1b8a9280f7f788307d2a6f4d2f59cc8e8358b6c69c11')
    version('0.60.0', sha256='a57fce96d50a603075a8a4a583431a1a03170df4d2894ff30f84d8c5ab4caf47')
    version('0.59.0', sha256='eae5933a7b37834cf4f70424b083f99799f9381ee8bb616f3a01d4ab2e5631a6')
    version('0.58.0', sha256='6b092dda66e7cc1bc4842fe54ab41248c4f136307cc955081e8052222c82aff1')
    version('0.57.0', sha256='4f978616c13f311170fdc992610ad1fd727884cf0d20b6849b2c985d936c482b')
    version('0.56.2', sha256='1ae20415ba50a4dcfec7992e9a571f09f075f077ebdd7c1afb9a19b158f6205d')
    version('0.56.1', sha256='01b7c09f1eafff819de0079baf033f75547432be62dc10cb96691d078994a4e9')
    version('0.56.0', sha256='77003c9dde0590ca37fddfbe380b29b9f897fa0dadb9b9f953819f5e9d9f08f0')
    version('0.55.3', sha256='f8c6ae6ae48c4d38a82691d7de219ebf0e3f9ca38ae6ba31a64181bfd8a8c50a')
    version('0.55.2', sha256='47f25f27f4bff22fd32825d5a1135522e61f9505758dde3d093cfbdaff0b3255')
    version('0.55.1', sha256='39f1799d965cd0fec06f0a43dec865c360cbb206e4254f4deb4f7b7f7f3c3b2f')
    version('0.55.0', sha256='fb74cfe2a8f3da51f9840082fa563c2a4ce689972c164e95b1b8a1817c4224cf')
    version('0.54.0', sha256='cd28ddf054446c286f9bfae563aa463e638ee03e0353c0828a9ce44be4ce2df9')
    version('0.53.2', sha256='4a7b57f1fd8e3e85ecf4a481cc907b81a71c4f44cf2c4a506cb37a6513a819a4')
    version('0.53.1', sha256='1425dec7ee1a7ddf1c3086b83834ef6e49de021901a62d5bff0f2ca0c75d3455')
    version('0.53.0', sha256='0afb44c2dab8dd8121d174193eb6623b29da9592e5fe1bbe344cfc9cacbec0cb')
    version('0.52.2', sha256='c642463da0bbdd533399e43c84ea0007b1d7da98276c26bc075c7b4778f97a01')
    version('0.52.1', sha256='32f211aaf4641223bf837dc71ea064931f85aa9260b9c7f379787ca907c78c3a')
    version('0.52.0', sha256='2fd4cf0cc43c363b2e51cb264a919a1b43514aad979b9b5761b746fc70490130')
    version('0.51.0', sha256='878d5399c4789034b7f587a478e2baf8e852f7f1f82aa59e276ddf81d325b934')
    version('0.50.4', sha256='f4ab7dada0e07ecf97f88e2dd7ca6c4755fb0f4175d8d12ed3a856c45b240bde')
    version('0.50.3', sha256='cc78bfc9a5d1b061098c892e9c8ff14861aa48ea95f0e9684ca4250d30c38889')
    version('0.50.2', sha256='0ef1355f905d48ed01c034a8d418e9c528113d65acb3dd31951297029c5aaed4')
    version('0.50.1', sha256='1500bae01ba74c330bc205b57423688c2b1aacafe1aabcaf469b221dcda9beec')
    version('0.50.0', sha256='c50fb77b5c8d535fe0c930e5d4400d039ad567a571ea9711b01d6d5bd2a26fb6')
    version('0.49.2', sha256='cde90e0183024dc1a78d510e2ae3effa087c86c5761f84cba0125f10abc74254')
    version('0.49.1', sha256='6d1952ada65d52d2fd5d4c60bb17e51d264c2c618f9b66dadeffa1e5f849394a')
    version('0.49.0', sha256='adfe5c64a5d170197893fe5a4c9338cde6cbdd5b54e52534886425101be4458f')
    version('0.48.0', sha256='087a7f944240caf2d121c1520a6877beea5d30cc598d09a55138014d7953348a')
    version('0.47.0', sha256='efce0f6f32e00482b80973d951a6ddc47b20c8703bd0e63ab59acc0e339d410b')
    version('0.46.3', sha256='24bc5d8532a90f07ab2a412ea28ddbfc8ff7ab27cd9b4e7bd99a92b2a0b5acfd')
    version('0.46.2', sha256='3ebbafa241e54cb328966ea99eab5d837c4a889f17c3b2048cc2961166a84cc4')
    version('0.46.1', sha256='be7468b30a367bcbefab09ed5ac07320cd323904c9129d6b874175b39ef65cd9')
    version('0.46.0', sha256='ab944358edc7e03be604749002f1f00aaf4d55d20bac2689d40bd4e66357879d')
    version('0.45.0', sha256='b3307b99f82f0300dfed7dd122447a6e74ca8ad8c012d2fc60467e6e067ac226')
    version('0.44.0', sha256='cec114325167731233be294aab329d54862457cb2e1f1a87d42d100da7c53aa5')
    version('0.42.2', sha256='a9289260eb0a4eaf4550c2d6ad1af7e95a669a747ce425ab9a572d4ab80e2c1f')
    version('0.42.1', sha256='5f79487568ec4625b0731f0c10efb565201602a733d1b6ac1436e8934cf8b8ec')
    version('0.42.0', sha256='c08e047e202271ec15eeda53670c6082815d168009f4e993debcc0d035904d6b')
    version('0.41.0', sha256='b789360d70656d99cd5e0ceebfc8828bdf129f7e2bfe6451592a735be9a0809a')
    version('0.40.1', sha256='73a65f17e727191b97dfdf770dd2c285900af05e6fee93aa9ced9eadb86f58ff')
    version('0.40.0', sha256='80e68172eeef0fbff128ede354eaac759a9408c3ef72c5eed871bb9430b960ff')
    version('0.39.0', sha256='e62fea9bcb96529507fdd83abc991036e8ed9aa858b7d36587fce3d559420036')
    version('0.38.2', sha256='5f38387d92338eac8658cd70544a5d9a609bd632090f4f69bcbc9f07ec4abd7b')
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


    variant('blosc', default=False, description='support the blosc lossless compressors')
    variant('fpzip', default=False, description='support for the FPZIP lossy compressor')
    variant('hdf5', default=False, description='support reading and writing from hdf5 files')
    variant('magick', default=False, description='support the imagemagick image compressors')
    variant('mgard', default=False, description='support for the MAGARD error bounded lossy compressor')
    variant('python', default=False, description='build the python wrappers')
    variant('sz', default=False, description='support for the SZ error bounded lossy compressor')
    variant('zfp', default=False, description='support for the ZFP error bounded lossy compressor')
    variant('boost', default=False, description='support older compilers using boost')
    variant('petsc', default=False, description='support IO using petsc format')
    variant('mpi', default=False, description='support for launching processes using mpi')
    variant('lua', default=False, description='support for composite metrics using lua')
    variant('libdistributed', default=False, description='support for distributed multi-buffer support')
    variant('ftk', default=False, description="build support for the feature tracking toolkit")
    variant('digitrounding', default=False, description="build support for the digit rounding")
    variant('bitgrooming', default=False, description="build support for the bitgrooming")
    variant('openmp', default=False, description="build plugins that use openmp")
    variant('docs', default=False, description="build and install manual pages")
    variant('remote', default=False, description="build the remote launch plugin")
    variant('json', default=False, description="build the JSON support")
    variant('szauto', default=False, description="build szauto support")
    variant('unix', default=False, description="build support for unixisms like mmap and rusage")

    depends_on('boost', when="@:0.51.0+boost")
    depends_on('libstdcompat@0.0.7:+boost', when="@0.70.3:+boost")
    depends_on('libstdcompat@0.0.7:', when="@0.70.3:~boost")
    depends_on('libstdcompat@0.0.6:+boost', when="@0.70.2:+boost")
    depends_on('libstdcompat@0.0.6:', when="@0.70.2:~boost")
    depends_on('libstdcompat@0.0.5:+boost', when="@0.63.0:+boost")
    depends_on('libstdcompat@0.0.5:', when="@0.63.0:~boost")
    depends_on('libstdcompat@0.0.3:+boost', when="@0.60.0:+boost")
    depends_on('libstdcompat@0.0.3:', when="@0.60.0:~boost")
    depends_on('libstdcompat+boost', when="@0.52.0:+boost")
    depends_on('libstdcompat', when="@0.52.0:~boost")
    depends_on('c-blosc', when="+blosc")
    depends_on('fpzip', when="+fpzip")
    depends_on('hdf5', when="+hdf5")
    depends_on('imagemagick', when="+magick")
    depends_on('mgard', when="+mgard")
    depends_on('python@3:', when="+python", type=("build", "link", "run"))
    depends_on('py-numpy', when="+python", type=("build", "link", "run"))
    depends_on('swig@3.12:', when="+python", type="build")
    depends_on('sz@2.1.8.1:', when="@0.55.2:+sz")
    depends_on('sz@2.1.11.1:', when="@0.55.3:+sz")
    depends_on('sz@2.1.12:', when="@0.69.0:+sz")
    depends_on('fftw', when="+sz ^sz@:2.1.10")
    depends_on('zfp', when="+zfp")
    depends_on('petsc', when="+petsc")
    depends_on('mpi@2:', when="+mpi")
    depends_on('sol2', when="+lua")
    depends_on('libdistributed@0.0.11:', when="+libdistributed")
    depends_on('pkg-config', type='build')
    depends_on('ftk@master', when="+ftk")
    depends_on('digitrounding', when="+digitrounding")
    depends_on('bitgroomingz', when="+bitgrooming")
    depends_on('cmake@3.14:', type="build")
    depends_on('py-mpi4py', when="@0.54.0:+mpi+python", type=("build", "link", "run"))
    depends_on('py-numcodecs', when="@0.54.0:+python", type="run")
    depends_on('doxygen+graphviz', when="+docs", type="build")
    depends_on('curl', when="+remote")
    depends_on('nlohmann-json~single_header', when="+remote")
    depends_on('nlohmann-json~single_header', when="+json")
    depends_on('szauto', when="+szauto")
    conflicts('~json', when="@0.57.0:+remote", msg="JSON support required for remote after version 0.57.0")

    extends("python", when="+python")

    def cmake_args(self):
        args = []
        if "+python" in self.spec:
            args.append("-DBUILD_PYTHON_WRAPPER=ON")
            args.append("-DPython3_EXECUTABLE={0}".format(self.spec['python'].command))
            if "+mpi" in self.spec:
                args.append("-DLIBPRESSIO_HAS_MPI4PY=ON")
        if "+hdf5" in self.spec:
            args.append("-DLIBPRESSIO_HAS_HDF=ON")
            args.append("-DHDF5_ROOT=" + self.spec['hdf5'].prefix)
        if "+sz" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZ=ON")
        if "+szauto" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZ_AUTO=ON")
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
        if "+libdistributed" in self.spec:
            args.append("-DLIBPRESSIO_HAS_LIBDISTRIBUTED=ON")
        if "+ftk" in self.spec:
            args.append("-DLIBPRESSIO_HAS_FTK=ON")
        if "+bitgrooming" in self.spec:
            args.append("-DLIBPRESSIO_HAS_BIT_GROOMING=ON")
        if "+digitrounding" in self.spec:
            args.append("-DLIBPRESSIO_HAS_DIGIT_ROUNDING=ON")
        if "+openmp" in self.spec:
            args.append("-DLIBPRESSIO_HAS_OPENMP=ON")
        if "+docs" in self.spec:
            args.append("-DBUILD_DOCS=ON")
            args.append("-DLIBPRESSIO_INSTALL_DOCS=ON")
        if "+remote" in self.spec:
            args.append("-DLIBPRESSIO_HAS_REMOTELAUNCH=ON")
        if "+json" in self.spec:
            args.append("-DLIBPRESSIO_HAS_JSON=ON")
        if "+unix" in self.spec:
            args.append("-DLIBPRESSIO_HAS_LINUX=ON")
        if self.run_tests:
            args.append("-DBUILD_TESTING=ON")
        else:
            args.append("-DBUILD_TESTING=OFF")
        return args

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def test(self):
        make('test')

    @run_after('build')
    def install_docs(self):
        if "+docs" in self.spec:
            with working_dir(self.build_directory):
                make('docs')
