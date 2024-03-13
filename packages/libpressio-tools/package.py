from spack import *
from spack.pkg.builtin.libpressio_tools import LibpressioTools as BuiltinLibPressioTools


class LibpressioTools(BuiltinLibPressioTools):
    """Pre-Release: General Utilities for LibPressio"""


    version("0.4.6", sha256="b1253d49bd16669c41332146e3c441f5a6363cad73262e91a945831ec2bc76e0")
    version("0.4.5", sha256="4f296e4b31f6880f388cb95823864f2c76244e40bb6a94d7918234d189f799ed")
    version("0.4.4", sha256="edbff72b0dba11b145b4d61d507b869ef976c5a8941afb817a533b923a9d7a41")
    version("0.4.3", sha256="2122e2c5212325a54bb6a80f4b7fb56060a1d2d0fa5733ac5757109ea892c9f9")
    version("0.4.2", sha256="fc5cc2876c0bff2012d51daf5835380afba71061a162d9b29235e639eb94f241")
    version("0.4.1", sha256="c342866ce95167ff708c7b3559c43ee174b7f4e760940f1c145a2fb4b9250c83")
    version("0.4.0", sha256="c68ae3b0e73c7c4fb1562f3515d41a227eb4c0e842eb3106b719afcc1e35a7d9")

    depends_on('libpressio-frsz', when="+frsz")
    depends_on('libpressio-adios1@0.0.2:', when="+adios1")
    depends_on('lc-framework@1.1.1:+libpressio', when="+lc")
    depends_on('dctz@0.2.2:+libpressio', when="+dctz")
    depends_on('libpressio-predict@0.0.4:', when="+predict")
    depends_on('libpressio-dataset@0.0.8:', when="+dataset")
    depends_on('libpressio-jit@0.0.1:', when="+jit")

    variant("frsz", default=False, description="depend on frsz", when="@0.1.2:")
    variant("adios1", default=False, description="depend on adios1", when="@0.4.3:")
    variant("lc", default=False, description="depend on lc", when="@0.4.4:")
    variant("dctz", default=False, description="depend on dctz", when="@0.4.5:")
    variant("dataset", default=False, description="depend on libpressio-dataset", when="@0.4.6:")
    variant("predict", default=False, description="depend on libpressio-predict", when="@0.4.6:")
    variant("jit", default=False, description="depend on libpressio-jit", when="@0.4.6:")

    def cmake_args(self):
        args = super().cmake_args()
        if "+dctz" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_DCTZ=YES")
        if "+frsz" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_FRSZ=YES")
        if "+adios1" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_ADIOS1=YES")
        if "+lc" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_LC=YES")
        if "+predict" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_PREDICT=YES")
        if "+jit" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_JIT=YES")
        if "+dataset" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_DATASET=YES")
        return args
