import random
import os

def read_cue_card(line):
    """Return formatted cuecard."""
    front = ""
    x = 0
    is_front = True
    while line[x] != "/": #a.k.a before the separator "/" has appeared
        front += line[x]
        x += 1
    back = ""
    x += 1
    while x < len(line): #output the rest of the line
        back += line[x]
        x += 1
    return front, back


def read_cuecard_set(topics):
    """Print cuecards in specified file.
    
    Goes through the lines in the file, the cue cards, printing
    when prompted allowing the user to pass through the cue cards
    at their own pace.

    Args:
        topics -- a list of all currently available sets of cue cards.
    """
    topic_name = input("Enter name of first set of cuecards: ")
    topic_name = topic_name + ".txt"
    if topic_name not in topics:
        print("Invalid topic name.")
        return
    topic = open(topic_name,'r') #opens the file of cue cards relating to topic to read
    lines = topic.readlines()   #creates a list containing each line in the file
    end = False
    while len(lines) > 0 and not end:    #while there is still lines to be read
        line = lines[random.randint(0,len(lines)-1)]  #randomly select a line
        front,back = read_cue_card(line)
        print("Front of cue card: " + front)
        cont = input("When ready to see back of cue card, press Enter")
        print("Back of cue card is: " + back)
        cont = input("When ready to continue, press Enter, or to exit press 'X'")
        if cont == "X" or cont == "x":
            break
        else:
            lines.remove(line)
    print("Cue Card Reading has Finished")
    topic.close()
    return


def add_cuecards(topics, edit_type):
    """Add specified number of cue cards to a file.
    
    Adds a specified number of cue cards to an existing set if edit_type
    is "a" or to a new set if edit_type is "w". The user is able to
    input the specific cue cards in turn, then confirm that it's
    correct.

    Args:
        topics -- a list of all currently available sets of cue cards.
        edit_type -- a string that is "w" or "a".
    """
    topic_name = input("Please enter the Topic Name: ")
    topic_name = topic_name + ".txt"
    if topic_name not in topics and edit_type == "a":   #if the topic does not already exist, and is expected to
        print("Invalid topic name.")
        return
    elif topic_name not in topics and edit_type == "w":     #new topic is added to list of topics
        topics.append(topic_name)
    topic = open(topic_name, edit_type)
    numcards = int(input("How many cuecards do you want to add? "))
    numcardsleft = numcards
    end = False
    while numcardsleft > 0 and not end:
        front = input("Enter the front of the cue card: ")
        back = input("Enter the back of the cue card: ")
        cuecard = front + "/" + back
        print("The cue card looks like this: '" + cuecard + "' is this correct? Y/N, or any other key to finish adding cuecards early.")
        correct = input()
        if correct == "Y" or correct == "y":
            numcardsleft -= 1
            topic.write(cuecard + '\n')
        elif correct == "N" or correct == "n":
            print("Enter the cue card again...")
        else:
            end = True
    print("Cue Card set finished.")
    topic.close()
    return
    
def delete_set(topics):
    """Delete a set of cue cards."""
    topic_name = input("Please enter the Topic to be deleted: ")
    topic_name = topic_name + ".txt"
    if topic_name not in topics:
        print("Invalid topic name.")
        return
    os.remove(topic_name)       #removes the file/set of cue cards from the folder
    topics.remove(topic_name)
    print("\n" + topic_name + " has been deleted.\n")
    return

def print_topics(topics):
    """Print list of topics."""
    print("Existing topics: \n")
    for i in range(len(topics)):
        print("     - " + topics[i] + "\n")
    return

def main_menu(topics):
    """Print menu for making selections on using the cue cards.
    
    This is the main/opening function that allows navigation
    between the different functions of this program.

    Args:
        topics -- a list of all currently available sets of cue cards.
    """
    print("Select command from following list by entering the associated number/letter:")
    print("     1. Read a set of cuecards")
    print("     2. Add a new set of cuecards")
    print("     3. Add to an existing set of cuecards")
    print("     4. Delete a set of cuecards")
    print("     5. View existing topics")
    print("     X. Exit program")
    menu_choice = input()
    if menu_choice == "1":
        read_cuecard_set(topics)
        main_menu(topics)
    elif menu_choice == "2":
        add_cuecards(topics,"w")
        main_menu(topics)
    elif menu_choice == "3":
        add_cuecards(topics,"a")
        main_menu(topics)
    elif menu_choice == "4":
        delete_set(topics)
        main_menu(topics)
    elif menu_choice == "5":
        print_topics(topics)
        main_menu(topics)
    elif menu_choice == "X" or menu_choice == "x":
        print("Thank you for using this program")
        return
    else:
        print("The option you entered was invalid, please try again:")
        main_menu(topics)

topics = os.listdir("C:\\Users\\ncoia\\Documents\\University\\cue_card_program")
topics.remove("LICENSE")
topics.remove(".git")                       #removes files that are known not to be topics from the list of topics.
topics.remove("cue_card_reader.py")
topics.remove("README.md")
main_menu(topics)