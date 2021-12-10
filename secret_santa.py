# Secret Santa Code Program 
# -------------------------
# 
# Author: Esteban Perez
#
# link: https://discuss.codecademy.com/t/challenge-secret-santa/634327

from random import shuffle, choice

from sklearn.datasets import load_files

def main(file="names.txt"):
    # load the file .txt
    try:
        with open(file) as f:
            lines = f.readlines()
            if len(lines) == 0: # check if the file is not empty
                print("The file {} is empty".format(file))
                return
    except:
        print("Error: the file {} cannot be found or could not be loaded".format(file))
        return

    # create a list of participants and removing the symbol \n
    participants = []
    for line in lines:
        participants.append(line.replace("\n", ""))
    
    # delete duplicate items if there are any
    participants = list(set(participants))

    # check if the list is not even            
    if len(participants) % 2 != 0:
        sel_particip_out = choice(participants)
        participants.remove(sel_particip_out)
        create_list(participants)
        print(sel_particip_out + " must be found a partner to exchange gifts!!")
        generate_christmas()
    else:
        create_list(participants)
        generate_christmas()


def create_list(participants):
    """
    Generates a list of participants by entering a 
    list with its members.

    Args:
        participants (list): list of all participants
    """
    shuffle(participants)
    print("\n")
    print("                  *                             *            *   ")
    print("     +----------------------------------------------------------+")
    print("     |          ***          Secret Santa          ***          |")
    print("     +----------------------------------------------------------+")
    print("     |                                                          |")
    n = 0
    for i in range(0, len(participants), 2):
        name1 = participants[i] + ' ' * (20 - len(participants[i]))
        name2 = participants[i+1] + ' ' * (20 - len(participants[i+1]))
        print("     |    ", name1, " <——>     ", name2, "|")
    print("     |                                                          |")
    print("     +----------------------------------------------------------+")
    

def generate_christmas():
    """
    Generate an ascii christmas image 
    from a txt file
    """
    try:
        with open('santa_claus.txt') as f:
            lines = f.readlines()

        christmas = []
        for line in lines:
            christmas.append(line.replace("\n", ""))
            
        for line in christmas:
            print(line)
    except:
        return


if __name__ == "__main__":
    import sys
    if len (sys.argv) == 1:
        main()
    else:
        main(str(sys.argv[1]))