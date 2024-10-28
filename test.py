
start = 0
end = 0 

def openFun(list):
   temp_list = str(list)
   for i in range(len(temp_list)):
      if temp_list[i] == '{':
         print
         start = i
      elif i == 0:
         continue
      elif temp_list[-i] == '}':
         end = -i
         break

   new_list = temp_list[start+1:end-1]
   return new_list

def changing(list):
   pos = 1
   start = None
   end = None
   for i in range(len(list)):
      
      if  list[i] == "'" and list[i+3] == "{":
         print("second list")
         myFunc(list[i:])
      elif list[i] == "'" and pos == 1:
         pos = 0
         start = i
      elif list[i] == "'" and pos == 0:
         pos = 1
         end = i
      
      if start != None and end != None:
         print(list[start+1:end])
         start = None
         end = None
      
         



def myFunc(list):
   new = openFun(list)
   changing(new)


def main():
   message = {
       'content_type': 'text', 
       'id': 32, 
       'message_id': 32, 
       'from_user': {
           'id': 6612544010, 
           'is_bot': False, 
           'first_name': 'саша добрый', 
           'username': None, 
           'last_name': None, 
           'language_code': 'ru', 
           'can_join_groups': None, 
           'can_read_all_group_messages': None, 
           'supports_inline_queries': None, 
           'is_premium': None, 
           'added_to_attachment_menu': None, 
           'can_connect_to_business': None, 
           'has_main_web_app': None
       }, 
       'date': 1730065737, 
       'chat': {
           'id': 6612544010, 
           'type': 'private', 
           'title': None, 
           'username': None, 
           'first_name': 'саша добрый', 
           'last_name': None, 
           'is_forum': None
       }
   }
   res = myFunc(message)
   print(res)
   print('end')

main()