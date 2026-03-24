from collections import Counter


def list_final_task(orig_list):

    #Remove duplicates
    unique_num_list=[]
    for i in orig_list:
        if i not in unique_num_list:
            unique_num_list.append(i)
    
     # Find Unique values from the original list
    unique_val= list(set(orig_list))

   #  count the number of duplicate 
    count_num=dict(Counter(orig_list))

   #Return  the results individually in the dictionary form
    dict_of_tasks={
        'Original_List':orig_list,
        'Unique_Values' : unique_val,
        'Counts': count_num
    }
    
    #return the final result
    return dict_of_tasks

#original List
num_lists=[1,2,2,3,4,5,5,5,6,6,7,7,7,8,8,9,9,9]
final_result=list_final_task(num_lists)
print(final_result)