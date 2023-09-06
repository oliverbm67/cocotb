-- TOP module

library ieee;
use ieee.std_logic_1164.all;

library cell_lib;
use cell_lib.all;

library default_lib;
use default_lib.all;

entity top is
    port(
        clk                     : in  std_logic;
        rstn                    : in  std_logic;
        sig_in                  : in  std_logic;
        sig_out                 : out std_logic_vector(3 downto 0)
    );
end top;

architecture rtl of top is

begin

-- Verilog module from default library
reg_verilog_default : entity default_lib.reg_a_v
port map(
    clk     => clk,
    rstn    => rstn,
    d       => sig_in,
    q       => sig_out(0)
);

-- Verilog module from cell library
reg_verilog_cell : entity cell_lib.reg_b_v
port map(
    clk     => clk,
    rstn    => rstn,
    d       => sig_in,
    q       => sig_out(1)
);

-- VHDL module from default library
reg_vhdl_default : entity default_lib.reg_a
port map(
    clk     => clk,
    rst_n   => rstn,
    d       => sig_in,
    q       => sig_out(2)
);

-- VHDL module from cell library
reg_vhdl_cell : entity cell_lib.reg_b
port map(
    clk     => clk,
    rst_n   => rstn,
    d       => sig_in,
    q       => sig_out(3)
);

end rtl;

