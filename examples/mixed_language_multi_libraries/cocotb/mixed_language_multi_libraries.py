"""A compilation example for hdl mixing Verilog and VHDL and multiple libraries"""

import os
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def sanity_test(dut):
    """A simple test of the RTL to confirm the simulation is running"""
    cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())
    dut.rstn.value = 0
    dut.sig_in.value = 0
    await Timer(1, units="ns")
    await RisingEdge(dut.clk)
    assert dut.sig_out.value == 0
    dut.sig_in.value = 1
    await RisingEdge(dut.clk)
    assert dut.sig_out.value == 15



def mixed_lang_multi_lib_runner():
    """cocotb python runner"""
    hdl_toplevel_lang = "vhdl"
    sim = "questa"

    rtl_dir = os.getcwd() + "/../hdl/"

    runner = get_runner(sim)

    runner.build(
        verilog_sources=[rtl_dir + "reg_b.v"],
        vhdl_sources=[rtl_dir + "reg_b.vhd"],
        hdl_library="cell_lib",
    )
    runner.build(
        verilog_sources=[rtl_dir + "reg_a.v"], vhdl_sources=[rtl_dir + "reg_a.vhd"]
    )
    runner.build(vhdl_sources=[rtl_dir + "top.vhd"], hdl_toplevel="top")
    runner.test(hdl_toplevel="top", test_module="mixed_language_multi_libraries")


if __name__ == "__main__":
    mixed_lang_multi_lib_runner()
