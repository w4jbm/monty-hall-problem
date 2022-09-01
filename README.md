# monty-hall-problem
Here is another math / probability puzzled called the Monty Hall Problem. I have also created a more generalized version that takes a number from the command line and lets you look at more doors than the original puzzle.

[From Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem), the problem can be stated as:

_Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?_

I certainly don't claim to be a genius, but this is one puzzle where the approach to the right answer was pretty clear to me from the start. It was interesting to generalize the solution to larger numbers of doors.

The most interesting part of the coding was creating a function that returned a random integer in a range while excluding a particular value. We need this to pick a door that is opened by our game show host. (You can use some IF-THEN/ELSE logic also, but the function was a cleaner way to do it.) The logic in the generalized version feels cleaner to me than the original version.

## The Results

Below is a screenshot showing the original Python program results and runs of the generalized version for 3, 4, and 5 doors.

![Sorted Results](https://raw.githubusercontent.com/w4jbm/monty-hall-problem/main/Images/DoorsScreenshot.png)

The explaination on Wikipedia is probably better than anything I can offer. The equations at the end of the generalized version show how to calculate the odds given any number of doors.

## Areas for Future Refinement

The biggest problem is likely to be how I snag the command line argument in the generalized version. I don't think this will work if you invoke the program using the python command instead of depend on the shebang (#!) like I did.

You could easily write a version that let you provide a range of doors or you could vary the number of doors the game show host opens (for example, have ten total doors and they open two of the doors not choosen to reveal goats). At the end of the day, the fundamental answer remains unchanged, it is just how much of an advantage switching offers that will vary. (And to be clear, even if you switch, you only increase your odds of winning--it certainly isn't a way to ensure winning.)

## The fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2022 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
