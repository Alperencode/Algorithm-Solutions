# Remove String Spaces
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5
def no_space(x):
    return ''.join([char for char in x if char != " "])

# Testcases
# no_space('8 j 8   mBliB8g  imjB8B8  jl  B') - '8j8mBliB8gimjB8B8jlB'
# no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd') - '88Bifk8hB8BB8BBBB888chl8BhBfd'
# no_space('8aaaaa dddd r     ') - '8aaaaaddddr'
# no_space('jfBm  gk lf8hg  88lbe8 ') - 'jfBmgklf8hg88lbe8'
# no_space('8j aam') - '8jaam'

# Status - Passed - 490ms