def RLC(message):
    message_list = []
    count = 1
    for i in range(0, len(message)):
        if i + 1 < len(message) and message[i] == message[i+1]:
            count += 1
        else:
            message_list.append(message[i])
            message_list.append(count)
            count = 1
    print(message_list)
    
    buf = ""
    for index, value in enumerate(message_list):
        if index % 2 == 0:
            buf += "(" + str(value) + ","
        else:
            buf += str(value) + "),"
    
    print(buf.rstrip(','))

