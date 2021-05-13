if __name__ == '__main__':

    name = 'rom_{0}x{1}.dat'

    while True:

        try:
            n = int(input('n: '))

            file = name.format(f'{2**(2*n)}', f'{2*n}')
            fileobject = open(file, 'w')

            for op1 in range(2**n):
                for op2 in range(2**n):
                    mult = op1 * op2
                    form_op1 = format(op1, f'0{n}b')
                    form_op2 = format(op2, f'0{n}b')
                    form_mult = format(mult, f'0{n*2}b')

                    print(form_mult)
                    fileobject.write(f'{form_mult}\n')
            
            fileobject.close()


        except ValueError:
            print(f'Integer only')
            continue
        else:
            break

    filename = "inter_mult.v"

    fileobject = open(filename,'w')
        
    fileobject.write(f"""module rom_file #(parameter n = {n})(data, address, read_en);

input [n-1:0] address;
input read_en;
output [n-1:0] data;
reg [n-1:0] mem [0:(2**n)-1];

assign data = read_en ? mem[address]:'b0;

initial begin

    $readmemb("{name}", mem);

end

endmodule""")

    fileobject.close()

    filename = "inter_mult_TB.v"

    fileobject = open(filename,'w')
        
    fileobject.write(f"""module rom_tb();
parameter n = {n};
reg [n-1:0] address;
 reg read_en;
 wire [n-1:0] data;
 integer i, j;
 
 initial begin
   address = 0;
   read_en = 0;
   #10 $monitor ("address = %b, data = %b, read_en = %b", address, data, read_en);
   for (i = 0; i <(2**n); i = i +1 ) begin
    for (j = 0; j<(2**n); j = j + 1) begin
     #10 address = {{i ,j}};
     read_en = 1;
   end
   end
 end
 
rom_file #(n) inst_1(
data , 
address    , 
read_en
);

endmodule
""")

    fileobject.close()