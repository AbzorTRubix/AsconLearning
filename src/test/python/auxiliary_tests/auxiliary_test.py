from ascon import parse, pad
import secrets

TEST_CASES = 50

def test_parse():
    assert parse("1011011000011000",3) == ["101","101","100","001","100","0"]
    assert parse(format(77,'b'),2) == ["10","01","10","1"]
    assert parse(format(178943243,'b'),7) == ["1010101","0101001","1101010","0001011"]
    assert parse(format(13294781239487123948712394871239487123,"b"),2) == ["10","10","00","00","00","00","01","11","10","11","01","01","00",
                                                                           "10","10","01","11","00","11","01","11","01","01","11","01","01",
                                                                           "10","10","11","11","10","01","10","11","10","01","11","01","00",
                                                                           "00","01","00","10","01","00","01","01","01","11","00","00","11",
                                                                           "10","10","00","10","11","10","10","01","00","11"]
    for _ in range(TEST_CASES):
        num = secrets.randbits(128)
        r = secrets.choice(range(1,11))
        b = format(num,"b")
        expected_result = [b[i:i+r] for i in range(0,len(b),r)]
        assert parse(b,r) == expected_result

def test_pad():
    assert pad("1011",7) == "1011100"
    assert pad("1",3) == "110"
    for _ in range(TEST_CASES):
        bit_len = secrets.choice(range(1,128))
        num = secrets.randbits(bit_len)
        r = secrets.choice(range(bit_len,128))
        b = format(num,"b")
        expected_result = b
        print(r,len(b),sep=" ")
        if(len(expected_result) != r):
            expected_result = expected_result + "1"
            while(len(expected_result) != r):
                expected_result = expected_result + "0"
        else:
            #output is a multiple of r, not guarenteed to be length r, i.e. equal length X is essentially doubled in size
            expected_result = expected_result + "1" + "0"*(r - 1)
        assert len(pad(b,r)) == len(expected_result)
        assert pad(b,r) == expected_result

