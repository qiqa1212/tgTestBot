  


def cath(my_dict):
   allDict= {}
   new_clear = {}
   for key in my_dict:
      if isinstance(my_dict[key], dict):
         allDict[key]= my_dict[key]

      elif my_dict[key] != None:
         new_clear[key] = my_dict[key]
   return allDict, new_clear

   
   
   

def main():
   message = {'content_type': 'text', 
              'id': 49, 
              'message_id': 49, 
              'from_user': {'id': 6612544010, 
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
                            'has_main_web_app': None}, 
                            'date': 1730066326, 
                            'chat': {'id': 6612544010, 
                                     'type': 'private', 
                                     'title': None, 
                                     'username': None, 
                                     'first_name': 
                                     'саша добрый', 
                                     'last_name': None, 
                                     'is_forum': None, 
                                     'max_reaction_count': None, 
                                     'photo': None, 
                                     'bio': None, 
                                     'join_to_send_messages': None, 
                                     'join_by_request': None, 
                                     'has_private_forwards': None, 
                                     'has_restricted_voice_and_video_messages': None, 
                                     'description': None, 
                                     'invite_link': None, 
                                     'pinned_message': None, 
                                     'permissions': None, 
                                     'slow_mode_delay': None, 
                                     'message_auto_delete_time': None, 
                                     'has_protected_content': None, 
                                     'sticker_set_name': None, 
                                     'can_set_sticker_set': None, 
                                     'linked_chat_id': None, 
                                     'location': None, 
                                     'active_usernames': None, 
                                     'emoji_status_custom_emoji_id': None, 
                                     'has_hidden_members': None, 
                                     'has_aggressive_anti_spam_enabled': None, 
                                     'emoji_status_expiration_date': None, 
                                     'available_reactions': None, 
                                     'accent_color_id': None, 
                                     'background_custom_emoji_id': None, 
                                     'profile_accent_color_id': None, 
                                     'profile_background_custom_emoji_id': None, 
                                     'has_visible_history': None, 
                                     'unrestrict_boost_count': None, 
                                     'custom_emoji_sticker_set_name': None, 
                                     'business_intro': None, 
                                     'business_location': None, 
                                     'business_opening_hours': None, 
                                     'personal_chat': None, 
                                     'birthdate': None, 
                                     'can_send_paid_media': None
                                     }, 
                              'sender_chat': None, 
                              'is_automatic_forward': None, 
                              'reply_to_message': None, 
                              'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 
                              'author_signature': None, 'text': '/info', 'entities': ["telebot.types.MessageEntity object at 0x000002D6C18D11F0"] , 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None, 'chat_background_set': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'users_shared': None, 'chat_shared': None, 'story': None, 'external_reply': None, 'quote': None, 'link_preview_options': None, 'giveaway_created': None, 'giveaway': None, 'giveaway_winners': None, 'giveaway_completed': None, 'forward_origin': None, 'boost_added': None, 'sender_boost_count': None, 'reply_to_story': None, 'sender_business_bot': None, 'business_connection_id': None, 'is_from_offline': None, 'effect_id': None, 'show_caption_above_media': None, 'paid_media': None, 'refunded_payment': None, 'proximity_alert_triggered': None, 'video_chat_scheduled': None, 'video_chat_started': None, 'video_chat_ended': None, 'video_chat_participants_invited': None, 'web_app_data': None, 'message_auto_delete_timer_changed': None, 'json': {'message_id': 49, 'from': {'id': 6612544010, 'is_bot': False, 'first_name': 'саша добрый', 'language_code': 'ru'}, 'chat': {'id': 6612544010, 'first_name': 'саша добрый', 'type': 'private'}, 'date': 1730066326, 'text': '/info', 'entities': [{'offset': 0, 'length': 5, 'type': 'bot_command'}]}}
   dicts, new_withot= cath(message)
   for key in new_withot:
      if  isinstance(new_withot[key], dict):
         pass
      else: 
         print(key, new_withot[key])


main()