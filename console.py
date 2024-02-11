#!/usr/bin/python3
"""
this is a modul of console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def splitbraces(e_arg):
    """
    this is a method to split a curly braces
    """
    bra = re.search(r"\{(.*?)\}", e_arg)

    if bra:
        commaid = shlex.split(e_arg[:bra.span()[0]])
        id = [i.strip(",") for i in commaid][0]

        datastring = bra.group(1)
        try:
            arg_dict = ast.literal_eval("{" + datastring + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


class HBNBCommand(cmd.Cmd):
    """
    class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        for empty line
        """
        pass

    def do_EOF(self, arg):
        """
        end of file
        """
        return True

    def do_quit(self, arg):
        """
        exit
        """
        return True

    def do_create(self, arg):
        """
        create
        """
        com = shlex.split(arg)

        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{commands[0]}()")
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """
        show
        """
        com = shlex.split(arg)

        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(com) < 2:
            print("** instance id missing **")
        else:
            jects = storage.all()

            key = "{}.{}".format(com[0], com[1])
            if key in jects:
                print(jects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        destory
        """
        com = shlex.split(arg)

        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(com) < 2:
            print("** instance id missing **")
        else:
            jects = storage.all()
            key = "{}.{}".format(com[0], com[1])
            if key in jects:
                del jects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        do all
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        count
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        upadate
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                bra = re.search(r"\{(.*?)\}", arg)

                if bra:
                    try:
                        datastring = bra.group(1)

                        arg_dict = ast.literal_eval("{" + datastring + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        try:
                            attr_name1 = attribute_names[0]
                            attr_value1 = attribute_values[0]
                            setattr(obj, attr_name1, attr_value1)
                        except Exception:
                            pass
                        try:
                            attr_name2 = attribute_names[1]
                            attr_value2 = attribute_values[1]
                            setattr(obj, attr_name2, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                obj.save()

    def default(self, arg):
        """
        defult
        """
        arg_list = arg.split('.')

        cls_nm = arg_list[0]  # incoming class name

        command = arg_list[1].split('(')

        cmd_met = command[0]  # incoming command method

        e_arg = command[1].split(')')[0]  # extra arguments

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met]("{} {}".format(cls_nm, e_arg))
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = splitbraces(e_arg)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_met]
                    return call("{} {} {}".format(cls_nm, obj_id, arg_dict))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
