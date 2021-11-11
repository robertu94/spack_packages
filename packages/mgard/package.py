from spack import *


class Mgard(CMakePackage, CudaPackage):
    """MGARD error bounded lossy compressor"""

    homepage = "https://github.com/CODARcode/MGARD"
    git      = "https://github.com/CODARcode/MGARD"

    version('master', branch='master')
    version('robertu94', git="https://github.com/robertu94/MGARD", branch="master", prefered=True)
    version('2020-10-01', commit="b67a0ac")

    depends_on("zlib")
    depends_on("zstd")
    depends_on("libarchive", when="@robertu94:")
    depends_on("tclap", when="@robertu94:")
    depends_on("yaml-cpp", when="@robertu94:")
    depends_on("nvcomp@robertu", when="+cuda")

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING=OFF"
        ]
        if "+cuda" in self.spec:
            args.append("-DMGARD_ENABLE_CUDA=ON")
            args.append("-DCUDA_ARCH_STRING={}".format(
                ";".join(self.spec.variants["cuda_arch"].value))
                )
        return args
