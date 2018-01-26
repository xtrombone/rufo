#~# ORIGINAL

 [  ]

#~# EXPECTED

[]

#~# ORIGINAL

 [  1 ]

#~# EXPECTED

[1]

#~# ORIGINAL

 [  1 , 2 ]

#~# EXPECTED

[1, 2]

#~# ORIGINAL

 [  1 , 2 , ]

#~# EXPECTED

[1, 2]

#~# ORIGINAL
#~# print_width: 4

 [
 1 , 2 ]

#~# EXPECTED

[
  1,
  2,
]

#~# ORIGINAL
#~# print_width: 4

 [
 1 , 2, ]

#~# EXPECTED

[
  1,
  2,
]

#~# ORIGINAL
#~# print_width: 4

 [
 1 , 2 ,
 3 , 4 ]

#~# EXPECTED

[
  1,
  2,
  3,
  4,
]

#~# ORIGINAL
#~# print_width: 4

 [
 1 ,
 2]

#~# EXPECTED

[
  1,
  2,
]

#~# ORIGINAL

 [  # comment
 1 ,
 2]

#~# EXPECTED

[ # comment
  1,
  2,
]

#~# ORIGINAL

 [
 1 ,  # comment
 2]

#~# EXPECTED

[
  1, # comment
  2,
]

#~# ORIGINAL
#~# print_width: 4

 [  1 ,
 2, 3,
 4 ]

#~# EXPECTED

[
  1,
  2,
  3,
  4,
]

#~# ORIGINAL

 [  1 ,
 2, 3,
 4, ]

#~# EXPECTED

[1, 2, 3, 4]

#~# ORIGINAL

 [  1 ,
 2, 3,
 4,
 ]

#~# EXPECTED

[1, 2, 3, 4]

#~# ORIGINAL

 [ 1 ,
 2, 3,
 4, # foo
 ]

#~# EXPECTED

[
  1,
  2,
  3,
  4, # foo
]

#~# ORIGINAL

 begin
 [
 1 , 2 ]
 end

#~# EXPECTED

begin
  [1, 2]
end

#~# ORIGINAL

 [
 1 # foo
 ]

#~# EXPECTED

[
  1, # foo
]

#~# ORIGINAL

 [ *x ]

#~# EXPECTED

[*x]

#~# ORIGINAL

 [ *x , 1 ]

#~# EXPECTED

[*x, 1]

#~# ORIGINAL

 [ 1, *x ]

#~# EXPECTED

[1, *x]

#~# ORIGINAL

 x = [{
 foo: 1
}]

#~# EXPECTED

x = [{foo: 1}]

#~# ORIGINAL

[1,   2]

#~# EXPECTED

[1, 2]

#~# ORIGINAL

[
  1,
  # comment
  2,
]

#~# EXPECTED

[
  1,
  # comment
  2,
]

#~# ORIGINAL
#~# print_width: 5

[
  *a,
  b,
]

#~# EXPECTED

[
  *a,
  b,
]

#~# ORIGINAL
#~# print_width: 5

[
  1, *a,
  b,
]

#~# EXPECTED

[
  1,
  *a,
  b,
]

#~# ORIGINAL nested_array_with_brackets

[([1,2]), ([3,4]), ([5,6])]

#~# EXPECTED

[([1, 2]), ([3, 4]), ([5, 6])]

#~# ORIGINAL array_with_method_call

[a(1)]

#~# EXPECTED

[a(1)]

#~# ORIGINAL array_with_ternary

[true ? 1 : 2]

#~# EXPECTED

[true ? 1 : 2]

#~# ORIGINAL array_with_indexing_element

[a[:b]]

#~# EXPECTED

[a[:b]]

#~# ORIGINAL array_with_symbol

[:a]

#~# EXPECTED

[:a]

#~# ORIGINAL nested_array_splat

[[], *a]

#~# EXPECTED

[[], *a]

#~# ORIGINAL nested_different_array_types

[%w[( )]]

#~# EXPECTED

[%w[( )]]