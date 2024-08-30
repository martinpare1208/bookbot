def main():
  path = r'books/frankenstein.txt'
  with open(path) as f:
    file_contents = f.read()
    aggregate_report(file_contents)
    
#Count the occurences of words
def count_words(content):
  return len(content.split())

#Count each individual lowercased character
def count_characters(content):
  a_dict = {}
  for each_word in content:
    each_word = each_word.lower()
    for each_char in each_word:
      if each_char not in a_dict and each_char.isalpha():
        a_dict[each_char] = 1
      elif each_char in a_dict and each_char.isalpha():
        a_dict[each_char] += 1
  return a_dict

def sort_on(dict):
  return dict["num"]

def aggregate_report(content):
  word_count = count_words(content)
  char_count = count_characters(content)
  formatted_list = []
  for k, v in char_count.items():
    entry = {}
    entry["char"] = k
    entry["num"] = v
    formatted_list.append(entry)
    
  formatted_list.sort(reverse=True, key=sort_on)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  print("")
  for each_dict in formatted_list:
    print(f"The '{each_dict['char']}' character was found {each_dict['num']} times")
    
  
main()
