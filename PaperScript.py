from collections import deque
import sys, getopt

stack = deque()
blockMode = False
blockCounter = 1
blockString = ""


def printIntro():
    print('\tUnlike most popular sports, one of the defining characteristics of Golf is the distinction that the player with the lowest score is the winner. From this distinction the programming challenge known as Code Golf gets its name. Much like in regular Golf – where the goal is to complete the course in as few strokes as possible – the goal of Code Golf is to complete a program in as few keystrokes as possible. The notion of trying to complete a program in this manner has been around for about as long as programming generally has not been a recommended programming practice in real world scenarios. A programming manual from 1962 went as far as to state that "it is a time-consuming sport to code with the least possible number of instructions" (Anderson & Gram, 1962). Writing code in a certain way just to prove you can is not always advantageous for performance or readability, so you are generally recommended against writing real-world code in this style. However – as with most professions – the maturing of the artform of programming has allowed for new offshoots of traditional programming orthodoxy to develop. Beginning around the 1990s, programmers began to formalize the challenge of solving problems in as few keystrokes as possible through the recognition of the practice under the modern name of Code Golf (Bacon, 1999). Several communities have grown around Code Golfing since the term’s inception, the largest of which being the Code Golf & Coding Challenges Stack Exchange on the popular technical social media site Stack Exchange. With over eighty-two thousand members, Code Golf SE is the perfect location for programmers to participate in and discuss Gode Golfing.')

def printBasicInfo():
    print('\tThe primary section of the Code Golf Stack Exchange is centered around two types of posts, Challenges and Solutions. A “Challenge” is a problem in which a certain output is requested from the user given a particular input. The complexity of these problems can range from anything as simple as statically outputting the text “Hello World!” to cracking the Enigma code given a text input (Merril, 2016). Recommended templates for “Challenges” are provided by the community to make them easier to write and solve. A “Solution” is a user’s attempt at completing a “Challenge” using a programming language of the user’s choosing.\n\tOn the other end of the Code Golf Stack Exchange is the Meta Section. This area of the site is used for discussion about Code Golfing instead of the activity itself. Here, users can discuss the development of Challenges, strategies for Solutions, and rules and policies.\n\tThe Code Golf Stack Exchange is open to programmers of all skill levels: so long as you can complete the challenges with any length program, you can participate. It is however important to note that it takes a lot of skill to Code Golf well, the challenges you have to complete in Code Golfing are not always trivial and on top of that you of course are expected to optimize your code as much as possible. If you are not up to the task of participating in challenges, you can still find a place in the community by either giving optimization suggestions to fellow members or by creating your own challenges.')

def printTerm():
    print('\tThe Code Golf community exists as a sort of niche of a niche, where programming is already a pretty specialized activity. This adds an extra layer of complication when talking about the specialized language used in the Code Golfing community as there is a lot of terminology that used in the Code Golfing community that would be considered pretty standard for most programmers but wouldn’t make a lot of sense to non-programmers. This language is specialized, but its use has little to do with the Code Golfing community other than its use by consequence of Code Golfing being a type of programming. One instance where Code Golfing separates from regular programming in terms of language usage is the term byte. Technically, the term byte always refers to a set of 8 bits (binary data i.e., on or off, 1 or 0) so any place that data is used the term byte is applicable. However, in the Code Golfing community, byte is almost exclusively used to represent a single character in text as this is used to represent the “size” of the code. Exclusively coining byte for this case has come about as a necessity to standardize the scoring for Code Golf challenges. This usage allows for instant recognition of the size of a program (at least relative to the language it was written in). Even in instances of programming languages that do not feature regular characters, the term byte is ordinarily still applicable such as when writing a program Minecraft, the number of bytes that the corresponding structure takes up in a world file is used (Crump, 2016).')
    
def printEscoInfo():
    print('\tWhen someone imagines a “programming language”, what they think of will probably have a lot to do with how much they know about programming in general. A complete outsider to programming may picture a series of random ones and zeros or the keyboard-mashed text of a hacker in a blockbuster movie. A seasoned software engineer might picture the language they use most in their job or their favorite language for hobby projects. The truth is there is no single programming language that one can consider the prototypical language and similarly there is no prototypical language for Code Golfing. Since the number of instructions necessary to complete a task may vary wildly between programming languages, the Code Golf Stack Exchange community differentiates submissions by the programming language used in the solution. In this way, each Challenge posted is actually many competitions, each between users of a specific programming language.')
    
def printGolfLangInfo():
    print('\tTowards the goal of solving Golfing Challenges, programming languages have been created with the express purpose of Golfing. These “Golfing Languages” intentionally sacrifice readability for conciseness towards the goal of the most optimized code imaginable. Take this solution writing in the golfing language Jelly: “,gþr’§Ạð+¥1#” (hyper-neutrino & carid, 2021). Any human in the world, be it a seasoned programmer or an accountant is going to have a lot of trouble trying to figure out what this code does. None the less, this code is so well golfed that the solution only takes 12 “bytes” where a solution in the popular language Python takes a whopping 536 “bytes”. There has been a lot of discussion about whether or not Golfing Languages are a benefit or a detriment to the community. Even if the rules specify that users only compete within their own language, this can be confusing to new members on the sight. Meanwhile however, the skill required to understand the cryptic nature of writing in these languages makes the challenge of Golfing Languages a worthy feature to many users on the site. (Redwolf & Carid, 2021).')
    
def printConclusion():
    print('\tIt would be easy it jump to the conclusion that it would be redundant to Code Golf in your spare time if your day job was already writing code. The thing is a lot of what goes in to being a software engineer has little to do with writing code from scratch. There is a lot of maintenance that goes along with being a programmer, and that is not usually why people get into writing code. Code Golf is unique because of how different it is. Developers get to use their skills as programmers in a really unique way that can be rewarding in both the spirit of competition and as practice for real world programming. While you might not directly use the type of coding strategies you use when golfing in real world settings, the ability to problem solve under tight restrictions is invaluable for software engineers. Most of all, Code Golfing is a fun hobby for those who want a little extra from programming in a special way.')

def startBlock():
    global blockCounter
    global blockString
    global blockMode
    blockCounter = 1
    blockString = ""
    blockMode = True

def loop():
    global stack
    block = stack.pop()
    count = stack.pop()
    for i in range(count):
        parse(block)
    
charDict = {'i': printIntro, 'b': printBasicInfo, 'r' : printTerm, 'e' : printEscoInfo, 'g' : printGolfLangInfo, 'c' : printConclusion, '<' : startBlock, 'L' : loop}



stack.append(2)

def parse(code : str):
    global blockCounter
    global blockMode
    global blockString

    for char in code:
        if blockMode:
            if char == '<':
                blockCounter += 1
            elif char == '>':
                blockCounter -= 1
            
            if blockCounter == 0:
                stack.append(blockString)
                blockMode = False
            else:
                blockString += char
        elif char in charDict:
            charDict[char]()

def main():
    if len(sys.argv) < 2:
        exit(2)

    fileName = sys.argv[1]

    for arg in sys.argv[2:]:
        stack.append(int(arg))

    with open(fileName) as f:
        code = f.read()

    parse(code)

    


if __name__ == "__main__":
    main()
