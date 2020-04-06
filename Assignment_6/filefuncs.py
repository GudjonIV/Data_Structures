# Author: Guðjón Ingi Valdimarsson
# Date: 06.04.2020

# -------- Word file functions --------
def get_file_list(file):
    """ Takes in a filename and returns a list of lines from the file.
        Raises exception if file does not exist """
    ret_list = []
    try:
        with open(file, "r") as f:
            for line in f:
                ret_list.append(line.strip())
    except FileNotFoundError:
        raise Exception("File '{}' does not exist".format(file))
    f.close()
    return ret_list

def add_words_to_file(file, wordslist):
    """ Adds new words to the word file """
    with open(file, "a") as f:
        for word in wordslist:
            f.write("\n"+word)
    f.close()
    print ("Words succesfully added")

# -------- Stick figure function --------
def get_stickfigures(file):
    """ Gets the stick figures from file and returns a list split by figure """
    ret_list = []
    try:
        with open(file, "r") as f:
            string = ""
            for line in f:
                if line == "\n":
                    ret_list.append(string)
                    string = ""
                else:
                    string += line
    except FileNotFoundError:
        raise Exception("File '{}' does not exist".format(file))
    f.close()
    return ret_list

# -------- Profile file functions --------
def get_profiles(file):
    """ Takes in a file and returns a dictionary of profiles with id as key """
    profile_dict = {}
    with open(file, "r") as f:
        next(f)
        for line in f:
            line = line.strip()
            line = line.split(",")
            line[3] = line[3].split(";")
            line[1] = int(line[1])
            line[2] = int(line[2])
            line[4] = int(line[4])
            profile_dict[int(line[0])] = line[1:]
    return profile_dict

def save_profiles(file, profile_dict):
    """ Takes in a dictionary of profiles and saves them to the file """
    with open(file, "w") as f:
        f.write("id,wins,losses,history,score,name")
        for key, value in profile_dict.items():
            key = str(key)
            value = [str(x) if not isinstance(x, list) else x for x in value] # Change everything to string except for the histroy list
            value[2] = ";".join(value[2])
            f.write("\n{},{}".format(key, ",".join(value)))