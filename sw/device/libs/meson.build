# Copyright Stefan Wallentowitz <stefan.wallentowitz@hm.edu>.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

c = meson.get_compiler('c')

ot_dir = meson.current_source_dir() + '/../../../opentitan/'
libbasedir = ot_dir + 'build-out/sw/device/lib/'
libdirs = [ libbasedir, libbasedir+'runtime', libbasedir+'dif', libbasedir+'base', libbasedir+'crt', libbasedir+'testing' ]

lib_runtime_hart = c.find_library('runtime_hart_ot', dirs : libdirs)
lib_runtime_print = c.find_library('runtime_print_ot', dirs : libdirs)
lib_runtime_log = c.find_library('runtime_log_ot', dirs : libdirs)
lib_pinmux = c.find_library('pinmux_ot', dirs : libdirs)
lib_dif_uart = c.find_library('uart_ot', dirs : libdirs)
lib_dif_spi_device = c.find_library('sw_lib_dif_spi_device', dirs : libdirs)
lib_irq = c.find_library('irq_ot', dirs : libdirs)
lib_irq_handlers = c.find_library('irq_default_handlers_ot', dirs : libdirs)
lib_mmio = c.find_library('mmio_ot', dirs : libdirs)
lib_mem = c.find_library('mem_ot', dirs : libdirs)
lib_test_status = c.find_library('test_status_ot', dirs : libdirs)
lib_crt = c.find_library('crt_ot', dirs : libdirs)

riscv_crt = declare_dependency(
  sources: [
      ot_dir + 'sw/device/exts/common/flash_crt.S',
      ot_dir + 'sw/device/exts/common/ibex_interrupt_vectors.S',
  ],
  dependencies: [
      lib_crt
  ]
)

ot_sdk = declare_dependency(
    dependencies: [
      lib_runtime_hart,
      lib_runtime_print,
      lib_runtime_log,
      lib_pinmux,
      lib_irq,
      lib_dif_spi_device,
      lib_dif_uart,
      lib_irq_handlers,
      lib_mmio,
      lib_mem,
      lib_test_status,
      riscv_crt,
    ],
    include_directories: ['../../opentitan/' ]
)
