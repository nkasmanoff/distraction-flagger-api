


def check_relevance(_input,_topic):
    """
    Simple rule based approach for checking if a webpage is on topic or not. 

    Gets the word overlap between the input and topic. 
    
    If there is at least one word from the topic in the input, returns 0. Otherwise, returns 1
    
    """

    # split the input into words
    input_words = _input.split()

    # split the topic into words
    topic_words = _topic.split()

    # get the word overlap between the input and topic
    overlap = set(input_words).intersection(set(topic_words))

    # if there is at least one word from the topic in the input, return 0. Otherwise, return 1
    if len(overlap) > 0:
        return 0
    else:
        return 1