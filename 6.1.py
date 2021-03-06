def count_positives_sum_negatives(arr):
    
    if not arr:
        return []
    positives = 0
    negatives = 0
    for x in arr:
      if x > 0:
          positives += 1
      if x < 0:
          negatives += x
    return [positives, negatives]