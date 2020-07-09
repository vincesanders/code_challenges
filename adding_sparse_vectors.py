'''
     0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7
A = {1,0,0,0,0,0,0,0,0,4,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,7}
B = {0,0,0,7,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7}

head1 = {0, 1} -> {9, 4} -> {10, 10} -> {26, 6} -> {27, 7}
head2 = {3, 7} -> {10, 1} -> {27, 1}

output = a0*b0+a1*b1+..........an*bn

output = 1x0 + 0x7 + 4x0 + 8x1 + 6x0 + 7x7 = 57

1. Store the index.
2. store the non-zero value for the index.

1. traverse thru both the linked lists and make sure if one of the list has reached to its end, exit
2. if indexes are same, multiply them, also move both the linked list to next elements
3. if head1 index is smaller, move to the next element of head1
4. If index of head2 is smaller, move to the next element of n2
'''

class Node:
    def __init__(self, value=None):
        self.value = value # Vector Element
        self.next = None

class VectorElement:
    def __init__(self, index, value):
        self.index = index
        self.value = value

def sparseVectorMultiplication(head1, head2):
    if head1 is None or head2 is None:
        return 0

    first_vector_list = head1
    second_vector_list = head2
    total = 0

    while first_vector_list.value is not None and second_vector_list.value is not None:
        if first_vector_list.value.index == second_vector_list.value.index:
            total += (first_vector_list.value.value * second_vector_list.value.value)
            first_vector_list = first_vector_list.next
            second_vector_list = second_vector_list.next
        elif first_vector_list.value.index < second_vector_list.value.index:
            first_vector_list = first_vector_list.next
        else:
            second_vector_list = second_vector_list.next

    return total

array1 = [1,0,0,0,0,0,0,0,0,4,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,7]
array2 = [0,0,0,7,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7]

array1VE = []
array2VE = []

for i in range(len(array1)):
    array1VE.append(VectorElement(i, array1[i]))
    array2VE.append(VectorElement(i, array2[i]))

LinkedList1 = Node()
LinkedList2 = Node()
head1 = LinkedList1
head2 = LinkedList2

for vector in array1VE:
    if vector.value > 0:
        LinkedList1.value = vector
        LinkedList1.next = Node()
        LinkedList1 = LinkedList1.next

for vector in array2VE:
    if vector.value > 0:
        LinkedList2.value = vector
        LinkedList2.next = Node()
        LinkedList2 = LinkedList2.next

print(sparseVectorMultiplication(head1, head2))