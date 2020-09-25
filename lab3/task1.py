if __name__ == '__main__':
    hotel_rooms = [('Ann', 400), ('Elizabeth', 103), ('Mr. McMullen', 202), ('Mrs. Smith', 200)]

    for (name, room) in hotel_rooms:
        print('{0}, {1}! Your room is {2}.'.format(('Good morning' if ('Mr.' in name)
                                                                      or ('Mrs.' in name)
                                                                      or ('Miss' in name)
                                                                      or ('Ms.' in name) else 'Hello'), name, room))
