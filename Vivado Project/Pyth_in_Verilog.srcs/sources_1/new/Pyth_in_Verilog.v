`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/05/2021 04:30:53 PM
// Design Name: 
// Module Name: rom_file
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module rom_file #(parameter n = 4)(data, address, read_en);

input [n-1:0] address;
input read_en;
output [n-1:0] data;
reg [n-1:0] mem [0:(2**n)-1];

assign data = read_en ? mem[address]:'b0;

initial begin

    $readmemb("rom_16x4.dat", mem);

end

endmodule
