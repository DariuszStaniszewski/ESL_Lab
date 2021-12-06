from myhdl import intbv,bin,modbv,Signal

test = intbv(24, min = 0, max = 25)
print(test.min)
print(test.max)
print(len(test))

%Pojedyńcze wartości
print(test[0])
print(test[1])
print(test[2])

%Zakresy
print(bin(test[3:2]))
print(bin(test[:]))

count = Signal(modbv(0, min=0, max=2**8))
print(count)
count.next = count + 1
print(count.next)
