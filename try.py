

def convert_list_to_str(lister,final_term):
    global home_screen_text
            string = ""
            for letter in lister:
                if len(string) - 1  == final_term:
                    home_screen_text = 1
                    print("done!!")
                    print(final_term)
                    print(string)
                    break
                else:
                    string = string + letter
            print(string)
            return string