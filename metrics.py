def accuracy(y_test, y):
  cont = 0
  for i in range(len(y)):
    if y[i] == y_test[i]:
      cont += 1
  return cont / float(len(y))


def f_measure(y_test, y, beta=1):
  tp = 0.0 # true pos
  fp = 0.0 # false pos
  tn = 0.0 # true neg
  fn = 0.0 # false neg
  for i in range(len(y)):
    if y_test[i] == 1.0 and y[i] == 1.0:
      tp += 1.0
    elif y_test[i] == 1.0 and y[i] == 0.0:
      fp += 1.0
    elif y_test[i] == 0.0 and y[i] == 0.0:
      tn += 1.0
    elif y_test[i] == 0.0 and y[i] == 1.0:
      fn += 1.0
  if (tp + fp) != 0.0:
    precision = tp / (tp + fp)
  else:
    precision = 0.0
  if (tp + fn) != 0.0:
    recall = tp / (tp + fn)
  else:
    recall = 0.0
  if (((beta ** 2.0) * precision) + recall) != 0:
    resultado = (1.0 + (beta ** 2.0)) * ((precision * recall) / (((beta ** 2.0) * precision) + recall))
  else:
    resultado = 0.0
  return resultado
