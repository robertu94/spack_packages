# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyTomocupy(PythonPackage):
    """a Python package and a command-line interface for GPU reconstruction of
       tomographic/laminographic data in 16-bit and 32-bit precision"""

    homepage = "https://tomocupy.readthedocs.io/en/latest/index.html"

    url = "https://github.com/tomography/tomocupy"

    maintainers("robertu94")

    version("2023-04-20", "5ded81d8da7d3f8ded6e1570e8c47cfc5446d5a5")

    depends_on("py-scikit-build", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-cupy", type=("build", "run"))
    depends_on("swig", type=("build", "run"))
    depends_on("opencv", type=("build", "run"))
    depends_on("py-pywavelets", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-astropy", type=("build", "run"))
    depends_on("py-olefile", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-torchaudio", type=("build", "run"))
