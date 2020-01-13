open_file = open('project_twitter_data.csv', 'r')
outfile = open("resulting_data.csv","w")

def strip_punctuation(s):
    for punc in punctuation_chars:
        if punc in s:
            new_word = s.replace(punc, "")
            s = new_word
        else:
            new_word = s
    return new_word

def get_pos(s):
    count_pos = 0
    split_sentence = strip_punctuation(s)
    split_sentence = split_sentence.split()
    for word in split_sentence:
        if word in positive_words:
            count_pos = count_pos + 1
        else:
            continue
    return count_pos


def get_neg(s):
    count_pos = 0
    split_sentence = strip_punctuation(s)
    split_sentence = split_sentence.split()
    for word in split_sentence:
        if word in negative_words:
            count_pos = count_pos + 1
        else:
            continue
    return count_pos



punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def Write_Data(outfile):
    # output the header row
    outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    outfile.write('\n')
    get_lines =  open_file.readlines()
    headerNotUsed = get_lines.pop(0)
    for lines in get_lines:
        list_words = lines.strip().split(',')
        outfile.write("{}, {}, {}, {}, {}".format(list_words[1], list_words[2], get_pos(list_words[0]), get_neg(list_words[0]), (get_pos(list_words[0])-get_neg(list_words[0]))))
        outfile.write("\n")


Write_Data(outfile)
open_file.close()
outfile.close()
