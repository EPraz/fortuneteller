from django.shortcuts import render
import random


fortuneList = [
   "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"
]

pets = [
  { "petname": "Fido", "animal_type": "dog"},
  { "petname": "Clementine", "animal_type": "cat"},
  { "petname": "Cleo", "animal_type": "cat"},
  { "petname": "Oreo", "animal_type": "dog"},
]

# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    fortune2 = random.choice(fortuneList)
    context = {
        "fortune": fortune,
        "fortune2": fortune2,
        "fortuneList": fortuneList,
        "pets": pets,
        }

    return render(request, "randomfortune/fortune.html", context)
