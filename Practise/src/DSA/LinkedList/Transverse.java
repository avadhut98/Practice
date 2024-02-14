package DSA.LinkedList;

public class Transverse {

    
    public void listTraverse(){
        Node n = head;
        while (n != null) {
        System.out.print(n.data + " ");
        n = n.next;
        }
        }
        
    
}
