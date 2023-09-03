# Makefile for mixed_language_multi_libraries

SIM ?= questa
TOPLEVEL_LANG ?= vhdl

# Compilation in default libraries
VHDL_SOURCES = $(PWD)/../hdl/reg_a.vhd $(PWD)/../hdl/top.vhd
VERILOG_SOURCES = $(PWD)/../hdl/reg_a.v

# Compilation in cell_lib
VHDL_SOURCES_cell_lib = $(PWD)/../hdl/reg_b.vhd
VERILOG_SOURCES_cell_lib = $(PWD)/../hdl/reg_b.v

# Define library order
VHDL_LIB_ORDER = cell_lib
TOPLEVEL = top

MODULE = mixed_language_multi_libraries

include $(shell cocotb-config --makefiles)/Makefile.sim
