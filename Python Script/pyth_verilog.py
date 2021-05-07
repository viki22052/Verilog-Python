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