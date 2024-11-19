




def str_split(str,splitter):
    str_list  = []
    temp_str = ""
    timer = 0
    # appends the rest into a list
    for char in str:
        timer +=1
        temp_str = temp_str + char
        if len(temp_str) == splitter:
            str_list.append(temp_str)
            temp_str = ""
            

    if len(temp_str) > 0:
        str_list.append(temp_str)




    return str_list


