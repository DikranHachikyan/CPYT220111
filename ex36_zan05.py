# глобална променлива

# 1. дефиниция на функцията

def sort_priority(values,group):
    found = False

    def sort_helper(el):
        nonlocal found
        if el in group:
            found = True
            return (0,el)
        return (1,el)
    

    values.sort(key=sort_helper)
    return found

if __name__ == '__main__':
#   
    # 2. извикване на функ.
    numbers = [5,4,3,2,1,9,8,7]
    grp = {4,8,9}

    is_found = sort_priority(numbers, grp)

    print(f'numbers:{numbers}, found={is_found}')

    print('---')