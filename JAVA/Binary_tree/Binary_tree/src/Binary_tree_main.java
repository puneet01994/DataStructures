/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author puneet
 */

import java.util.*;

public class Binary_tree_main {
    public static void main(String[] args){
        Binary_tree bt = new Binary_tree();

//        For traversals and lca.       
        
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        for(int i=0; i<n; i++){
//            bt.insert_Node(sc.nextInt());
//        }
//        
//        bt.levelOrderTraversal();
//        System.out.println("Inorder traversal");
//        bt.inOrderTraversal(bt.root);
//        System.out.println();
//        System.out.println("LCA of 21 and 23 is "+bt.FindLCA(bt.root, 21, 23).data);



//        For Constructing new binary tree from given pre-order and in-order traversals.

        ConstructBinaryTreeFromPreAndInOrder ct = new ConstructBinaryTreeFromPreAndInOrder();
        Scanner sc = new Scanner(System.in);
        
        int pre[] = new int[]{1,2,4,5,3,6};
        int in[] = new int[]{4,2,5,1,6,3};
//      
System.out.println("Enter preOrder");
//        for(int i=0; i>len; i++){
//            pre[i] = sc.nextInt();
//        }
//        
//        System.out.println("Enter inOrder");
//        for(int i=0; i<len; i++){
//            in[i] = sc.nextInt();
//        }

        int len = in.length;
        Node root = ct.buildTree(in, pre, 0, len-1);
        System.out.println("Pre Order traversal of the tree constructed with the help of pre and in-order");
        bt.inOrderTraversal(root);
    }
}
