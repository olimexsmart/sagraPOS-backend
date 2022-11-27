from escpos.printer import Network

kitchen = Network("192.168.1.37") #Printer IP Address
kitchen.text("Python best linguaggio ever\n")
kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
kitchen.cut()
