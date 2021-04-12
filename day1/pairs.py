import time

def multiply_pair_components(input):
  first, second = find_pairs_that_sum_to_2020(input)[0]
  return (first * second)

def multiply_triples_components(input):
  t0 = time.time()
  first, second, third = find_triples_that_sum_to_2020(input)[0]
  t1 = time.time()
  print(t1-t0)
  return (first * second * third)

def find_pairs_that_sum_to_2020(input):
  return [(first,second) for first in input for second in input if first + second == 2020]

def find_triples_that_sum_to_2020(input):
  # for idx, i in enumerate(input):
  #   for idx2, j in enumerate(input[idx+1:]):
  #     for k in input[idx2+1:]:
  #       if (i+j+k == 2020):
  #         return (i*j*k)
  return [(first,second,third) for idx1,first in enumerate(input) 
  for idx2,second in enumerate(input[idx1+1:]) 
  for third in input[idx2+1:] 
  if first + second + third == 2020]




if __name__ == '__main__':
  data = list(map(int, open("input.txt", "r").readlines()))
  print("part 1")
  print(multiply_pair_components(data))
  print("part 2")
  print(multiply_triples_components(data))