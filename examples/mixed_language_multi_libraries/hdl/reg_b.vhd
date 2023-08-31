library ieee;
use ieee.std_logic_1164.all;

entity reg_b is
    port(
        clk                     : in  std_logic;
        rst_n                   : in  std_logic;
        d                       : in  std_logic;
        q                       : out std_logic
    );
end reg_b;

architecture rtl of reg_b is

begin

process(clk,rst_n) begin
if rst_n = '0' then
    q <= '0';
elsif rising_edge(clk) then
    q <= d;
end if;
end process;

end rtl;

