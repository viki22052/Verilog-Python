module rom_tb();
parameter n = 2;
reg [n-1:0] address;
 reg read_en;
 wire [n-1:0] data;
 integer i;
 
 initial begin
   address = 0;
   read_en = 0;
   #10 $monitor ("address = %b, data = %b, read_en = %b", address, data, read_en);
   for (i = 0; i <(2**n); i = i +1 )begin
     #10 address = i;
     read_en = 1;
   end
 end
 
rom_file #(n) inst_1(
data , 
address    , 
read_en
);

endmodule
