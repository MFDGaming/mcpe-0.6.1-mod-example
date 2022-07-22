from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()

patch = Patch(0xcd240)
patch.generate_patch_from_binary(getcwd() + sep + "force_creative", 0x39e, 2)
mod.add_patch(patch)

patch2 = Patch(0xcd292)
patch2.generate_patch_from_binary(getcwd() + sep + "force_creative", 0x3a0, 2)
mod.add_patch(patch2)

mod.save(getcwd() + sep + "force_creative.mod")
