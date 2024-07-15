from tkinter import *

main = Tk()

#file name
fileName_label = Label(main, text = "File name")
fileName_label.grid(row=0, column=0)

file_name = Entry(main)
file_name.grid(row=0, column=1)
filetxt = Label(main, text = ".txt")
filetxt.grid(row=0, column = 2)

#[stock solution]
stocksol_label = Label(main, text="Concentration of Stock Solution")
stocksol_label.grid(row=1, column=0)

stocksol = Entry(main)
stocksol.grid(row=1, column=1)

clicked = StringVar()
clicked.set("mol/L")
drop = OptionMenu(main, clicked, "mol/L", "mmol/L", "Mmol/L", "nmol/L")
drop.grid(row=1, column=2)

#required concentrations
conc_label = Label(main, text="Required Concentrations (seperated by a space)")
conc_label.grid(row=2, column=0)

conc = Entry(main)
conc.grid(row=2, column=1)

clicked = StringVar()
clicked.set("mol/L")
drop = OptionMenu(main, clicked, "mol/L", "mmol/L", "Mmol/L", "nmol/L")
drop.grid(row=2, column=2)

#max vol of beaker
maxvol_label = Label(main, text="Maximum Volume of Beaker")
maxvol_label.grid(row=3, column=0)

maxvol = Entry(main)
maxvol.grid(row=3, column=1)
unit1 = Label(main, text="mL")
unit1.grid(row=3,column=2)

#min vol of beaker
minvol_label = Label(main, text="Minimum Volume of Beaker")
minvol_label.grid(row=4, column=0)

minvol = Entry(main)
minvol.grid(row=4, column=1)
unit2 = Label(main, text="mL")
unit2.grid(row=4,column=2)

#min vol of pipette
minpip_label = Label(main, text="Minimum Volume of Pipette Gun")
minpip_label.grid(row=5, column=0)

minpip = Entry(main)
minpip.grid(row=5, column=1)
unit3 = Label(main, text="mL")
unit3.grid(row=5,column=2)

#initial volume
initialvol_label = Label(main, text="Initial Volume")
initialvol_label.grid(row=6, column=0)

initialvol = Entry(main)
initialvol.grid(row=6, column=1)
unit4 = Label(main, text="mL")
unit4.grid(row=6,column=2)

#load method
loadmethod_button = Button(main, text="Load Method")
loadmethod_button.grid(row=7, column=0)

var = IntVar()
c = Checkbutton(main, text="Export Method", variable=var)
c.grid(row=7, column=1)

var1 = IntVar()
c1 = Checkbutton(main, text="Export Results", variable=var1)
c1.grid(row=7, column=2)


main.mainloop()
