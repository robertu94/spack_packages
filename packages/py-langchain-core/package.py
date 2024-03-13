# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLangchainCore(PythonPackage):
    """LangChain Core contains the base abstractions that power the rest of the LangChain ecosystem."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://api.python.langchain.com/en/stable/core_api_reference.html"
    url = "https://files.pythonhosted.org/packages/b1/e9/7e624fe4a7619821331ad2e943fbfc2eab7465cf97ee95158c435a276d3e/langchain_core-0.1.23-py3-none-any.whl"

    maintainers("robertu94")

    license("MIT", checked_by="robertu94")

    version("0.1.23", sha256="d42fac013c39a8b0bcd7e337a4cb6c17c16046c60d768f89df582ad73ec3c5cb", expand=False)

    depends_on("python@3.8.1:", type=("build", "run"))

    depends_on("py-poetry-core", type="build")
    depends_on("py-pydantic@1:2", type=("build","run"))
    depends_on("py-tenacity@8.1:9", type=("build", "run"))
    depends_on("py-jsonpatch@1.33:2", type=("build", "run"))
    depends_on("py-anyio@3", type=("build", "run"))
    depends_on("py-pyaml@5.3:", type=("build", "run"))
    depends_on("py-requests@2", type=("build", "run"))
    depends_on("py-packaging@23.2:", type=("build", "run"))
    depends_on("py-jinja2@3", type=("build", "run"))
