"""
The purpose of this question is to flip a 0 bit to a 1 
bit in order to find the longest sequence of 1's

Example:
    >>> FlipBit(int(00001111110111011111001111110000, base=2))
    10

    >>> FlipBit(int(1111111111, base=2))
    10

    >>> FlipBit(int(0000000000, base=2))
    0

Edge cases:
    >>> FlipBit(None)
    TypeError('a binary integer is expected input')
"""

class Buffer(object):
    
    def __init__(self):
        self.length = 0
        self.zero_seen = False
        self.buffer = []

    def __len__(self):
        return self.length
    
    def clear(self):
        self.length = 0
        self.zero_seen = False
    
    def push(self, bit):
        if bit == 0:  
            if self.length > 0 and not self.zero_seen:
                self.length += 1
                self.zero_seen = True
                self.buffer.append(bit)
            elif self.zero_seen:
                length = self.length
                print("Buffer before clear: {0}".format(self.buffer))
                self.clear()
                return length
        else:
            self.length += 1
            self.buffer.append(bit)
        
        return self.length

    def peek(self):
        return self.buffer


class Bits(object):

    def __init__(self):
        self.longest_string = 0
        self.first_zero = False
        self.buffer_1 = Buffer()
        self.buffer_2 = Buffer()

    def flip_bit(self, number):
        if not isinstance(number, int):
            raise TypeError('a binary integer is expected input')

        while number:
            bit = number & 1
            self.push_to_buffer(bit)
            
            # Shift the number to the right 1 place
            number >>= 1

        return self.longest_string

    def push_to_buffer(self, value):
        if not self.first_zero:
            buffer_1.push(value)
        if self.first_zero:
            b1 = buffer_1.push(value)
            b2 = buffer_2.push(value)
            self.longest_string = max(self.longest_string, b1, b2)

        print("/nBuffer 1: {0}".format(buffer_1))
        print("Buffer 2: {0}/n".format(buffer_2))
