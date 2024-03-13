# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-langsmith
#
# You can edit this file again by typing:
#
#     spack edit py-langsmith
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyLangsmith(PythonPackage):
    """LangSmith is a platform for building production-grade LLM applications."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://docs.smith.langchain.com/"
    url = "https://files.pythonhosted.org/packages/12/2a/f091e2d0922469b5a96c33238f66340c507d43298ee0802a20f1c66759d3/langsmith-0.1.1-py3-none-any.whl"

    maintainers("robertu94")

    license("MIT", checked_by="robertu94")

    version("0.1.1", sha256="10ff2b977a41e3f6351d1a4239d9bd57af0547aa909e839d2791e16cc197a6f9", expand=False)

    depends_on("python@3.8.1:4", type=("build", "run"))
    depends_on("py-pydantic@1:2", type=("build","run"))
    depends_on("py-requests@2", type=("build","run"))
