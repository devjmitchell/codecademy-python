def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
                break
        return True

print "Are the following numbers prime?"
print "-1: " + str(is_prime(-1))
print "0: " + str(is_prime(0))
print "1: " + str(is_prime(1))
print "2: " + str(is_prime(2))
print "3: " + str(is_prime(3))
print "4: " + str(is_prime(4))
print "5: " + str(is_prime(5))
print "6: " + str(is_prime(6))
print "7: " + str(is_prime(7))
print "8: " + str(is_prime(8))
print "9: " + str(is_prime(9))
print "\n"

your_input = raw_input("Enter a number to see if it is prime:")
print is_prime(int(your_input))
