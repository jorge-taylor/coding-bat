def in1to10(n, outside_mode):
  return(not outside_mode and 1 <= n <= 10 or outside_mode and (n <= 1 or n >= 10))
