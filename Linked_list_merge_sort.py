from Linked_List import LinkedList
def merge_sort(linked_list):
    if linked_list.size() == 1 or linked_list.head is None:
      return linked_list

    left_half, right_half = split(linked_list)
    
    return merge(merge_sort(left_half), merge_sort(right_half))

def split(linked_list):
    if linked_list is None or linked_list.head is None:
        return linked_list, None

    size = linked_list.size()
    mid_node_index = size // 2

    left_half = LinkedList()
    right_half = LinkedList()

    current_node = linked_list.head
    for i in range(mid_node_index):
        left_half.insert(current_node.data)
        current_node = current_node.next

    while current_node:
        right_half.insert(current_node.data)
        current_node = current_node.next

    return left_half, right_half
  
    if linked_list is None or linked_list.head is None:
      return linked_list, None

    size = linked_list.size()
    
    mid_node_index= size // 2
    
    mid_node_prev= linked_list.node_at_index(mid_node_index - 1)

    
    left_half= LinkedList()
    
    left_half.head= linked_list.head
    
    
    
    right_half= LinkedList()
    
    right_half.head= mid_node_prev.next
    
    mid_node_prev.next=None
    
    return left_half,right_half

def merge(left, right):  
  merged= LinkedList()
  
  merged.insert(0)
  
  curr= merged.head
  
  
  left_head= left.head
  
  right_head= right.head
  
  
  while left_head or right_head:   
    if left_head is None:
      curr.next= right_head 
      break 
      
    elif right_head is None: 
      curr.next= left_head 
      break 

    if left_head.data < right_head.data: 
      curr.next= left_head 
      left_head= left_head.next 
      
    else: 
      curr.next= right_head 
      right_head= right_head.next 

    curr= curr.next 

  merged.head= merged.head.next 

  return merged 

idk = LinkedList()
idk.insert(6)
idk.insert(4)
idk.insert(2)
idk.insert(10)
idk.insert(5)

print(merge_sort(idk))
print(idk)