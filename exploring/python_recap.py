import re 
import functools

a = [1,2,3,4,5]

functools.reduce(lambda x, y: x + y, a)
re.sub("ll", "xxx", "hello")

print("%s, %7.2f" % ("Cathy", 13.4375)) # the precision on the float also rounds


# List comprehension
[(x ** 2) for x in range(100) if (x % 2 == 0)] # More like calculus style



def simpleGen(): 
  mylist = range(5)
  for x in mylist:
     yield x*x
      
myGen = simpleGen() # create a generator 
print(myGen) # mygenerator is an object! <generator object createGenerator at 0xb8555d21>

for x in myGen: # It prints numbers!
  print(x) 





"""
What’s new in the Python world in 2020
While the existence of Python 3 is definitely not news, let’s take a quick look
at this most recent version of the language. It was first presented in December
2008. Despite the fact that the actual current version (3.8) differs slightly
from its 3.0 (or Py3k) predecessor, changes haven’t been huge, at least in
terms of compatibility.

The shift between versions 3 and 2, on the other hand, was big. There is no
backwards compatibility at all. As such, it might surprise you that, even as
recently as 2-4 years ago, there was no clear preference between versions 2 and
3. No backwards compatibility would mean porting multiple legacy applications
and modules, which wasn’t a trivial task. Those who felt it wouldn’t be a
worthwhile endeavour simply continued on with Python 2. The community didn’t so
much resist the change as it avoided it - but only for a time.

As of 01.01.2020, Python 2 is officially dead. That is, it has been retired.
Those of us new to the world of Python development, or at least those not
working on legacy apps, don’t need to worry about the change very much. (It’s a
lot like what happened with Ruby 1.9). Those whose Python 2.x apps are still
operational might need to consider switching to Python 3 in the near future.

Python from a Ruby expert’s perspective - tools of the trade
Every programmer has their own preferred set of tools, patterns and well-known
solutions. Because of this, you might be reluctant to make the switch from Ruby
to Python, as you wouldn’t have access to all the things you like. But worry
not! We’ve prepared a quick breakdown of what’s available for both of these
languages, and how the tools available compare to each other.

IDE
If you’re coming from the RubyMine world, then starting your journey with
Python using PyCharm should be pretty painless. The whole IDE is almost
identical, with only minor colour changes and language specific features. Which
is hardly surprising, as the same company created both.

You might also want to take a look at other solutions, such as Spyder (if
you’re interested in data analytics and data science), or PyDev which is
essentially an Eclipse port for Python. Other plugins for a typical IDE include
Atom and Sublime Text. Everyone should be able to find something for
themselves.

Packages
In the Ruby world, package management is ruled by gems. Python has a close
equivalent, called pip. Using it is fairly straightforward, and it has received
recommendations by the Python core team.

Package versioning
By now you might be wondering about how to accomplish scenarios with multiple
versions of different packets under specific bags. We have good news for all
rvm, rbenv enthusiasts: there are viable alternatives in the Python ecosystem,
virtualenv and pyenv. It’s difficult to declare one superior to the other -
it’s a matter of personal preferences.

Working with virtualenv involves two main shell commands:

$ virtualenv ENV
$ source /path/to/ENV/bin/activate
you want. If you want to change them, just hit $ deactivate and it’s done.
Quick and easy.

Shell
Python offers its own shell, IPython, which allows for real-time
interpretation. In the Ruby world, we can call it Python’s irb alternative.
Like with Ruby, a developer can easily run snippets or load entire methods to
namespace and play around. Typically for an interpreter, IPython allows rapid
testing of new libraries and debugging.

Debugging
We all know that good and reliable software should be equipped with meaningful
test coverage. Despite that, we might need a tool for temporary fixes when
debugging something specific. In the Ruby ecosystem, we have Pry or ByeBug.
Python offers its own options, including ipdb and pdb. Both are good at what
they are meant to do.

Web frameworks
The most popular Python framework used for web development is Django. It’s
quite mature and popular, but has a very different philosophy compared to
Rails. Django emphasizes rapid development, but under the hood you won’t find
typical RoR magic (e.g. an overriden autoloader). Django represents the MTV
rather than the MVC approach. The framework’s strengths include really great
documentation, versatility, and its facilitation of rapid development.

For those who prefer more lightweight solutions, the Pyramid framework is a
nice option. Its learning curve is significantly lower, too. Another similar
framework is Flask, which is something of an alternative to Ruby’s Sinatra. It
might not be as robust as other frameworks, but it’s still rather popular,
particularly for data engineering work (thanks to its simple API and
hassle-free approach). For non-mainstream enthusiasts looking for a robust and
versatile framework (like Hanami in the Ruby World), the lightweight but
powerful Falcon can be a good choice.

Traps Ruby experts might fall into when working with Python
The order of parameters or callers might look a bit weird for Rubyists
Take a look at the following equivalent code samples. Of note: Both are doing
the exact same thing!

Ruby:

a = [1,2,3,4,5]

a.reduce(0) {|acc, el| acc = acc + el} # Alernatively a.reduce{|acc, el| acc += el}
a.map{ |x| x*x } # a.calls with block

"hello".gsub('ll', 'xxx')

printf("%s %7.2f\n", "Cathy", 13.4345)

# List comprehension
(0..99).select {|x| x % 2 == 0 }.map {|x| x ** 2 } # is likely easier to
understand than the Python’s Python:

import re 

a = [1,2,3,4,5]

reduce(lambda x, y: x + y, a) 
reduce(lambda x: x*x, a) # reduce takes lambda (with block) and takes ‘a’

re.sub("ll", "xxx", "hello")

print("%s, %7.2f" % ("Cathy", 13.4345))

# List comprehension
[(x ** 2) for x in range(100) if (x % 2 is 0)] # More like calculus style
It’s not an issue of which language is better, but a matter of proficiency and
convention. Anyone with a Ruby background might be momentarily confused. “I
cannot count how many times I tried to trigger in the wrong direction,” says
one of iRonin.IT’s developers.

The “yield” keyword is the same, but different
This difference, at least, is quite commonly known. A Ruby yield (with or
without a block) allows you to pass a set of extra instructions during a method
invocation. Whereas for Python, yield’s definition is more precise (and
concise, as is most of the language’s syntax). The keyword is used like return,
except the function will return a generator.

It’s crucial to understand that, whenever you call the function, the code
written in the function body does not run. All the function does is return the
generator object. That’s the difference between Python and Ruby.

def simpleGen(): 
  mylist = range(5)
  mylist = range(5)
  for x in mylist:
     yield x*x
      
myGen = simpleGen() # create a generator 
print(myGen) # mygenerator is an object! <generator object createGenerator at 0xb8555d21>

for x in myGen: # It prints numbers!
  print(x) 
Other important differences
With Python, you can legally pass one function to another function as a parameter (high-order function concepts). In Ruby, you can deal with this only indirectly - using Proc alt. lambda wrappings.
Both languages support closures, but in different ways. For Ruby, you can define closures with blocks. All closures have full read and write access to variables from the outer scope. For Python, you can define one function inside another one. The inner function has read-only access to variables from the outer function, and not full write access.
Python legally supports multiple inheritance. In Ruby, it is achievable only using mixins.
Python does not have switch/case statements. In Ruby, we have many variants.
In Python, there is no ternary operator in the form of: expr ? val1 : val2 at all (known from almost any other language). For a similar result, you can use val1 if expr else val2 - which obviously isn’t the same thing.
For else if expressions, a restricted keyword in Ruby is elsif, and in Python it’s elif.
Helpful similarities between Python and Ruby (not typical for other languages)
In both languages, you can use simultaneous assignment constructs, e.g.:
a,b = b,a # for value switch
The splat * operator (for unpacking):
Of note - for dicts **
Both languages have the ability to express code in a more FP manner (map,
filter, reduce concepts).  The entire exception handling flow in Ruby is
generally inspired by Python. Python’s [try, except, else, finally] are
respectively [begin, rescue, else, ensure] in Ruby.  In both Ruby and Python we
use # for comments.  Inside classes, a typical
reference to instance for many languages is this. In both Ruby and Python, we
have the self keyword.
In Ruby, we can handle multi-line strings through heredocs. You can also use
double quotation marks three times (" ""), which by default is also supported in
Python (along with using single quotation marks: ''').  A practical example
Because Python offers a splendid set of tools for general data-tinkering,
scientific calculations, as well as for machine learning like SkiPy learn,
Pandas, NumPy (Sklearn), etc., it’s always worth it to consider combining these
as a new microservice for an existing system which needs it (regardless of
technology). One of our clients faced this issue.

Their Ruby-based application focused on the S & OP area. At one point, its
offer needed to be extended with forecasting based on archived delivery data.
This goal was easiest to realize with linear regression, as well as classical
time series forecasting (in that specific case using ARIMA algorithms, among
other solutions) in a more advanced version. The code was quite concise. It
performed the aforementioned calculations and was offered its basic API, made
up of a couple of lines of Flask code.

The next step involved gently wrapping it as a Zappa project, in order to
easily deploy that specific code to AWS Lambda. The client required fast
response times and a reliable solution with a high uptime. It was easy-peasy to
add the newest Python API within the Ruby code in order to read specific data
and pass that further back to an existing pipeline. Everything ended up working
smoothly. This story shows how Ruby and Python can coexist within the same
project.



"""
