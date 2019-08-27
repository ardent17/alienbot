# importing regex and random libraries
import re
import random

# potential negative responses
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
# keywords for exiting the conversation 
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
# random starter questions
random_questions = (
    "Why are you here? ", 
    "Are there many humans like you? ", 
    "What do you consume for sustenance? ", 
    "Is there intelligent life on this planet? ", 
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet?"
    )

name = ""

alienbabble = (
    # Your planet...
  {r'.*\s*your planet':
    ("My planet is a utopia of diverse organisms and species. ",
    "I am from Opidipus, the capital of the Wayward Galaxies. ")
    },
  # why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
     ("What makes you think I {0}? ",
      "Do I {0}? ",
      "Why should I {0}? ")
    },
  # why...?
    {r'.*why\s+.*':
     ("Because I want to harvest your body. ",
      "I heard Earth girls were easy. ",
      "This vibe is siiiiq. ")
    },
  # what...?
    {r'.*what\s+.*':
     ("What do you think? ",
      "Why do you ask? ",
      "If you examine your own reason for asking that question, what do you determine? ")
    },
  # it is...
    {r'.*it\s+is':
     ("Are you sure? ",
      "Can you validate that? ",
     "I'm gonna need some more supporting evidence. ")
    },
  # I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
     ("Don't say, I think. Act like you know, as if you were any mediocre white man. ",
      "Why do you think {0}? ")
    },
  # Other responses
    {r'.*':
     ("Please tell me more. ",
      "Tell me more! ",
      "Why do you say that? ",
      "I see. Can you elaborate? ",
      "Interesting. Can you tell me more? ",
      "I see. How do you think? ",
      "Why? ",
      "How do you think I feel when you say that? ")
    }
)

# Define greet() below:
def greet():
  name = input("What is your name? ")
  will_help = input("Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(name))
  for resp in negative_responses:
    if resp in will_help:
      print("Peace bruh, enslave yr planet l8r")
      return False
  return True
    

greet()

# Define make_exit() here:

def make_exit(reply):
  for command in exit_commands:
    if command in reply:
      print("l8r g8r")
    return True
  return False

make_exit('see you later')

# Define alienbot() next:
def alienbot(reply):
  reply = input(random.choice(random_questions)).lower()
  if greet is True:
    return reply
  else:
    reply = converse(reply)
    return reply
  		
#alienbot('ask me a question')

# Define converse() below:
def converse(reply):
  for pair in alienbabble:
    for regex_pattern, alien_answer in pair.items():
      found_match = re.match(regex_pattern, reply)
      if found_match:
        alien_answer = random.choice(alien_answer)
        formatted_alien_answer = alien_answer.format(*[reflect(matching_group) for matching_group in found_match.groups()])
        reply = input(formatted_alien_answer).lower()
        return reply

converse('reply')

# dictionary used to switch pronouns 
# and verbs in responses
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}
def reflect(response):
  words = response.split()
  for index, word in enumerate(words):
    if word in reflections:
      words[index] = reflections[word]
  return ' '.join(words)

alienbot('reply')