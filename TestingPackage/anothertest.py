#from TestingPackage.MyString import MyString
from MyString import MyString
s=MyString("I Went To The Park")
print("string is", s.getString())
print("vowels are", s.getVowels())
# Returns a string that consists of the substring between start and end indexes (both included) in the current string.
# Index 1 corresponds to the first character in the current string.'''
print("substring is ' We' ", s.getSubstring(2, 4))
