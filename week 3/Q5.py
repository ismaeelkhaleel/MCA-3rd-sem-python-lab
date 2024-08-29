def remove_chars(input_str, a):
    return input_str[:a-1]


if __name__ == "__main__":

  input_str = str(input("Enter a String : "))
  a = int(input("Enter a index : "))
  
  print(remove_chars(input_str,a))

