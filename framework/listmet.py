
class ListMet():
    def _compars_mass(self,first_list, second_list, type_value=False):
        if len(first_list)!=len(second_list):
            return False
        if type_value is False:
            for i in range(0, len(first_list)):
                if first_list[i] != second_list[i]:
                    return first_list[i], second_list[i], i
        else:
            for i in range(0, len(first_list)):
                if eval(type_value + '({})'.format(first_list[i])) != eval(type_value +
                    '({})'.format(second_list[i])):
                    return (first_list[i], second_list[i], i)
