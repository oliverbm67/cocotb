"""A compilation example for hdl mixing Verilog and VHDL and multiple libraries"""

import os
import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock


@cocotb.test()
async def sanity_test(dut):
    """A simple test of the RTL to confirm the simulation is running"""
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rstn.value = 0
    dut.sig_in.value = 0
    await Timer(1, units="ns")
    await RisingEdge(dut.clk)
    assert dut.sig_out.value == 0
    await Timer(1, units="ns")
    dut.rstn.value = 1
    dut.sig_in.value = 1
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")
    assert dut.sig_out.value == 15
