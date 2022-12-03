#!/usr/bin/python3
"""
This file contains a class HBNBCommand
This file deals with the entire command
interpretor
The class uses cmd module
The command interpretor should implement
quit and EOF to exit the program
This class deals with providing custom prompt
upload fixed bug
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand is a subclass of the Cmd class of the cmd module\
    The class will help in building a console interface for manipulating data\
    and objects
    """
    prompt = '(hbnb) '
    __classes = ['BaseModel', 'User', 'State',
                 'City', 'Amenity', 'Place', 'Review']
    __commands = ['all', 'create', 'update', 'destroy', 'show']

    def default(self, arg):
        """ Enables consloe manipulate instance using commands like
        <class name>.command()"""
        if arg != "":
            try:
                class_name, command = arg.split(".")
                if class_name in HBNBCommand.__classes:
                    if command == "all()":
                        self.do_all(class_name)
                    elif command == "count()":
                        self.count(class_name)
                    elif command[0:4] == "show":
                        cmd = command[5:43].replace('"', '')
                        arg_id = class_name + " " + cmd
                        self.do_show(arg_id)
                    elif command[0:7] == "destroy":
                        cmd = command[8:46].replace('"', '')
                        arg_id = class_name + " " + cmd
                        self.do_destroy(arg_id)
                    else:
                        print("*** Unknown syntax: {}".format(arg))
                        return
            except error as e:
                my_list = list(arg.split(" "))
                if my_list[0] in HBNBCommand.__commands:
                    pass
                else:
                    print("*** Unknown syntax: {}".format(arg))

    def count(self, class_name):
        """ Implementation for counting objects of a class
        Usage: <class name>.count()"""
        get_objects = storage.all()
        count = 0
        for key, value in get_objects.items():
            class_nam, id_ = key.split(".")
            if class_nam == class_name:
                count += 1
        print(count)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Override empty lines function not to do default action.
        That is repeat last command when no command is given\n"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the called model,\
        saves it (to the JSON file) and prints the id
        """
        if arg != "":
            if arg in HBNBCommand.__classes:
                my_model = eval(arg)()
                storage.new(my_model.to_dict())
                storage.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based\
        on the class name and id
        """
        if arg != "":
            try:
                class_name, class_id = arg.split(" ")
            except ValueError:
                if arg in HBNBCommand.__classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
                return
            if class_name in HBNBCommand.__classes and class_id != "":
                my_dict = storage.all()
                my_id = class_name + "." + class_id
                try:
                    d = my_dict[my_id]
                    if "__class__" in d:
                        del d['__class__']
                except Exception as ex:
                    print("** no instance found **")
                    return
                my_object = "["+class_name+"] ({:s}) {}"
                my_object = my_object.format(class_id, d)
                print(my_object)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        try:
            class_name, class_id = arg.split(" ")
        except ValueError:
            if arg in HBNBCommand.__classes:
                print("** instance id missing **")
            elif arg != "":
                print("** class doesn't exist **")
            else:
                print("** class name missing **")
            return
        if class_name in HBNBCommand.__classes and class_id != "":
            my_dict = storage.all()
            my_id = class_name + "." + class_id
            try:
                del my_dict[my_id]
            except Exception as ex:
                print("** no instance found **")
                return
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based\
        or not on the class name.
        """
        if arg in HBNBCommand.__classes or arg == "":
            my_dict = {key: value for key, value in storage.all().items()}
            my_list = []
            for keys, v in my_dict.items():
                to_append = False
                if "__class__" in v:
                    del v['__class__']
                class_name, class_id = keys.split(".")
                my_object = "["+class_name+"] ({:s}) {}"
                if arg != "":
                    if class_name == arg:
                        to_append = True
                else:
                    to_append = True
                my_object = my_object.format(class_id, v)
                if to_append:
                    my_list.append(my_object)
            print(my_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and\
        id by adding or updating attribute
        """
        args_list = list(arg.split(" "))
        if len(args_list) < 4:
            if len(args_list) == 0:
                print("** class name missing **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            elif len(args_list) == 2:
                print("** attribute name missing **")
            elif len(args_list) == 3:
                print("** value missing **")
        else:
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            cls_model = args_list[0]
            cls_id = args_list[1]
            cls_attr = args_list[2]
            cls_val = args_list[3]
            cls_key = cls_model+'.'+cls_id
            my_dict = storage.all()
            try:
                my_obj = my_dict[cls_key]
                my_obj[cls_attr] = cls_val
                storage.save()
                print("hi")
            except Exception as ex:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
