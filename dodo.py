#!/usr/bin/env python3
# Copyright Stefan Wallentowitz <stefan.wallentowitz@hm.edu>.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

from doit.action import CmdAction
from doit import get_var

DOIT_CONFIG = {'default_tasks': []}

opentitan = get_var("opentitan", "opentitan")
toolchain = get_var("toolchain", "/tools/riscv")

def task_prepare_opentitan_sw():
    return {
        "actions": [
            CmdAction("./meson_init.sh", cwd=opentitan),
            CmdAction("ninja -C build-out all", cwd=opentitan),
        ],
        "verbosity": 2,
    }

def task_prepare_opentitan_bitstream():
    return {
        "actions": [
            CmdAction("fusesoc --cores-root . run --flag=fileset_top --target=synth lowrisc:systems:chip_earlgrey_nexysvideo", cwd=opentitan),
        ],
        "verbosity": 2,
        "task_dep": ["prepare_opentitan_sw"],
    }

def task_program_bitstream():
    return {
        "actions": [f"{opentitan}/util/opentitan-pgm-fpga/opentitan-pgm-fpga xc7a200tsbg484-1 {opentitan}/build/lowrisc_systems_chip_earlgrey_nexysvideo_0.1/synth-vivado/lowrisc_systems_chip_earlgrey_nexysvideo_0.1.bit"],
        "verbosity": 2
    }

def task_build_device_sw():
    build_dir = "build-device-sw"

    return {
        "actions": [f"meson {build_dir} sw/device --cross-file={toolchain}/meson-riscv32-unknown-elf-clang.txt", f"ninja -C {build_dir} all"],
        "verbosity": 2
    }

def task_flash_device_sw():
    def create_cmd_string(pos):
        return "{opentitan}/build-out/sw/host/spiflash/spiflash --input build-device-sw/apps/{app}/{app}_fpga_nexysvideo.bin".format(app=pos[0], opentitan=opentitan)

    return {
        "actions": [CmdAction(create_cmd_string)],
        "pos_arg": "pos",
        "verbosity": 2
    }