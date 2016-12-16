from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as BaseBuildExt


EXT_MODULES = []


def make_ext(swig_opts):
    return Extension(
        "_ome_files",
        sources=["src/ome_files.i"],
        libraries=["ome-common", "ome-files", "ome-xml"],
        swig_opts=swig_opts,
    )


class BuildExt(BaseBuildExt):

    def run(self):
        # NOTE: also adds the Python headers dir
        swig_opts = ["-c++"] + ["-I%s" % _ for _ in self.include_dirs]
        EXT_MODULES.append(make_ext(swig_opts))
        BaseBuildExt.run(self)


setup(
    name="ome_files",
    cmdclass={"build_ext": BuildExt},
    ext_modules=EXT_MODULES,
)
