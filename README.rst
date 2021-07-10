OpenTitan Demos
===============

This is a work-in-progress repository that helps building your own FPGA demonstrators and apps.

At the moment it uses the entire OpenTitan tree to build a modified bitstream for the Nexys Video board. The modification is an extra SPI device that is mapped to the JA pmod.

In future the idea is to support multiple FPGA boards and SoC layouts, but there is some work pending on OpenTitan itself to better support that.

For now, the main purpose is to build software for OpenTitan *out-of-tree*. It is very simple to create own applications and execute them.

QuickStart
----------

Clone OpenTitan:

.. code:: cmd

   git submodule update --init --recursive

You need to prepare the Python environment:

.. code:: cmd

   pip3 install -r python-requirements.txt
   pip3 install -r opentitan/python-requirements.txt

You will need Vivado and the RISC-V toolchain as described in the OpenTitan documentation.

Prepare OpenTitan bitstream and libraries:

.. code:: cmd

   doit prepare_opentitan_sw
   doit prepare_opentitan_bitstream

Now load the bitstream to the FPGA:

.. code:: cmd

   doit program_bitstream

Finally build the software from this repository:

.. code:: cmd

   doit build_device_sw

And now flash it to the device (set app as you like):

.. code:: cmd

   doit flash_device_sw hello

   
