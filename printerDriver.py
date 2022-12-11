from escpos.printer import Network


if __name__ == '__main__':
    printer = Network("192.168.1.37") #Printer IP Address
    printer.set(align='left', custom_size=True, height=3, width=2, bold=True)
    printer.text("CAPPONADDA         4X\n")
    printer.text("TROFIE             3X\n")
    printer.text("TESTAROLO PESTO    6X\n")
    printer.text("BIRRA              3X\n")
    printer.cut(feed=False)


def order(plainOrder):
    printer = Network("192.168.1.37", timeout=3) #Printer IP Address
    printer.set(align='left', custom_size=True, height=3, width=2, bold=True)
    for k, v in plainOrder.items():
        for e in v:
            t = '{name:<18}{quantity:>2}X\n'.format(**e).upper()
            print(t)
            print('BOMBER')
            printer.text(t)
        printer.cut()
    printer.text('PROVAAAAA\n\n')
