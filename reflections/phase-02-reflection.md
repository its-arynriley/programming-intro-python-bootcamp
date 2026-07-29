# Phase Reflection

## Phase

Phase: 02 - Variables, input, and athlete profile

Branch: phase-02-athlete-profile

Pull request: Added a basic athlete profile and a phase reflection.

## What I Built

I built an athlete profile in `app/app.py` that asks the user for:
- Athlete name
- Graduation year
- Primary event
- Current PR
- Goal mark

Then the app prints the profile back in a clean format and tells the user whether they reached the goal.

## What I Learned

I learned how to use `input()` to get text from the user and how to convert text into numbers using `int()` and `float()`.
I also learned that the app must collect data before it can print it, or Python will say a variable is not defined.

## Commands I Used

```bash
cd app
python3 app.py
cd ..
```

## Bugs Or Mistakes

I had a problem where the app tried to print values before asking for them. I fixed it by moving the input lines above the print block.

## AI Usage

Did I use AI?
Yes

What did I ask?
How to format the app and fix the Python error.

What did AI help me understand?
That I needed to save the file and make sure the input variables were defined before printing them.

Can I explain every line of code in my PR?
Yes

## Demo Notes

Show the app running from `app/app.py` and entering values for the athlete profile. Then show the printed summary and goal message.

## What variables are
Variables are named storage boxes for data.

## What input() does
`input()` asks the user to type something and returns that text.

## Why input() returns text
Because everything typed by the user starts as text, even numbers like `42`.

## What int() or float() does
`int()` converts text to a whole number and `float()` converts text to a decimal number.

