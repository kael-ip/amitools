import datetime
from amitools.vamos.libcore import LibCreator, LibInfo, LibCtx
from amitools.vamos.machine import MockMemory, MockTraps, MockCPU
from amitools.vamos.AccessMemory import AccessMemory
from amitools.vamos.label import LabelManager
from amitools.vamos.MemoryAlloc import MemoryAlloc
from amitools.vamos.lib.VamosTestLibrary import VamosTestLibrary


def setup():
  raw_mem = MockMemory(fill=23)
  traps = MockTraps()
  cpu = MockCPU()
  mem = AccessMemory(raw_mem)
  size = raw_mem.get_ram_size() * 1024 - 0x100
  alloc = MemoryAlloc(mem, 0x100, size)
  ctx = LibCtx(cpu, mem)
  return mem, traps, alloc, ctx


def libcore_create_lib_default_test():
  mem, traps, alloc, ctx = setup()
  impl = VamosTestLibrary()
  # create info for lib
  date = datetime.date(2012, 11, 12)
  info = LibInfo('vamostest.library', 42, 3, date)
  # create lib
  creator = LibCreator(alloc, traps)
  lib = creator.create_lib(info, ctx, impl)
  # free lib
  creator.free_lib(lib)


def libcore_create_lib_fake_test():
  mem, traps, alloc, ctx = setup()
  impl = None
  # create info for lib
  date = datetime.date(2012, 11, 12)
  info = LibInfo('vamostest.library', 42, 3, date)
  # create lib
  creator = LibCreator(alloc, traps)
  lib = creator.create_lib(info, ctx, impl)
  # free lib
  creator.free_lib(lib)


def libcore_create_lib_label_mgr_test():
  mem, traps, alloc, ctx = setup()
  impl = VamosTestLibrary()
  label_mgr = LabelManager()
  # create info for lib
  date = datetime.date(2012, 11, 12)
  info = LibInfo('vamostest.library', 42, 3, date)
  # create lib
  creator = LibCreator(alloc, traps, label_mgr)
  lib = creator.create_lib(info, ctx, impl)
  # free lib
  creator.free_lib(lib)


def libcore_create_lib_profile_test():
  mem, traps, alloc, ctx = setup()
  impl = VamosTestLibrary()
  # create info for lib
  date = datetime.date(2012, 11, 12)
  info = LibInfo('vamostest.library', 42, 3, date)
  # create lib
  creator = LibCreator(alloc, traps)
  lib = creator.create_lib(info, ctx, impl, do_profile=True)
  # free lib
  creator.free_lib(lib)
