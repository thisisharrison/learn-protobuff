from google.protobuf import json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumeration_pb2 as enumeration_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2
import proto.addressbook_pb2 as addressbook_pb2


# Instantiate a simple message
def simple():
    return simple_pb2.Simple(
        id=10,
        is_simple=True,
        name='hello',
        sample_list=[1,2,3]
    )

# Instantiate a complex message
def complex():
    message = complex_pb2.Complex()
    message.single_dummy.id = 1
    message.single_dummy.name = 'First'
    message.list_of_dummy.add(id=2, name='Second')
    message.list_of_dummy.add(id=3, name='Third')
    message.list_of_dummy.add(id=4, name='Fourth')
    return message

# Using enum
def use_enum():
    return enumeration_pb2.Enumeration(
        eye_color=enumeration_pb2.EYECOLOR_BROWN
        # eye_color = 3 would also work
    )

# Using oneof
def use_oneof():
    '''
    All the fields in a oneof share memory, and at most one field can be set at the same time.
    Setting a oneof field will automatically clear all other members of the oneof. 
    So if you set several oneof fields, only the last field you set will still have a value.
    '''
    message = oneofs_pb2.Result(this='this')
    print(message)
    
    # 'this' is cleared
    message.that = 'that'
    print(message)

# Using map
def use_map():
    '''
    Will create key if key does not exist
    '''
    message = maps_pb2.DrinkMap()
    message.menu['latte'].size = 'large'
    message.menu['latte'].price = 40
    
    message.menu['espresso'].size = 'small'
    message.menu['espresso'].price = 20
    
    print(message)

# Reading and Writing binary 
def file(message): 
    '''
    Write to disk and then Read from disk
    '''
    path = 'simple.bin'

    print('Write to file')
    print(message)

    with open(path, 'wb') as f:
        # SerializeToString: serializes the message and returns it as a string. 
        # Note that the bytes are binary, not text; we only use the str type as a convenient container.
        bytes_to_str = message.SerializeToString()
        f.write(bytes_to_str)
    
    print('Read from file')

    with open(path, 'rb') as f:
        MessageType = type(message)
        # FromString: Returns a new message instance deserialized from the given string.
        message2 = MessageType().FromString(f.read())
        print(message2)

# Serializing and Parsing JSON
def json(message, MessageType):
    json = to_json(message)
    print('JSON')
    print(json)
    print('-' * 10)

    message = from_json(json, MessageType)
    print('MESSAGE')
    print(message)

def to_json(message):
    return json_format.MessageToJson(
        message,
        # options
        indent=None, # one-line
        preserving_proto_field_name=True # Snake Case instead of Camel
    )

def from_json(json, MessageType):
    return json_format.Parse(
        json, 
        MessageType(),
        ignore_unknown_fields=True
    )

# Write Address Book
def create_address_book():
    '''
    Create address book, and instantiate a person (.add)
    '''
    address_book = addressbook_pb2.AddressBook()

    done = False
    
    while not done:
        person = address_book.people.add()
        create_person(person)
        done = input('Are you done? (y/N)') == 'y'
    
    path = 'address.bin'

    with open(path, 'wb') as f:
        f.write(address_book.SerializeToString())
    
    return address_book

# Write person
def create_person(person):
    person.id = int(input('id: '))
    person.name = input('name: ')
    person.email = input('email: ')

    done = False

    # Instantiate PhoneNumber
    phones_number = person.phones.add()

    while not done: 
        phones_number.number = input('phone number: ')
        phone_type = input('What type? ').strip()

        if phone_type == 'mobile': 
            phones_number.type = addressbook_pb2.Person.PhoneType.MOBILE
        elif phone_type == 'home': 
            phones_number.type = addressbook_pb2.Person.PhoneType.HOME
        else:
            phones_number.type = addressbook_pb2.Person.PhoneType.WORK
        
        done = input('Is that it? (y/N)') == 'y'

# Read person
def read_address_book():
    path = 'address.bin'
    address_book = addressbook_pb2.AddressBook()

    with open(path, 'rb') as f:
        address_book.ParseFromString(f.read())
    
    print_people(address_book)

def print_people(address_book):
    for person in address_book.people:
        print(person)

if __name__ == '__main__':
    # print(simple())
    # print(complex())
    # print(use_enum())
    # use_oneof()
    # use_map()
    # file(simple())
    # json(complex(), complex_pb2.Complex)

    # https://developers.google.com/protocol-buffers/docs/pythontutorial#writing-a-message
    create_address_book()
    read_address_book()
