# Makefile for mixed_language_multi_libraries

SIM ?= questa
TOPLEVEL_LANG ?= vhdl


# Compilation in default library
VHDL_SOURCES_default_lib = $(PWD)/../hdl/reg_a.vhd
VERILOG_SOURCES_default_lib = $(PWD)/../hdl/reg_a_v.v

# Compilation in cell_lib
VHDL_SOURCES_cell_lib = $(PWD)/../hdl/reg_b.vhd
VERILOG_SOURCES_cell_lib = $(PWD)/../hdl/reg_b_v.v

# Top level
VHDL_SOURCES = $(PWD)/../hdl/top.vhd 

# Define library order
VHDL_LIB_ORDER = cell_lib default_lib

# HDL top level
TOPLEVEL = top

# Python file test
MODULE = mixed_language_multi_libraries

# Include cocotb makefile flow
include $(shell cocotb-config --makefiles)/Makefile.sim
