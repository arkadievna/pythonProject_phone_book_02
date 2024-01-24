import text
import view
import model

def find_contact(phones: model.PhoneBook):
    word = view.input_data(text.input_search_word)
    result = phones.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

def start_app():
    pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
# В этой старой версии метод match не работает, выдаёт ошибку.
# В новой версии это будет работать:
        # match choice:
        #     case 1:
        #         pb.open_file()
        #     case 2:
        #         pass
        #     case 3:
        #         pass
        #     case 4:
        #         pass
        #     case 5:
        #         pass
        #     case 6:
        #         pass
        #     case 7:
        #         pass
        #     case 8:
        #         break

# в старой версии так:
        if choice == 1:
                  pb.open_file()
                  view.print_message(text.load_successful)
        elif choice == 2:
                  pb.save_file()
                  view.print_message(text.save_successful)
        elif choice == 3:
                  view.show_contacts(pb, text.empty_phone_book)
        elif choice == 4:
                  contact = view.add_contact(text.new_contact)
                  pb.new_contact(contact)
                  view.print_message(text.new_contact_added_successful(contact[0]))
        elif choice == 5:
            find_contact(pb)
        elif choice == 6:
            find_contact(pb)
            c_id = int(view.input_data(text.input_id_change_contact))
            c_contact = view.add_contact(text.change_contact, pb.phonebook[c_id])
            pb.change_contact(c_id, c_contact)
            view.print_message(text.contact_changed_successful(c_contact[0]))
        elif choice == 7:
            find_contact(pb)
            c_id = int(view.input_data(text.input_id_delete_contact))
            name = pb.delete_contact(c_id)[0]
            view.print_message(text.contact_delete_successful(name))
        elif choice == 8:
            view.print_message(text.good_bay)
            break