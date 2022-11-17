from spack import *
from spack.pkg.builtin.libpressio_tools import LibpressioTools as BuiltinLibPressioTools


class LibpressioTools(BuiltinLibPressioTools):
    """Pre-Release: General Utilities for LibPressio"""
    version("0.2.0", sha256="75048950f0dfa0e20f2651991875822f36fceb84bdda12d1c0361d49912392b8")
    depends_on('libpressio@0.89.0:', when="@0.2.0:")
    depends_on('libpressio-frsz', when="+frsz")

    variant("frsz", default=False, description="depend on frsz", when="@0.1.2:")

    def cmake_args(self):
        args = super().cmake_args()
        if "+frsz" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_FRSZ=YES")
        return args
