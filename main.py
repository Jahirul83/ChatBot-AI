import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])




    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    #response(long.R_DEPT, ['how', 'many', 'dept'], required_words=['many', 'dept'])
    response(long.R_Greating , ['assalamuwalikum'])
    response(long.Uni_Ranking, ['ranking','of','iiuc','in','bangladesh'], required_words=['ranking','bangladesh'])
    response(long.Uni_tot_dept, ['how','many','dept','in','iiuc'], required_words=['many','dept'])
    response(long.cse_chairman_no, ['chairman','head','cse','number','phone'], required_words=['chairman','number','cse','phone'])
    response(long.admission_link,['give','me','the','admission','link'],required_words=['admission','link'])
    response(long.location,['iiuc','location'],required_words=['iiuc','location'])
    response(long.hostel,['hostel'],required_words=['hostel'])
    response(long.min_gpa_EP,['minimum','gpa','engineering','pharma'],required_words=['minimum','gpa','engineering','pharma'])
    response(long.min_gpa_ell,['minimum','gpa','ell'],required_words=['minimum','gpa','ell'])
    response(long.min_gpa_law,['minimum','gpa','law'],required_words=['minimum','gpa','law'])
    response(long.min_gpa_econ,['minimum','gpa','economic','&', 'banking'],required_words=['minimum','gpa','economic','&', 'banking'])
    response(long.cost_ell,['cost','ell'],required_words=['cost','ell'])
    response(long.cost_eng, ['cost', 'engineering'], required_words=['cost', 'engineering'])
    response(long.cost_law, ['cost', 'law'], required_words=['cost', 'law'])
    response(long.cost_econ, ['cost', 'economic','&','banking'], required_words=['cost', 'economic','&','banking'])
    response(long.cost_parma,['cost','pharmacy'],required_words=['cost','pharmacy'])
    response(long.cost_arabic,['cost','arabic'],required_words=['cost','arabic'])
    response(long.library,['library'],single_response=True)
    response(long.cafe,['cafe','cafeteria'],single_response=True)
    response(long.two_campus,['campus','separate'],required_words=['campus','separate'])
    response(long.transport,['transport','transportation'],single_response=True)
    response(long.admission_fee,['admission','fee'],required_words=['admission','fee'])
    response(long.waiver,['waiver'],single_response=True)


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
