module rom_file #(parameter n = 2)(data, address, read_en);

input [n-1:0] address;
input read_en;
output [n-1:0] data;
reg [n-1:0] mem [0:(2**n)-1];

assign data = read_en ? mem[address]:'b0;

initial begin

    $readmemb("rom_{0}x{1}.dat", mem);

end

endmodule