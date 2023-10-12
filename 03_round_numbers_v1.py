def round_ans(val):
  return "{:.0f}".format(val)

test_cases = [0.5, 0.2, 1.9, 0.51]
for item in test_cases:
  rounded = round_ans(item)
  print("{} is rounded to {}".format(item, rounded))