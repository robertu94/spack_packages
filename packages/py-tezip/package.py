# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTezip(PythonPackage):
    """Data data compression tool for time evolutonary data"""
    homepage = "https://tezip.readthedocs.io/en/latest/#environment-construction-procedure"
    git = "https://github.com/kento/TEZip"

    maintainers("robertu94")
    license("Apache-2.0", checked_by="robertu94")

    version("2023-03-31", commit="f18ca0fb076b21dd8c5dabc6dc401049462b0409")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-tensorflow+cuda", type=("run"))
    depends_on("py-h5py", type=("run"))
    depends_on("py-cupy+cuda", type=("run"))
    depends_on("py-numpy", type=("run"))
    depends_on("py-pillow", type=("run"))

    variant("examples", default=False)
    depends_on("py-beautifulsoup4", when="+examples")
    depends_on("py-imageio", when="+examples")
    depends_on("py-requests", when="+examples")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
