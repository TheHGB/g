import random
import time
import subprocess as sp
def printBanner():
    heart = """              ......           ......
           ,ad8PPPP88b,     ,d88PPPP8ba,
          d8P        Y8b, ,d8P        Y8b
         dP             8a8            `Yd
         8(              '              )8
         I8                             8I
          Yb,                         ,dP
            8a,                     ,a8
              8a,                 ,a8
                Yba             adP   
                 `Y8a         a8P'
                   `88,     ,88'
                      8b   d8
                       8b d8
                       `888'
                         '
                         """
    print heart
    print "Welcome to the love calculator where we will use very complex math to \nasign a value to the probability of love between you and your interest\nbased solely in your names, because thats how shit works "

def printBannerG():
    gentoo="""     -/oyddmdhs+:.
     -o${c2}dNMMMMMMMMNNmhy+${c1}-`
   -y${c2}NMMMMMMMMMMMNNNmmdhy${c1}+-
 `o${c2}mMMMMMMMMMMMMNmdmmmmddhhy${c1}/`
 om${c2}MMMMMMMMMMMN${c1}hhyyyo${c2}hmdddhhhd${c1}o`
.y${c2}dMMMMMMMMMMd${c1}hs++so/s${c2}mdddhhhhdm${c1}+`
 oy${c2}hdmNMMMMMMMN${c1}dyooy${c2}dmddddhhhhyhN${c1}d.
  :o${c2}yhhdNNMMMMMMMNNNmmdddhhhhhyym${c1}Mh
    .:${c2}+sydNMMMMMNNNmmmdddhhhhhhmM${c1}my
       /m${c2}MMMMMMNNNmmmdddhhhhhmMNh${c1}s:
    `o${c2}NMMMMMMMNNNmmmddddhhdmMNhs${c1}+`
  `s${c2}NMMMMMMMMNNNmmmdddddmNMmhs${c1}/.
 /N${c2}MMMMMMMMNNNNmmmdddmNMNdso${c1}:`
+M${c2}MMMMMMNNNNNmmmmdmNMNdso${c1}/-
yM${c2}MNNNNNNNmmmmmNNMmhs+/${c1}-`
/h${c2}MMNNNNNNNNMNdhs++/${c1}-`
`/${c2}ohdmmddhys+++/:${c1}.`
  `-//////:--.
  """
    print gentoo

def veryImportantCalculations():
    time.sleep(1.5)
    return random.randint(0,100)



if __name__ == "__main__":
    printBanner()

    name1 = raw_input("What is your name?\n")
    name2 = raw_input("What is you interests name?\n")
    gent = raw_input("Are you a /g/entooman? [YES/{NO}]")
    print "Calculating"
    
    if gent.lower() == "yes":
        sp.call('clear',shell=True)
        printBannerG()
        print "WTF were you thinking. " + name2 + " is fucking Chad, or Stacy, or both of them at the same time. When is the last time you installed Gentoo? Shit, I bet you have not even installed Gentoo in your mom's SmartTV. Go buy a ThinkPad and while you are at it, get a couple of DragonDildos to shove up your ass the next time you even dare to think about any possible intaraction with another human being."
    

    else:
        probability = str(veryImportantCalculations())
        print "The probabiltiy of you two finding love is " + probability + "%"

