import math

LN2 = math.log(2.0)

def nats_to_bits(nats: float) -> float:
    return nats / LN2

def bits_to_nats(bits: float) -> float:
    return bits * LN2
