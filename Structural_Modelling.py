from myhdl import block, Signal, delay,always, now

from ClkDriver import ClkDriver
from Hello import Hello


SLOW, MEDIUM, FAST = range(3)

@block
def top1(speed=SLOW):
    def slowAndSmall():
       return 1
    def fastAndLarge():
       return 2
    if speed == SLOW:
        return slowAndSmall()
    elif speed == FAST:
        return fastAndLarge()
    else:
        raise NotImplementedError

# @block
# def top():
#
#     din = Signal(0)
#     dout = Signal(0)
#     clk = Signal(bool(0))
#     reset = Signal(bool(0))
#
#     channel_inst = channel(dout, din, clk, reset)
#
#     return channel_inst

# @block
# def top(..., n=8):
#
#     din = [Signal(0) for i in range(n)]
#     dout = [Signal(0) for in range(n)]
#     clk = Signal(bool(0))
#     reset = Signal(bool(0))
#     channel_inst = [None for i in range(n)]
#
#     for i in range(n):
#         channel_inst[i] = channel(dout[i], din[i], clk, reset)
#
#     return channel_inst


%Zmienne z instrukcji
# request_list = [Signal(bool()) for i in range(M)]
# arb = arbiter(grant_vector, request_vector, clock, reset)
# request_vector = ConcatSignal(*reversed(request_list)
#grant_vector = Signal(intbv(0)[M:])
#grant_list = [grant_vector(i) for i in range(M)]
