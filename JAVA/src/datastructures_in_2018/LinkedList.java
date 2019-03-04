/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package datastructures_in_2018;

/**
 *
 * @author puneet
 */
public class LinkedList {
    Node head;
    void addNodeToLast(int d){
        Node n = new Node(d);
        
        if(head == null){
            head = n;
            return;
        }
        Node current=head;
            while(current.next!=null) {
                current=current.next;
            }
            current.next = n;
    }
    
    void addElementToIndex(int data, int index){
        Node n = new Node(data);
        Node current = head;
        Node n1;
        for(int i=1;i<index;i++) {
           current=current.next;
        }
        n1=current.next;
        
        current.next=n;
        n.next=n1;
    }
    
    void traverseList() {
        Node current = head;
        while(current!=null) {
            System.out.print(current.data + " ");
            current=current.next;
        }
        System.out.println();
    }
}


