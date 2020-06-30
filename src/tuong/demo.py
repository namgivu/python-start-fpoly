def demo():
    # declare 2 arrays
    PASS = ["18v200628",
            "6",
            "4v200628",
            "3v200628",
            "5v200628",
            "1v200628",
            "6v200628"]
    FAIL = [ "17v200628",
            "30v200628",
            "20v200628",
            "15v200628",
            "25v200628",
            "23v200628",
            "26v200628",
            "28v200628",
            "7v200628",
            "22v200628",
            "27v200628",
            "10v200628",
            "19v200628",
            "29v200628",
            "13v200628",
            "12v200628",
            "8v200628",
            "11v200628",
            "16v200628",
            "21v200628",
            "2v200628"]

    # sort by alphabet then length
    PASS.sort()
    PASS.sort(key=len)

    FAIL.sort()
    FAIL.sort(key=len)

    # print arrays after sorted
    print('Sorted list PASS:', PASS,'\n Sorted list FAIL: ',FAIL)

    return PASS, FAIL
