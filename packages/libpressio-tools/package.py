from spack import *
from spack.pkg.builtin.libpressio_tools import LibpressioTools as BuiltinLibPressioTools


class LibpressioTools(BuiltinLibPressioTools):
    """Pre-Release: General Utilities for LibPressio"""


    version("0.4.2", sha256="fc5cc2876c0bff2012d51daf5835380afba71061a162d9b29235e639eb94f241")
    version("0.4.1", sha256="c342866ce95167ff708c7b3559c43ee174b7f4e760940f1c145a2fb4b9250c83")
    version("0.4.0", sha256="c68ae3b0e73c7c4fb1562f3515d41a227eb4c0e842eb3106b719afcc1e35a7d9")

    depends_on('libpressio-frsz', when="+frsz")

    variant("frsz", default=False, description="depend on frsz", when="@0.1.2:")

    def cmake_args(self):
        args = super().cmake_args()
        if "+frsz" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_FRSZ=YES")
        return args
