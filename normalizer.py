def min_max(data, numeric_columns=[], boolean=False):
  for column in data.columns:
    if column in numeric_columns:
      data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
      if boolean:
        data[column] = data[column] >= (data[column].max() - data[column].min()) / 2.0
  return data
