"""
Diffrent kind of inheritance
1. Single Inheritance
2. Multi level Inheritance
3. Hybrid Inheritance
4. Hirearchical Inheritance
"""

"""
Encapsulation:
Encapsulation is a mechanism where you bind your data and code together as a single unit. 
It also means to hide your data in order to make it safe from any modification.
What does this mean? The best way to understand encapsulation is to look at the example of a medical capsule, 
where the drug is always safe inside the capsule. Similarly, 
through encapsulation the methods and variables of a class are well hidden and safe.

We can achieve encapsulation in Python by:

Declaring the variables of a class as private(using double underscore).
Providing public setter and getter methods to modify and view the variables values.



Abstraction:
Abstraction refers to the quality of dealing with ideas rather than events. 
It basically deals with hiding the details and showing the essential things to the user. 
Example: whenever we get a call, we get an option to either pick it up or just reject it. 
But in reality, there is a lot of code that runs in the background. 
So you don’t know the internal processing of how a call is generated, that’s the beauty of abstraction. 
Therefore, abstraction helps to reduce complexity. 

Note: Abstraction in Java is done using Abstract class(0 - 100% abstraction) and Interface (100% abstraction)

In python:
You can or dont have to have constructor,depends on use case; also depends on how much abstraction you want to achieve
if you want to achive 100% they write pass statements for all the methods in parent class

A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.
The above statement works for Java and C++ when the subclass does not override the parent class; for python you need to
import abc which gives you @abstractmethod decorator 

class Polygon(ABC): 
  
    # abstract method 
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides")
        
        

Polymorphism:
What is Polymorphism : The word polymorphism means having many forms. In programming,
polymorphism means same function name (but different signatures) being uses for different types.
Polymorphism means taking many forms, where ‘poly’ means many and ‘morph’ means forms. 
It is the ability of a variable, function or object to take on multiple forms. 
In other words, polymorphism allows you define one interface or method and have multiple implementations.

Example:
Example of inbuilt polymorphic functions :
# Python program to demonstrate in-built poly- 
# morphic functions 

# len() being used for a string 
print(len("geeks")) 

# len() being used for a list 
print(len([10, 20, 30])) 


Example of used defined Polymorphic functions:
# A simple Python function to demonstrate 
# Polymorphism 

def add(x, y, z = 0): 
	return x + y+z 

# Driver code 
print(add(2, 3)) 
print(add(2, 3, 4)) 



Example of Polymorphism with inheritance:
class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): 
    print("Ostriches cannot fly.") 


Let’s consider this real world scenario in cricket, we know that there are different types of bowlers i.e. 
Fast bowlers, Medium pace bowlers and spinners. As you can see in the above figure, there is a parent class- BowlerClass
and it has three child classes: FastPacer, MediumPacer and Spinner. 
Bowler class has bowlingMethod() where all the child classes are inheriting this method. 
As we all know that a fast bowler will going to bowl differently as compared to medium pacer and 
spinner in terms of bowling speed, long run up and way of bowling, etc. Similarly a medium pacer’s implementation of 
bowlingMethod() is also going to be different as compared to other bowlers. And same happens with spinner class.
The point of above discussion is simply that a same name tends to multiple forms. All the three classes above inherited 
the bowlingMethod() but their implementation is totally different from one another.


# See runtime and compile time polymorphism (Not in py i think, exists in Java)
"""