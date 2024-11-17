from spack import *
from spack.pkg.builtin.libpressio_tools import LibpressioTools as BuiltinLibPressioTools


class LibpressioTools(BuiltinLibPressioTools):
    """Pre-Release: General Utilities for LibPressio"""


    depends_on('libpressio-frsz', when="+frsz")

    variant("frsz", default=False, description="depend on frsz", when="@0.1.2:")
    variant("lcgpu", default=False, description="depend on lc-gpu", when="@0.5.0:")

    version("0.5.1", sha256="0146e26dc7fb3bae05edb9d4143cea39018c873a4e53be017271c1e6a00d696d")
    version("0.5.0", sha256="6fbab7fc2ce6dc65f9fa84c6e07feee22ae67d133b46a42e91c775cc99d6071c")
    depends_on("lc-framework@1.3.0:+libpressio+cuda", when="+lcgpu")
    depends_on("libpressio@1.0.0:", when="@0.5.0:")

    def setup_run_environment(self, env):
        libraries = find_libraries(["liblibpressio_meta"], root=self.prefix, recursive=True)
        env.set("LIBPRESSIO_PLUGINS", libraries[0])

    def cmake_args(self):
        args = super().cmake_args()
        if "+frsz" in self.spec:
            args.append("-DLIBPRESSIO_TOOLS_HAS_FRSZ=YES")
        args.append(self.define_from_variant("LIBPRESSIO_TOOLS_HAS_ADIOS2", "adios2"))
        args.append(self.define_from_variant("LIBPRESSIO_TOOLS_HAS_LC_GPU", "lcgpu"))
        return args
