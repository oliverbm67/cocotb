"""A compilation example for hdl mixing Verilog and VHDL and multiple libraries"""

import os
from cocotb.runner import get_runner

def mixed_lang_multi_lib_runner():
    hdl_toplevel_lang = "vhdl"
    sim = "questa"

    rtl_dir = os.getcwd()+"/../hdl/"

    runner = get_runner(sim)

    runner.build(
            verilog_sources = [ rtl_dir+"reg_b.v" ],
            vhdl_sources = [ rtl_dir+"reg_b.vhd" ],
            hdl_library = "cell_lib"
    )
    runner.build(
            verilog_sources = [ rtl_dir+"reg_a.v" ],
            vhdl_sources = [ rtl_dir+"reg_a.vhd" ]
    )
    runner.build(
            vhdl_sources = [ rtl_dir+"top.vhd" ],
            hdl_toplevel = "top"
    )
    runner.test(hdl_toplevel="top", test_module="mixed-langages-multi-lib")

if __name__ == "__main__":
    mixed_lang_multi_lib_runner()
