pkgname = "vulkan-headers"
pkgver = "1.3.279"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "7844631d7765bcaebb8db5cce9837a4561285640a4d3e9ea144c6d27fdd50d61"
# no test suite
options = ["!check"]
