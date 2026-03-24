
def set_final_operation(a_set,b_set,d_set={2,3,4,5,6}):
    
    #perform union set, intersection set and difference set operation
    union_set=a_set.union(b_set)
    intersection_set=a_set.intersection(b_set)
    difference_set=a_set.difference(b_set)

    final_result=f"The union set is {union_set}. Intersection set is {intersection_set}. Difference set is {difference_set}"
    return final_result


     
# declare two sets
set_A = {1,2,3,4,5,6}
set_B={3,4,5,6,7,8}
final_res=set_final_operation(set_A,set_B)
print(final_res)