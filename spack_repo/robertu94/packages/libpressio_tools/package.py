from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_tools.package  import LibpressioTools as BuiltinLibPressioTools
except ImportError:
    from spack_repo.builtin.packages.libpressio_tools.package import LibpressioTools as BuiltinLibPressioTools


class LibpressioTools(BuiltinLibPressioTools):
    """Pre-Release: General Utilities for LibPressio"""


    depends_on('libpressio-frsz', when="+frsz")

    variant("frsz", default=False, description="depend on frsz", when="@0.1.2:")
    variant("lcgpu", default=False, description="depend on lc-gpu", when="@0.5.0:")

    version("0.5.4", sha256="a6bb535ccab0ff21f24f17a68e48370adf01e199ee634b0128c03c576df92e17")
    version("0.5.3", sha256="c4dfd1c03046f5d93212ae2a33c0f5843752d314d264a06f2d1e80b947e81a23")
    version("0.5.2", sha256="7e0e6254154578864835ea6c8e7f8dbad0266d87aee13ce3295a9800e895b973")
    version("0.5.1", sha256="0146e26dc7fb3bae05edb9d4143cea39018c873a4e53be017271c1e6a00d696d")
    version("0.5.0", sha256="6fbab7fc2ce6dc65f9fa84c6e07feee22ae67d133b46a42e91c775cc99d6071c")
    depends_on("lc-framework@1.3.0:+libpressio+cuda", when="+lcgpu")
    depends_on("libpressio@1.0.0:", when="@0.5.0:")
    depends_on("libpressio@1.0.5:", when="@0.5.4:")
    depends_on("libpressio-predict@0.0.6:", when="+predict@0.5.3:")
    depends_on("cxx", type="build")
    depends_on("c", type="build")

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
