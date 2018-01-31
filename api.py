# import ATD
import random
import requests
from flask import abort, Flask, jsonify, request

api = Flask(__name__)

questions = ["If you didn't have to sleep, what would you do with the extra time?",
             "What's your favorite piece of clothing you own / owned?",
             "What hobby would you get into if time and money weren't an issue?",
             "What would your perfect room look like?",
             "How often do you play sports?",
             "What fictional place would you most like to go?",
             "What job would you be terrible at?",
             "When was the last time you climbed a tree?",
             "If you could turn any activity into an Olympic sport, what would you have a good chance at winning medal for?",
             "What is the most annoying habit that other people have?",
             "What job do you think you'd be really good at?",
             "What skill would you like to master?",
             "What would be the most amazing adventure to go on?",
             "If you had unlimited funds to build a house that you would live in for the rest of your life, what would the finished house be like?",
             "What's your favorite drink?",
             "What state or country do you never want to go back to?",
             "What songs have you completely memorized?",
             "What game or movie universe would you most like to live in?",
             "What do you consider to be your best find?",
             "Are you usually early or late?",
             "What pets did you have while you were growing up?",
             "When people come to you for help, what do they usually want help with?",
             "What takes up too much of your time?",
             "What do you wish you knew more about?",
             "What would be your first question after waking up from being cryogenically frozen for 100 years?",
             "What are some small things that make your day better?",
             "Who's your go to band or artist when you can't decide on something to listen to?",
             "What shows are you into?",
             "What TV channel doesn't exist but really should?",
             "Who has impressed you most with what they've accomplished?",
             "What age do you wish you could permanently be?",
             "What TV show or movie do you refuse to watch?",
             "What would be your ideal way to spend the weekend?",
             "What is something that is considered a luxury, but you don't think you could live without?",
             "What's your claim to fame?",
             "What's something you like to do the old-fashioned way?",
             "What's your favorite genre of book or movie?",
             "How often do you people watch?",
             "What have you only recently formed an opinion about?",
             "What's the best single day on the calendar?",
             "What are you interested in that most people haven't heard of?",
             "How do you relax after a hard day of work?",
             "What was the best book or series that you've ever read?",
             "What's the farthest you've ever been from home?",
             "What is the most heartwarming thing you've ever seen?",
             "What is the most annoying question that people ask you?",
             "What could you give a 40-minute presentation on with absolutely no preparation?",
             "If you were dictator of a small island nation, what crazy dictator stuff would you do?",
             "What is something you think everyone should do at least once in their lives?",
             "Would you rather go hang gliding or whitewater rafting?",
             "What's your dream car?",
             "What's worth spending more on to get the best?",
             "What is something that a ton of people are obsessed with but you just don't get the point of?",
             "What are you most looking forward to in the next 10 years?",
             "Where is the most interesting place you've been?",
             "What's something you've been meaning to try but just haven't gotten around to it?",
             "What's the best thing that happened to you last week?",
             "What piece of entertainment do you wish you could erase from your mind so that you could experience for the first time again?",
             "If all jobs had the same pay and hours, what job would you like to have?",
             "What amazing thing did you do that no one was around to see?",
             "How different was your life one year ago?",
             "What's the best way to start the day?",
             "What quirks do you have?",
             "What would you rate 10 / 10?",
             "What fad or trend do you hope comes back?",
             "What's the most interesting piece of art you've seen?",
             "What kind of art do you enjoy most?",
             "What do you hope never changes?",
             "What city would you most like to live in?",
             "What movie title best describes your life?",
             "Why did you decide to do the work you are doing now?",
             "What's the best way a person can spend their time?",
             "If you suddenly became a master at woodworking, what would you make?",
             "Where is the most relaxing place you've ever been?",
             "What is the luckiest thing that has happened to you?",
             "Where would you rather be from?",
             "What are some things you've had to unlearn?",
             "What are you looking forward to in the coming months?",
             "What website do you visit most often?",
             "What one thing do you really want but can't afford?",
             "Where do you usually go when you when you have time off?",
             "Where would you spend all your time if you could?",
             "What is special about the place you grew up?",
             "What age do you want to live to?",
             "What are you most likely to become famous for?",
             "What are you absolutely determined to do?",
             "What is the most impressive thing you know how to do?",
             "What do you wish you knew more about?",
             "What question would you most like to know the answer to?"]


@api.route('/question', methods=['GET'])
def get_questions():
    return jsonify(
        {
         "messages": [
           {"text": questions[random.randrange(len(questions))]},
         ]
        }
    )


@api.route('/chatbot/api/check', methods=['POST'])
def check_text():
    if not request.args or 'text' not in request.args:
        abort(400)
    host = 'https://languagetool.org'
    path = '/api/v2/check'
    language = 'en-US'
    text = request.args.get('text')

    headers = {'Content-Type': application/x-www-form-urlencoded}

    uri = host + path

    values = {
        'language': language,
        'text': text
    }

    response = requests.post(uri, data=values, headers=headers)

    response_JSON = response.json();
    message = [];

    for match in response_JSON.matches:
        message += match.message;

    new_list = [{"text": i} for i in message]
    return jsonify(
        {"messages": new_list;})

    # ATD.setDefaultKey(key)
    # errs = ATD.checkDocument(text)
    # str_errs = [str(e) for e in errs]
    # metrics = ATD.stats(text)
    # str_metrics = [str(m) for m in metrics]
    # return jsonify({'errors': str_errs,
    #                 'metrics': str_metrics})

if __name__ == '__main__':
    api.run(debug=True)