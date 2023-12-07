print('hi')

# making a basic 4 node dictionary list
# linked list actual syntax is different

head = {
    'value': 11,
    'next': {
        'value': 15,
        'next': {
            'value': 10,
            'next': {
                'value': 15
            }
        }
    }
}

print(head['next']['next']['value'])
# print(my_linked_list.head.next.next.value) this is actual linked list syntax, hasnt been taught yet so doesnt work
