# Copyright lowRISC contributors, Stefan Wallentowitz <stefan.wallentowitz@hm.edu>.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

project('opentitan-device-demo-sw', 'c',
  default_options: [
    'c_std=c11',
    'build.c_std=c11',
    'cpp_std=c++14',
    'build.cpp_std=c++14',
    'warning_level=2',
    'werror=true',
    'debug=true',
    'b_staticpic=false', # Disable PIC for device static libraries
    'b_pie=false',       # Disable PIE for device executables
  ],
)

c_cpp_compile_args = [
  # Do not use standard system headers
  '-nostdinc',
  # Use OpenTitan's freestanding headers instead
  '-isystem' + meson.source_root() / '../../opentitan/sw/device/lib/base/freestanding',
  # Don't emit unwinding information
  '-fno-asynchronous-unwind-tables',
  # Don't use COMMON sections for uninitialized globals
  '-fno-common',
  '-Wimplicit-fallthrough', # Error on implicit fallthrough
  '-Wswitch-default', # Ensure all switches have default statements
  '-Wno-covered-switch-default', # We require `default:` always.
  '-Wgnu', # We aim to be standards compliant, and avoid gnu extensions.
  '-Wno-error=unused-function', # Don't error out on unused functions, only warn.
  # Issues we intend to fix in the future but are currently ignored as there are
  # many places they are triggered.
  '-Wno-unused-parameter',
  '-Wno-sign-compare',
  '-Wno-missing-field-initializers',
  '-Wno-gnu-zero-variadic-macro-arguments',
  '-Os', # General "Optimize for Size" Option
  '-fvisibility=hidden', # Hide symbols by default
]

# Add the flags for cross builds.
add_project_arguments(
  c_cpp_compile_args,
  language: ['c', 'cpp'], native: false)

# The following flags are applied only to cross builds
c_cpp_cross_link_args = [
  # Do not use standard system startup files or libraries
  '-nostartfiles',
  '-nostdlib',
   # Only link static files
  '-static',
  # Warn if we use COMMON
  '-Wl,--warn-common',
  # Warn if we include orphan sections
  '-Wl,--orphan-handling=warn',
  # Turn Linker Warnings into Errors
  '-Wl,--fatal-warnings',
]
add_project_link_arguments(
  c_cpp_cross_link_args,
  language: ['c', 'cpp'], native: false)

subdir('libs')

sw_lib_arch_fpga_nexysvideo = declare_dependency(
  link_with: static_library(
    'device_fpga_nexysvideo',
    sources: ['../../opentitan/sw/device/lib/arch/device_fpga_nexysvideo.c'],
    dependencies: [ ot_sdk ]
  ),
)

sw_lib_arch_core_devices = {
  'fpga_nexysvideo': sw_lib_arch_fpga_nexysvideo,
}

# `custom_target` arguments for creating a `.dis` file from an `.elf` file.
elf_to_dis_custom_target_args = {
  'output': '@BASENAME@.dis',
  'command': [
    find_program('objdump'),
    '--disassemble',
    '--headers',
    '--line-numbers',
    '--source',
    '@INPUT@',
  ],
  # Write the stdout of objdump to the output file.
  'capture': true,
  'build_by_default': true,
}

# `custom_target` arguments for creating a `.bin` file from an `.elf` file.
elf_to_bin_custom_target_args = {
  'output': '@BASENAME@.bin',
  'command': [
    find_program('objcopy'),
    '--output-target', 'binary',
    '@INPUT@',
    '@OUTPUT@',
  ],
  'build_by_default': true,
}

export_target_command = [
  meson.source_root() / '../../opentitan/util/export_target.sh',
  'builddir/sw',
  'sw',
  '@OUTDIR@',
  '@INPUT@',
]
export_target_depend_files = [
  meson.source_root() / '../../opentitan/util/export_target.sh',
]

subdir('apps')
