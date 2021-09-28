def find_happy_number(num):
  # TODO: Write your code here
  fast, slow = num, num
  # use while True, must have a break condition!!!
  # why exact same as answer, but wrong....!!!
  while True:
    slow = find_square_sum(slow)
    fast = find_square_sum(find_square_sum(fast))
    if slow == fast:
      break
  return slow == 1
