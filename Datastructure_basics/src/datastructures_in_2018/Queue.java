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
public class Queue {
        Node First;
        Node Last;
        void enque(int d) {
        Node n=new Node(d);
        if(Last==null) {
            First=Last=n;
            return;
        }
        Last.next=n;
        Last=n;
    }
        Node deque() {  //add more conditions.
            Node current=First;
            if(First!=null) {
                First = First.next;
            if(First==null) {
                Last=null;
            }
            }
            return current;
}
        void traverse() {
            Node current=First;
            while(current!=null) {
                System.out.print(current.data+ " ");
                current=current.next;
            }
        }   
}
