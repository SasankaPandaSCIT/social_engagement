# superclass(base class) Comments
# Comments should have the following instance variables: text, likes, dislikes and is_flagged.
class Comment():
    def __init__(self, Comment_text, Comment_likes, comment_dislikes, comment_is_flagged):
        self.text = Comment_text
        self.likes = Comment_likes
        self.is_flagged = comment_is_flagged
        self.dislikes = comment_dislikes

    #  print_info prints out each of the comment's variables.
    def print_info(self):
        print("Comment:", self.text)
        print("Likes:", self.likes, ", Dislike:", self.dislikes, ", Is Flagged:", self.is_flagged )


# subclass(Derived class) Question that inherit properties from Comments
# it has additional two valriables - answer and topic

class Question(Comment):
    def __init__(self, Quesion_text, Question_likes, QUestion_dislikes, Question_is_flagged, Question_Topic, QUestion_Answer):
        self.Topic = Question_Topic
        self.Answer = QUestion_Answer
        super().__init__(Quesion_text, Question_likes, QUestion_dislikes, Question_is_flagged)

    # prints additional variables in addition to variables in comments
    def print_info(self):
        super().print_info()
        print("Topic: ", self.Topic)
        print("Answer:", self.Answer)

# function to load the data to a list
def load_list(list):
    # load the data using comments class
    list.append(Comment('pineapple on pizza', 10, 10, True))
    list.append(Comment('I liked this video', 30, 20, False))
    list.append(Comment('LOL', 4, 1, False))

    # load the data using Questions class
    list.append(Question('Should I dislike Shrek?', 1, 15, True, 'Blasphemy', "No you shouldn't"))
    list.append(Question('Why did the programmer quit their job?', 12, 12, False, 'Coding',
                         "They didn't get arrays"))


# print all the rows from list using functions included in the class
def print_all(list):
    print("** ALL COMMENTS & QUESTIONS **\n")
    for row in list:
        row.print_info()
        print("\n")

# print rows with is_flagged variable as False from list using functions included in the class
def print_unflagged(list):
    print("** UNFLAGGED COMMENTS & QUESTIONS **\n")
    for row in list:
        if row.is_flagged == False:
            row.print_info()
            print("\n")

# function that calcualtes average engagement score
def average_engagement(list):
    print("** UNFLAGGED COMMENTS & QUESTIONS **\n")
    running_sum = 0
    counter = 0
    for row in list:
        running_sum = running_sum + (row.likes if row.likes is not None else 0)

        running_sum = running_sum + (row.dislikes if row.dislikes is not None else 0)
        counter = counter + 1

    print("\nAverage Engagement:",round(running_sum/counter,2), "like and dislikes per commment")

# main program that calls all the functions
mylist = []
load_list(mylist)
print_all(mylist)
print_unflagged(mylist)
average_engagement(mylist)

