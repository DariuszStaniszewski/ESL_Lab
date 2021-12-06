from myhdl import block, instance, Signal, intbv, delay, always_comb

@block
def mux(z, a, b, sel):

    """ Multiplexer.
    z -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b
    """

    @always_comb
    def comb():
        if sel == 1:
            z.next = a
        else:
            z.next = b

    return comb
