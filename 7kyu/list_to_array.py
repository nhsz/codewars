# http://www.codewars.com/kata/557dd2a061f099504a000088/

def list_to_array(lst):
    array = []
    try:
        while True:
            array.append(lst.value)
            lst = lst.next
    except:
        return array
