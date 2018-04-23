/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package datastructures_in_2018;
import java.util.*;
/**
 *
 * @author puneet
 */
public class DataStructures_in_2018 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        LinkedList l = new LinkedList();
        int data = sc.nextInt();
        l.addNodeToLast(data);
        int k = sc.nextInt();
        l.addNodeToLast(k);
        int m = sc.nextInt();
        l.addElementToIndex(m, 1);
        l.traverseList();
    }
    
}
