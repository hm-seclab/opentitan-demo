# Copyright lowRISC contributors.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

foreach device_name, device_lib : sw_lib_arch_core_devices
  hello_elf = executable(
    'hello_' + device_name,
    sources: ['hello.c'],
    name_suffix: 'elf',
    dependencies: [
      device_lib,
      ot_sdk,
    ],
    link_args: [
      '-Wl,-L,../opentitan/',
      '-Wl,-T,sw/device/exts/common/flash_link.ld',
      '-Wl,--build-id=none',
    ],
  )

  target_name = 'hello_@0@_' + device_name

  hello_dis = custom_target(
    target_name.format('dis'),
    input: hello_elf,
    kwargs: elf_to_dis_custom_target_args,
  )

  hello_bin = custom_target(
    target_name.format('bin'),
    input: hello_elf,
    kwargs: elf_to_bin_custom_target_args,
  )

  custom_target(
    target_name.format('export'),
    command: export_target_command,
    depend_files: [export_target_depend_files,],
    input: [
      hello_elf,
      hello_dis,
      hello_bin,
    ],
    output: target_name.format('export'),
    build_always_stale: true,
    build_by_default: true,
  )
endforeach
