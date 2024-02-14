package DSA.LinkedList;

public class Deletion {
    
    public void deleteFirstNode() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        Node temp = head;
        head = head.next;
        temp = null; // This line is optional. It's just to free up the memory.
        // System.out.println("First node has been deleted successfully");
    }
    
    
}
