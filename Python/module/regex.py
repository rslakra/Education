#
# Author: Rohtash Lakra
#

# Python Regex Metacharacters
# The real power of regex matching in Python emerges when <regex> contains special characters called metacharacters.
# These have a unique meaning to the regex matching engine and vastly enhance the capability of the search.
import re

s = 'foo123bar'

# re.search(<regex>, <string>)
# re.search(<regex>, <string>) scans <string> looking for the first location where the pattern <regex> matches.
# If a match is found, then re.search() returns a match object. Otherwise, it returns None.
#
# re.search() takes an optional third <flags> argument that you’ll learn about at the end of this tutorial.
if re.search('123', s):
    print('Found a match.')
else:
    print('No match.')


# In a regex, a set of characters specified in square brackets ([]) makes up a character class.
# This metacharacter sequence matches any single character that is in the class
print(re.search('[0-9][0-9][0-9]', s))

# [0-9] matches any single decimal digit character—any character between '0' and '9', inclusive.
# The full expression [0-9][0-9][0-9] matches any sequence of three decimal digit characters.
# In this case, s matches because it contains three consecutive decimal digit characters, '123'.

# Take a look at another regex metacharacter.
# The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard:
print(re.search('1.3', s))

# Metacharacters Supported by the re Module
# The following table briefly summarizes all the metacharacters supported by the re module. Some characters serve more
# than one purpose:
#   ----------------|----------------------------------------------------------------
#   Character(s)    |   Meaning
#   ----------------|----------------------------------------------------------------
#   .               |   Matches any single character except newline
#   ----------------|----------------------------------------------------------------
#   ^	            |   ∙ Anchors a match at the start of a string
#                   |   ∙ Complements a character class
#   ----------------|----------------------------------------------------------------
#   $	            |   Anchors a match at the end of a string
#   ----------------|----------------------------------------------------------------
#   *	            |   Matches zero or more repetitions
#   ----------------|----------------------------------------------------------------
#   +	            |   Matches one or more repetitions
#   ----------------|----------------------------------------------------------------
#   ?	            |   ∙ Matches zero or one repetition
#                   |   ∙ Specifies the non-greedy versions of *, +, and ?
#                   |   ∙ Introduces a lookahead or lookbehind assertion
#                   |   ∙ Creates a named group
#   ----------------|----------------------------------------------------------------
#   {}	            |   Matches an explicitly specified number of repetitions
#                       {m} - Matches exactly m repetitions of the preceding regex.
#                       This is similar to * or +, but it specifies exactly how many times the preceding regex must
#                       occur for a match to succeed:
#                       {m,n} - Matches any number of repetitions of the preceding regex from m to n, inclusive.
#                       Omitting m implies a lower bound of 0, and omitting n implies an unlimited upper bound:
#                       If you omit all of m, n, and the comma, then the curly braces no longer function as
#                       metacharacters. {} matches just the literal string '{}':
#                       In fact, to have any special meaning, a sequence with curly braces must fit one of the
#                       following patterns in which m and n are non-negative integers:
#                       {m,n}
#                       {m,}
#                       {,n}
#                       {,}
#                       Otherwise, it matches literally:
#   ----------------|----------------------------------------------------------------
#   \	            |   ∙ Escapes a metacharacter of its special meaning
#                   |   ∙ Introduces a special character class
#                   |   ∙ Introduces a grouping backreference
#   ----------------|----------------------------------------------------------------
#   []	            |   Specifies a character class
#   ----------------|----------------------------------------------------------------
#   |	            |   Designates alternation
#   ----------------|----------------------------------------------------------------
#   ()	            |   Creates a group
#   :
#   #
#   =
#   ----------------|----------------------------------------------------------------
#   !	            |   Designate a specialized group
#   ----------------|----------------------------------------------------------------
#   <>	            |   Creates a named group
#   ----------------|----------------------------------------------------------------
# This may seem like an overwhelming amount of information, but don’t panic! The following sections go over each one of
# these in detail.


#   ----------------|----------------------------------------------------------------
#   \w	            |   Match based on whether a character is a word character.
#                       \w matches any alphanumeric word character.
#                       Word characters are uppercase and lowercase letters, digits, and the underscore (_) character,
#                       so \w is essentially shorthand for [a-zA-Z0-9_], and
#   \W                  \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]
#   ----------------|----------------------------------------------------------------
#   \d              |   Match based on whether a character is a decimal digit.
#   \D                  \d is essentially equivalent to [0-9], and
#                       \D is equivalent to [^0-9].
#   ----------------|----------------------------------------------------------------
#   \s              |   Match based on whether a character represents whitespace.
#   \S                  \s matches any whitespace character:
#                       Note that, unlike the dot wildcard metacharacter, \s does match a newline character.
#                       \S is the opposite of \s. It matches any character that isn’t whitespace:
#                       Again, \s and \S consider a newline to be whitespace.
#   ----------------|----------------------------------------------------------------

# The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well

#   ----------------|----------------------------------------------------------------
# *?                |   The non-greedy (or lazy) versions of the *, +, and ? quantifiers.
# +?
# ??
#                       When used alone, the quantifier metacharacters *, +, and ? are all greedy, meaning they produce
#                       the longest possible match.
#                       Consider this example:
#                           re.search('<.*>', '%<foo> <bar> <baz>%')
#                       <_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>
#                       If you want the shortest possible match instead,
#                       then use the non-greedy metacharacter sequence *?:
#                       <_sre.SRE_Match object; span=(1, 6), match='<foo>'>
#                       There are lazy versions of the + and ? quantifiers as well:
#   ----------------|----------------------------------------------------------------



# Supported Regular Expression Flags
# The table below briefly summarizes the available flags. All flags except re.DEBUG have a short, single-letter name
# and also a longer, full-word name:
#
#   ----------------|---------------|----------------------------------------------------------------
#   Short Name  |   Long Name       |   Effect
#   re.I        | re.IGNORECASE     | Makes matching of alphabetic characters case-insensitive
#   re.M        | re.MULTILINE      | Causes start-of-string and end-of-string anchors to match embedded newlines
#   re.S        | re.DOTALL         | Causes the dot metacharacter to match a newline
#   re.X        | re.VERBOSE        | Allows inclusion of whitespace and comments within a regular expression
#   ----        | re.DEBUG          | Causes the regex parser to display debugging information to the console
#   re.A        | re.ASCII          | Specifies ASCII encoding for character classification
#   re.U        | re.UNICODE        | Specifies Unicode encoding for character classification
#   re.L        | re.LOCALE         | Specifies encoding for character classification based on the current locale
#   ----------------|----------------------------------------------------------------
print(re.search('A+', 'aaaAAA', re.IGNORECASE))
# <_sre.SRE_Match object; span=(0, 6), match='aaaAAA'>



