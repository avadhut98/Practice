package DSA.LinkedList;

static class insertion {

    public void InsertFirst(int new_data){

        // Allocate the Node with new data
        Node new_node = new Node(new_data);
        // Make next of new Node as head
        new_node.next = head;
        // Move the head to point to new Node
        head = new_node;
    }

    public void InsertAtSpecificPosition(Node prev_node, int new_data){
        // Check if the given Node is null
        if (prev_node == null){
        System.out.println("The given previous node cannot be null");
        return;
        }
        // Allocate the Node with new data
        Node new_node = new Node(new_data);
        // Make next of new Node as next of prev_node
        new_node.next = prev_node.next;
        // Make next of prev_node as new_node
        prev_node.next = new_node;
    }

    public int InsertAtEnd(int new_data){
        /* 1. Allocate the Node &
        2. Put in the data
        3. Set next as null */
        Node new_node = new Node(new_data);
        // If the Linked List is empty, then make the new node as head
        if (head == null){
        head = new Node(new_data);
        return;
        }
        // This new node is going to be the last node, so make next of it as null
        new_node.next = null;
        // Else traverse till the last node
        Node last = head;
        while (last.next != null)
        last = last.next;
        // Change the next of last node
        last.next = new_node;
        return;
        }


}
        