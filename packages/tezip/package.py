# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Tezip(CMakePackage, CudaPackage):
    """the tezip compressor for time evolving data"""

    homepage = "https://tezip.readthedocs.io/en/latest/"
    url = "tezip"

    maintainers("robertu94")

    license("Apache-2.0", checked_by="robertu94")

    version("main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("opencv+cuda+imgcodecs+highgui+imgproc+cudev", type=("build","link"))
    depends_on("hdf5+cxx", type=("build","link"))
    depends_on("boost+serialization", type=("build","link"))
    depends_on("h5cpp", type=("build","link"))
    depends_on("cereal", type=("build","link"))
    depends_on("py-torch+cuda", type=("build","link"))
    depends_on("libpressio@1.0.0:", type=("build","link"))
    conflicts("~cuda")
