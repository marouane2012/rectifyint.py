import math
from mpmath import *
import copy
class rectifyint:
    def __init__(inst,mantissa,exponent):
        """Create new arbitrary precision rectifyint"""
        inst.mantissa = mantissa
        inst.exponent = exponent
    def accurate(inst):
        """
        Makes an rectifyint type accurate
        """
        if abs(inst.mantissa) >= 10:
            inst.exponent += floor(log10(abs(inst.mantissa)))
            inst.mantissa /= 10**floor(log10(abs(inst.mantissa)))
        if abs(inst.mantissa) < 1 and abs(inst.mantissa) > 0:
            inst.exponent += floor(log10(abs(inst.mantissa)))
            inst.mantissa *= 10**(floor(log10(abs(inst.mantissa))*(-1))+1)
    def __str__(inst):
        return (str(inst.mantissa) + 'e' + str(inst.exponent))
    def add(inst,sec):
        """Adds 2 instances of rectifyint"""
        recicorpial = (inst.exponent-sec.exponent)*-1
        if recicorpial > 307:
            return sec
        else:
            k = inst.mantissa +(sec.mantissa)*(10**recicorpial)
            k = rectifyint(k,inst.exponent)
            k.accurate()
            return k
    def sub(inst,sec):
        """Subtracts rectifyint types."""
        recicorpial = (inst.exponent-sec.exponent)*-1
        if recicorpial > 307:
            return rectifyint(sec.mantissa*-1,sec.exponent)
        else:
            k = inst.mantissa -(sec.mantissa)*(10**recicorpial)
            k = rectifyint(k,inst.exponent)
            k.accurate()
            return k
    def mult(inst,sec):
        """Multiplies rectifyint types"""
        k = inst.mantissa*sec.mantissa
        l = inst.exponent+sec.exponent
        m = rectifyint(k,l)
        m.accurate()
        return m
    def div(inst,sec):
        """Divides rectifyint types"""
        if sec.mantissa != 0:
            k = inst.mantissa/sec.mantissa
            l = inst.exponent-sec.exponent
            m = rectifyint(k,l)
            m.accurate()
            return m
        else:
            raise ZeroDivisionError('rectifyint division by zero')
    def sqrt(inst):
        """Calculates square root of rectifyint type"""
        k = copy.copy(inst)
        k.mantissa **= 0.5
        k.exponent /= 2
        if k.exponent != math.floor(k.exponent):
            k.exponent = math.floor(k.exponent)
            k.mantissa *= math.sqrt(10)
        return k
    def floor(inst):
        """Calculates floor of rectifyint type"""
        k = copy.copy(inst)
        if k.exponent > 15:
            return k
        else:
            instv = k.mantissa * 10**k.exponent
            k.mantissa = math.floor(instv)
            k.exponent = 0
            k.accurate()
            return k
    def ceil(inst):
        """Calculates ceiling of rectifyint type"""
        k = copy.copy(inst)
        if k.exponent > 15:
            return k
        else:
            instv = k.mantissa * 10**k.exponent
            k.mantissa = math.ceil(instv)
            k.exponent = 0
            k.accurate()
            return k
    def round(inst):
        """Calculates rounded rectifyint type"""
        k = copy.copy(inst)
        if k.exponent > 15:
            return k
        else:
            instv = k.mantissa * 10**k.exponent
            if instv - math.floor(instv) < 0.5:
                k.mantissa = math.floor(instv)
                k.exponent = 0
                k.accurate()
            else:
                k.mantissa = math.ceil(instv)
                k.exponent = 0
                k.accurate()
            return k
    def abs(inst):
        """Calculates absolute value of rectifyint type"""
        return rectifyint(abs(inst.mantissa),inst.exponent)
    def neg(inst):
        """Calculates negative value of rectifyint type"""
        return rectifyint(inst.mantissa * -1,inst.exponent)
    def antiabs(inst):
        """Calculates negative absolute value of rectifyint type"""
        return rectifyint(abs(inst.mantissa) * -1,inst.exponent)
    def reci(inst):
        """Calculates reciprocal of rectifyint type"""
        one = rectifyint(1,0)
        return one.div(inst)
    def tostr(inst):
        """Convert rectifyint to str"""
        return (str(inst.mantissa) + 'e' + str(inst.exponent))
    def trunc(inst,length=10):
        """Truncate rectifyint type"""
        k = (str(inst.mantissa) + 'e' + str(inst.exponent))
        k = k[:length]
        return k
    def nth(inst,loc=10):
        """nth character in rectifyint type"""
        k = (str(inst.mantissa) + 'e' + str(inst.exponent))
        k = k[loc]
        return k
    def sign(inst):
        """Sign function"""
        if inst.mantissa = 0:
            return rectifyint(0,0)
        elif inst.mantissa = abs(inst.mantissa):
            return rectifyint(1,0)
        else:
            return rectifyint(-1,0)
    def pow(inst,sec):
        """Exponentiates rectifyint types."""
        #Idea:set the exponent to the the integer part of
        #(second number*log10(mantissa of first number)+exponent of first number)
        #and the mantissa to the fractional part of that
        #10^(floor(?*(instlogb)))
        instlog = mpf(log10(inst.mantissa))
        instlog += inst.exponent
        instlogb = rectifyint(instlog,0)
        instlogb.accurate()
        total = instlogb.mult(sec)
        exponent = total.floor()
        exponentb = mpf(exponent.mantissa * (10**exponent.exponent))
        totalb = copy.copy(total)
        totalb = totalb.sub(exponent)
        totalc = totalb.mantissa*(10**totalb.exponent)
        mantissa = 10**totalc
        output = rectifyint(mantissa,exponentb)
        output.accurate()
        return output
    def tetra(inst,sec):
        """Tetrates rectifyint types."""
        secasint = (sec.mantissa * (10**sec.exponent))
        secasintii = math.floor(secasint)
        secasintt = rectifyint(secasint - secasintii,0)
        olda = copy.copy(inst)
        oldaa = olda.pow(secasintt)
        k = copy.copy(inst)
        k = k.pow(oldaa)
        for i in range(secasintii-1):
            k = olda.pow(k)
        return k
    def log(inst,sec):
        instlog = log10(inst.mantissa)
        instlog += inst.exponent
        seclog = math.log10(sec.mantissa)+sec.exponent
        output = instlog/seclog
        output = rectifyint(output,0)
        output.accurate()
        return output
    def iterlog(inst,sec,count=3):
        k = copy.copy(inst)
        for i in range(count):
            k = k.log(sec)
        return k
    def iterexp(inst,sec,count=3):
        k = copy.copy(inst)
        for i in range(count):
            k = sec.pow(k)
        return k
    def antiiterexp(inst,sec,count=3):
        k = copy.copy(inst)
        for i in range(count):
            k = k.pow(sec)
        return k
    def log10(inst):
        instlog = log10(inst.mantissa)
        instlog += inst.exponent
        instlogb = rectifyint(instlog,0)
        instlogb.accurate()
        return instlogb
    def root(inst,sec):
        one = rectifyint(1,0)
        return inst.pow(one.div(sec))
    def factorial(inst):
        #n! ≈ sqrt(2*pi*n)*(n/e)**n
        pi = rectifyint(3.14159265358979323846264338,0)
        e = rectifyint(2.718281828459045235760287471352,0)
        num = copy.copy(inst)
        k = num.mult(pi)
        k = k.mult(rectifyint(2,0))
        k = k.sqrt()
        l = num.div(e)
        l = l.pow(num)
        total = k.mult(l)
        return total
    def moreeq(inst,sec):
        if inst.exponent < sec.exponent:
            return False
        else:
            if inst.exponent == sec.exponent:
                if inst.mantissa < sec.mantissa:
                    return False
                else:
                    return True
            else:
                return True
    def lesseq(inst,sec):
        if inst.exponent > sec.exponent:
            return False
        else:
            if inst.exponent == sec.exponent:
                if inst.mantissa > sec.mantissa:
                    return False
                else:
                    return True
            else:
                return True
    def eq(inst,sec):
        if inst.exponent != sec.exponent:
            return False
        else:
            if inst.exponent == sec.exponent:
                if inst.mantissa == sec.mantissa:
                    return True
                else:
                    return False
            else:
                return False
    def noteq(inst,sec):
        if inst.exponent == sec.exponent:
            return False
        else:
            if inst.exponent != sec.exponent:
                if inst.mantissa == sec.mantissa:
                    return False
                else:
                    return True
            else:
                return True
    def less(inst,sec):
        if inst.exponent < sec.exponent:
            return True
        else:
            if inst.exponent == sec.exponent:
                if inst.mantissa < sec.mantissa:
                    return True
                else:
                    return False
            else:
                return False
    def more(inst,sec):
        if inst.exponent > sec.exponent:
            return True
        else:
            if inst.exponent == sec.exponent:
                if inst.mantissa > sec.mantissa:
                    return True
                else:
                    return False
            else:
                return False
    def mod(inst,sec):
        k = inst.div(sec)
        l = k.floor()
        m = l.mult(sec)
        n = inst.sub(m)
        return n
    def tompf(inst):
        return mpf(inst.mantissa * 10**inst.exponent)
    def tologarithm(inst):
        if inst.exponent < 10**10:
            instlog = inst.log10()
            return ('e' + str(instlog.tompf()))
        elif inst.exponent < mpf(tentotentoten):
            instlog = inst.log10()
            instlog = instlog.log10()
            return ('ee' + str(instlog.tompf()))
        else:
            instlog = inst.log10()
            instlog = instlog.log10()
            instlog = instlog.log10()
            return ('eee' + str(instlog.tompf()))
    def tohyper(inst):
        if inst.exponent < 10**10:
            instlog = inst.log10()
            return ('E' + str(instlog.tompf()))
        elif inst.exponent < mpf(tentotentoten):
            instlog = inst.log10()
            instlog = instlog.log10()
            return ('E' + str(instlog.tompf()) + '#2')
        else:
            instlog = inst.log10()
            instlog = instlog.log10()
            instlog = instlog.log10()
            return ('E' + str(instlog.tompf()) + '#3')
    def tosuperlog(inst):
        ten = rectifyint(1,1)
        instlog = inst.slog(ten)
        return ('F' + str(instlog.tompf()))
    def slog(inst,sec,prec = -5):
        x = rectifyint(1,0)
        test = sec.tetra(x)
        unit = rectifyint(1,-2)
        overshoot = False
        while unit.exponent > prec:
            x = x.add(unit)
            test = sec.tetra(x)
            if test.moreeq(inst):
                x = x.sub(unit)
                unit.exponent -= 1
        return x
pi = rectifyint(3.14159265358979323846264338,0)
e = rectifyint(2.718281828459045235760287471352,0)
phi = rectifyint(1.6180339887498948482045868343656381177203,0)
tentotentoten = mpf(10**10)
tentotentoten = 10**tentotentoten
one = rectifyint(1,0)
zero = rectifyint(0,0)
negone = rectifyint(-1,0)
print('huh what')
helper = rectifyint(mpf(1),mpf(1))
a = rectifyint(mpf(1),mpf(100))
a = helper.pow(a)
print('starting!')
b = rectifyint(mpf(3),mpf(0))
b = rectifyint(mpf(1.45),mpf(3))
print(b)
print(a.tosuperlog())
