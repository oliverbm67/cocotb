module reg_b_v (
    input clk,
    input rstn,
    input d,
    output reg q);

always @(posedge clk)
    if (!rstn)
        q <= 0;
    else begin
        q <= d;
    end
endmodule
